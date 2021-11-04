import pika
from retry import retry
from models.order_model import OrderModelSend


class OrderNotifier:
    def __init__(self) -> None:
        self.__conn = self.__get_connection()

    def notify(self, order: OrderModelSend):
        print("---------- IN OrderNotifier Notify ----------")
        self.__conn.basic_publish(exchange='',
                                  routing_key='order',
                                  body=order.json())

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='order')

        return channel
