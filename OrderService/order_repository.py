from dbConnections.db_connection import DbConnection
from models.order_model import OrderModelSend, OrderModelGet


class OrderRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_order(self, order: OrderModelSend) -> int:
        '''Inserts an order into order database '''
        originalNumber = order.creditCard["cardNumber"]
        cardNumber = "*" * (len(originalNumber)-4) + originalNumber[-4::]

        self.__conn.execute(f'''
                INSERT INTO public.ORDER(product_id, merchant_id, buyer_id,
                            card_number, discount, totalPrice)
                            VALUES(
                            {order.productId},
                            {order.merchantId},
                            {order.buyerId},
                            '{cardNumber}',
                            {order.discount},
                            {order.totalPrice}
                            )
                            ''')
        self.__conn.commit()
        order_id = self.__conn.execute('''SELECT ID FROM public.ORDER
                                            ORDER BY ID Desc
                                            LIMIT 1''')

        return order_id

    def get_order(self, order_id: int) -> OrderModelGet:
        '''Fetch order from our database'''
        order = self.__conn.execute(f'''SELECT * FROM public.ORDER
                                        WHERE ID = {order_id}''')

        if len(order) > 0:
            order = OrderModelGet(productId=order[0][1],
                                  merchantId=order[0][2],
                                  buyerId=order[0][3],
                                  cardNumber=order[0][4],
                                  totalPrice=order[0][6])
        else:
            order = None

        return order
