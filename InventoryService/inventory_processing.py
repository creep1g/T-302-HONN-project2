from dbConnections.db_connection import DbConnection
import pika
from retry import retry
import json


class InventoryProcessing:
    def __init__(self, db_connection: DbConnection) -> None:
        print("in InventoryProcessing")
        self.__conn = self.__get_connection()
        self.__dbConn = db_connection

    def payment_success_callback(self, ch, method, properties, body):
        print("in payment_success_callback")
        body = body.decode("utf-8")
        body = json.loads(body)
        product_id = (body["productId"])
        print("product_id: ", product_id)
        self.__dbConn.execute(
            f''' UPDATE inventory SET quantity = quantity - 1 WHERE id = '{product_id}' ''')
        self.__dbConn.execute(
            f''' UPDATE inventory SET reserved = '{0}' WHERE id = '{product_id}' ''')
        self.__dbConn.commit()
        # hættaaðtakafrátiltekna vöru og minnka fjöldi vara in stock

    def payment_failure_callback(self, ch, method, properties, body):
        print("in payment_failure_callback")
        body = body.decode("utf-8")
        body = json.loads(body)
        product_id = (body["productId"])
        self.__dbConn.execute(
            f''' UPDATE inventory SET reserved = '{0}' WHERE id = '{product_id}' ''')
        self.__dbConn.commit()

    def payment_proccessing(self):
        print("in payment_proccessing")
        self.__conn.basic_consume(
            queue='paymentSuccess',
            on_message_callback=self.payment_success_callback,
            auto_ack=True)
        self.__conn.start_consuming()
        self.__conn.basic_consume(
            queue='paymentFailure', on_message_callback=self.payment_failure_callback, auto_ack=True)
        self.__conn.start_consuming()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbit1', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='paymentSuccess')  # Declare a queue
        channel.queue_declare(queue='paymentFailure')  # Declare a queue
        return channel
