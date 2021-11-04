import pika
import yagmail
from email_config import EmailConfig


class EmailHandler(EmailConfig):
    def __init__(self, email_config: EmailConfig) -> None:
        email = email_config.username
        pw = email_config.password
        self.yag = yagmail.SMTP(email, pw)

    def send_email(self, to, subject, contents):
        self.yag.send(to, subject, contents)

    def order_created_email(self):
        pass

    def payment_successful_email(self):
        pass

    def payment_failed_email(self):
        pass
