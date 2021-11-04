from dbConnections.db_connection import DbConnection
import pika
from retry import retry


class EmailReceiver:
    def __init__(self) -> None:
        self.__conn1 = self.__get_connection1()
        self.__conn2 = self.__get_connection2()
        self.__conn3 = self.__get_connection2()

    def payment_success_callback(self, ch, method, properties, body):
        pass

    def payment_failure_callback(self, ch, method, properties, body):
        pass

    def payment_proccessing(self):
        self.__conn1.basic_consume(
            queue='paymentSuccess', on_message_callback=self.payment_success_callback())
        self.__conn1.start_consuming()
        self.__conn2.basic_consume(
            queue='paymentFailure', on_message_callback=self.payment_failure_callback())
        self.__conn.start_consuming()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection1(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672))
        channel1 = connection.channel()
        channel1.queue_declare(queue='paymentSuccess')  # Declare a queue

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection2(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672))
        channel2 = connection.channel()
        channel2.queue_declare(queue='paymentFailure')  # Declare a queue
