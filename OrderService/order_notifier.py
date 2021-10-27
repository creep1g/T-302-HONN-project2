import pika
from retry import retry
from models.order_model import OrderModel


class OrderNotifier:
    def __init__(self) -> None:
        self.__conn = self.__get_connection()

    def notify(self, order: OrderModel):
        self.__conn.basic_publish(exchange='',
                                        routing_key='order',
                                        body=order.json())

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='order')

        return channel
