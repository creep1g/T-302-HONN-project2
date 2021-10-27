from dbConnections.db_connection import DbConnection
from models.buyer_model import BuyerModel


class BuyerRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_buyer(self, buyer: BuyerModel) -> int:
        self.__conn.exectue(f'''
                            INSERT INTO BUYERS(name, ssn, email, phone)
                            VALUES(
                            '{buyer.name}',
                            '{buyer.ssn}',
                            '{buyer.email}',
                            '{buyer.phone}'
                            )
                            ''')
        self.__conn.commit()
        buyer_id = self.__conn.execute('''SELECT ID FROM BUYERS
                                            ORDER BY ID Desc
                                            LIMIT 1''')

        return buyer_id

    def get_buyer(self, buyer_id: int) -> BuyerModel:
        buyer_response = self.__conn.exectue(f'''SELECT * FROM BUYERS
                                                 WHERE ID = {buyer_id}''')
        buyer = BuyerModel(name=buyer_response[0][0],
                           ssn=buyer_response[0][1],
                           email=buyer_response[0][2],
                           phone=buyer_response[0][3])

        return buyer
