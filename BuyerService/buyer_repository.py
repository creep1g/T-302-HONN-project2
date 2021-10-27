from dbConnections.db_connection import DbConnection
from models.buyer_model import BuyerModel
from typing import Optional


class BuyerRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_buyer(self, buyer: BuyerModel) -> int:
        exists = self.get_buyer(ssn=buyer.ssn)
        if exists is None:
            self.__conn.execute(f'''
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
            print(buyer_id)
        else:
            buyer_id = self.__conn.execute(f'''SELECT ID FROM BUYERS
                                           WHERE SSN = '{buyer.ssn}' ''')

        return buyer_id[0][0]

    def get_buyer(self, buyer_id: Optional[int] = None,
                  ssn: Optional[str] = None) -> BuyerModel:

        if ssn is not None:
            buyer_response = self.__conn.execute(f'''SELECT * FROM BUYERS
                                                 WHERE ssn = '{ssn}' ''')
        elif buyer_id is not None:
            buyer_response = self.__conn.execute(f'''SELECT * FROM BUYERS
                                                 WHERE ID = {buyer_id}''')
        else:
            buyer_response = []

        if len(buyer_response) > 0:
            buyer = BuyerModel(name=buyer_response[0][1],
                               ssn=buyer_response[0][2],
                               email=buyer_response[0][3],
                               phone=buyer_response[0][4])
        else:
            buyer = None

        return buyer
