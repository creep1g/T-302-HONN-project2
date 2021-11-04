import pika
from retry import retry
from card_validator import Validator
import json
from models.card_model import CardModel
from models.payment_model import PaymentModel
from notifier import PaymentNotifier
from payment_repository import PaymentRepository
from container import Container
from Settings import Settings


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbit1', port=5672)
    )

    channel = connection.channel()
    channel.queue_declare('order')
    channel.queue_declare('payment')
    return channel


def callback(ch, method, properties, body):
    body = body.decode("utf-8")

    body = json.loads(body)
    card = CardModel(**body["creditCard"])

    print('validating')
    valid = validator.validate(card)
    payment = PaymentModel(orderId=body["orderId"], success=valid)
    repo.create_payment(payment)
    notifier.notify(json.dumps(body), valid)


def arrange():
    container = Container()
    container.config.from_pydantic(Settings(_env_file='.env'))
    return container


if __name__ == '__main__':
    container = arrange()
    repo: PaymentRepository = container.payment_repository_provider()
    validator = Validator()
    notifier = PaymentNotifier()
    connection = get_connection()
    connection.basic_consume(queue='order',
                             on_message_callback=callback,
                             auto_ack=True)
    connection.start_consuming()
