import pika
from retry import retry


class PaymentNotifier:
    def __init__(self) -> None:
        self.__conn = self.__get_connection()

    def notify(self, body: dict, validation: bool):
        if validation:
            print("Payment Success")
            self.__conn.basic_publish(exchange='',
                                      routing_key='paymentSuccess',
                                      body=body)
        else:
            print("Payment Failed")
            self.__conn.basic_publish(exchange='',
                                      routing_key='paymentFailure',
                                      body=body)

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672)
        )
        channel = connection.channel()
        channel.queue_declare(queue='paymentSuccess')
        channel.queue_declare(queue='paymentFailure')

        return channel
