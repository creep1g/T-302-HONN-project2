import pika
import yagmail
from email_config import EmailConfig


class EmailHandler:
    def __init__(self, email_config: EmailConfig):
        email = email_config.username
        pw = email_config.password
        self.yag = yagmail.SMTP(email, pw)

    def send_email(self, to, subject, contents):
        self.yag.send(to, subject, contents)

    def order_created_email(self, merchant_email, buyer_email, orderId, productName, totalPrice):
        to = [merchant_email, buyer_email]
        subject = "Order has been created"
        contents = [str(orderId), productName, str(totalPrice)]
        self.send_email(to, subject, contents)

    def payment_successful_email(self, merchant_email, buyer_email, orderId):
        to = [merchant_email, buyer_email]
        subject = "Order has been purchased"
        contents = f'''Order {orderId} has been successfully purchased'''
        self.send_email(to, subject, contents)

    def payment_failed_email(self, merchant_email, buyer_email, orderId):
        to = [merchant_email, buyer_email]
        subject = "Order has been purchased"
        contents = f'''Order {orderId} purchase has failed'''
        self.send_email(to, subject, contents)
