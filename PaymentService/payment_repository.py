from dbConnections.db_connection import DbConnection
from models.payment_model import PaymentModel


class PaymentRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_payment(self, payment: PaymentModel) -> int:
        self.__conn.execute(f'''
                            INSERT INTO payments(order_id, result)
                            VALUES(
                            {payment.orderId},
                            {payment.success}
                            )
                            ''')
        self.__conn.commit()

        payment_id = self.__conn.execute('''SELECT ID FROM payments
                                            ORDER BY ID Desc
                                            LIMIT 1''')

        return payment_id[0][0]
