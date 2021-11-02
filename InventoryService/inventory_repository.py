from dbConnections.db_connection import DbConnection
from models.inventory_model import InventoryModel
from typing import Optional


class InventoryRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_product(self, product: InventoryModel) -> int:
        print("in here")
        exists = self.get_product(productName=product.productName)
        if exists is None:
            self.__conn.execute(f'''
                            INSERT INTO inventory(
                                merchantId,
                                productName,
                                price,
                                quantity,
                                reserved)
                                VALUES(
                                    '{product.merchantId}',
                                    '{product.productName}',
                                    '{product.price}',
                                    '{product.quantity}',
                                    '{0}')
                                    ''')
            self.__conn.commit()
            product_id = self.__conn.execute('''SELECT ID FROM inventory
                                            ORDER BY ID Desc
                                            LIMIT 1''')
        else:
            product_id = self.__conn.execute(f'''SELECT ID FROM inventory
                                           WHERE productName = '{product.productName}' ''')
        print("product: ", product)
        return product_id[0][0]

    def get_product(self, product_id: Optional[int] = None, productName: Optional[str] = None) -> InventoryModel:
        if productName is not None:
            response = self.__conn.execute(f'''SELECT * FROM inventory
                                                 WHERE productName = '{productName}' ''')
        elif product_id is not None:
            response = self.__conn.execute(f'''SELECT * FROM inventory
                                                 WHERE ID = {product_id}''')
        else:
            response = []
        if len(response) > 0:
            product = InventoryModel(merchantId=response[0][1],
                                     productName=response[0][2],
                                     price=response[0][3],
                                     quantity=response[0][4],
                                     reserved=response[0][5])
        else:
            product = None
        return product
