from dbConnections.db_connection import DbConnection
from models.order_model import OrderModel
from models.credit_card_model import CreditCardModel
import json

class OrderRepository:
    def __init__(self, db_connection: DbConnection):
        self.__conn = db_connection

    def create_order(self, order: OrderModel) -> int:
        '''Inserts an order into order database '''

        card = CreditCardModel(**order.creditCard) # Generate a CC model

        # Check to see if credit card is already on file.
        exists = self.__conn.execute(f'''
                                     SELECT ID FROM public.CreditCard
                                     WHERE cardnumber = '{card.cardNumber}'
                                     AND
                                     CVC = {card.cvc}
                                     ''')
       # If card does not exist log it
        if not exists:
            self.__conn.execute(f'''
                                INSERT INTO public.CreditCard(cardnumber, expirationMonth, expirationDay, cvc)
                                VALUES(
                                '{card.cardNumber}',
                                {card.expirationMonth},
                                {card.expirationYear},
                                {card.cvc}
                                )
                                ''')
            self.__conn.commit()
            # Get card id
            exists = self.__conn.execute(f'''
                                         SELECT ID FROM public.CreditCard
                                         ORDER BY ID Desc
                                         LIMIT 1
                                         ''')
        cardId = exists[0][0]

        self.__conn.execute(f'''
                INSERT INTO public.ORDER(product_id, merchant_id, buyer_id, card_id, discount)
                            VALUES(
                            {order.productId},
                            {order.merchantId},
                            {order.buyerId},
                            {cardId},
                            {order.discount}
                            )
                            ''')
        self.__conn.commit()
        order_id = self.__conn.execute('''SELECT ID FROM public.ORDER
                                            ORDER BY ID Desc
                                            LIMIT 1''')

        return order_id


    def get_order(self, order_id: int) -> OrderModel:
        '''Fetch order from our database'''
        order = self.__conn.execute(f'''SELECT * FROM public.ORDER
                                        WHERE ID = {order_id}''')

        card =  self.__conn.execute(f'''
                                    SELECT * FROM public.CreditCard
                                    WHERE ID = {order[0][3]}
                                    ''')

        card = CreditCardModel(cardNumber=card[0][1],
                               expirationMonth=card[0][2],
                               expirationYear=card[0][3],
                               cvc=card[0][4])

        if len(order) > 0:
            order = OrderModel(productId=order[0][0],
                            merchantId=order[0][1],
                            buyerId=order[0][2],
                            creditCard=card,
                            discount=order[0][4])
        else:
            order = None

        return order
