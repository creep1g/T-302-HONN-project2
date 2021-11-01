from dbConnections.db_connection import DbConnection
from models.merchant_model import MerchantModel
from typing import Optional


class MerchantRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_merchant(self, merchant: MerchantModel) -> int:
        exists = self.get_merchant(ssn=merchant.ssn)
        if exists:
            return exists.ssn

        self.__conn.execute(f'''
                            INSERT INTO MERCHANTS(name,
                            ssn,
                            email,
                            phone,
                            discount)
                            VALUES(
                            '{merchant.name}',
                            '{merchant.ssn}',
                            '{merchant.email}',
                            '{merchant.phoneNumber}',
                            {merchant.allowsDiscount}
                            )
                            ''')
        self.__conn.commit()
        merchant_id = self.__conn.execute('''SELECT ID FROM MERCHANTS
                                            ORDER BY ID Desc
                                            LIMIT 1''')

        return merchant_id[0][0]

    def get_merchant(self, merchant_id: Optional[int] = None,
                     ssn: Optional[str] = None) -> MerchantModel:

        if ssn is not None:
            response = self.__conn.execute(f'''SELECT * FROM MERCHANTS
                                                 WHERE ssn = '{ssn}' ''')
        elif merchant_id is not None:
            response = self.__conn.execute(f'''SELECT * FROM MERCHANTS
                                                 WHERE ID = {merchant_id}''')
        else:
            response = []

        if len(response) > 0:
            merchant = MerchantModel(name=response[0][1],
                                     ssn=response[0][2],
                                     email=response[0][3],
                                     phoneNumber=response[0][4],
                                     allowsDiscount=response[0][5])
        else:
            merchant = None

        return merchant
