from logging import Handler
from email_config import EmailConfig
from container import Container
import pika
from retry import retry
from container import Container
from Settings import Settings
from email_handler import EmailHandler
import json
import requests
from dependency_injector.wiring import Provide

merchant_service = "http://merchant_service:8001/merchants"
buyer_service = "http://buyer_service:8002/buyers"
inventory_service = "http://inventory_service:8003/products"


def arrange():
    container = Container()
    container.config.from_pydantic(Settings(_env_file='.env'))
    return container


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbit1', port=5672)
    )
    channel = connection.channel()
    channel.queue_declare(queue='paymentFailure')  # Declare a queue
    channel.queue_declare(queue='order')  # Declare a queue
    channel.queue_declare(queue='paymentSuccess')  # Declare a queue
    return channel


def callback_order(ch, method, properties, body):
    print("IN callback_order")
    body = body.decode("utf-8")
    body = json.loads(body)

    merchantId = (body["merchantId"])
    merchant = requests.get(f'''{merchant_service}/{merchantId}''').json()
    merchant_email = merchant["email"]
    buyerId = (body["buyerId"])
    buyer = requests.get(f'''{buyer_service}/{buyerId}''').json()
    buyer_email = buyer["email"]
    orderId = (body["orderId"])
    totalPrice = (body["totalPrice"])
    productId = (body["productId"])
    product = requests.get(f'''{inventory_service}/{productId}''').json()
    productName = product["productName"]
    handler = container.email_handler_provider()
    handler.order_created_email(
        merchant_email, buyer_email, orderId, productName, totalPrice)


def callback_payment_success(ch, method, properties, body):
    print(">>>>>>>>>< IN callback_payment_success <>>>>>>>>>>>>>>")
    body = body.decode("utf-8")
    body = json.loads(body)

    merchantId = (body["merchantId"])
    merchant = requests.get(f'''{merchant_service}/{merchantId}''').json()
    merchant_email = merchant["email"]

    buyerId = (body["buyerId"])
    buyer = requests.get(f'''{buyer_service}/{buyerId}''').json()
    buyer_email = buyer["email"]
    orderId = (body["orderId"])
    handler = container.email_handler_provider()
    handler.payment_successful_email(merchant_email, buyer_email, orderId)


def callback_payment_failed(ch, method, properties, body):
    print(">>>>>>>< IN callback_payment_failed >>>>>>><")
    body = body.decode("utf-8")
    body = json.loads(body)
    merchantId = (body["merchantId"])
    merchant = requests.get(f'''{merchant_service}/{merchantId}''').json()
    merchant_email = merchant["email"]

    buyerId = (body["buyerId"])
    buyer = requests.get(f'''{buyer_service}/{buyerId}''').json()
    buyer_email = buyer["email"]
    orderId = (body["orderId"])
    handler = container.email_handler_provider()
    handler.payment_failed_email(merchant_email, buyer_email, orderId)


if __name__ == '__main__':
    container = arrange()
    connection = get_connection()
    print("IN email main")
    connection.basic_consume(queue='paymentSuccess',
                             on_message_callback=callback_payment_success,
                             auto_ack=True)
    connection.start_consuming()
    connection.basic_consume(queue='order',
                             on_message_callback=callback_order,
                             auto_ack=True)
    connection.start_consuming()
    connection.basic_consume(queue='paymentFailure',
                             on_message_callback=callback_payment_failed,
                             auto_ack=True)
    connection.start_consuming()
