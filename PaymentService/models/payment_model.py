from pydantic import BaseModel


class PaymentModel(BaseModel):
    orderId: int
    success: bool
