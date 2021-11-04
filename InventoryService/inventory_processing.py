import pika
from retry import retry


class inventory_processing():
    def __init__(self) -> None:
        self.__conn = self.__get_connection()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='payment-Success')
        channel.queue_declare(queue='payment-Failure')
        channel.basic_consume(
            queue='payment-Success', on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        # do something
        pass
