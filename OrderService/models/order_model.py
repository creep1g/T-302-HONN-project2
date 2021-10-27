from pydantic import BaseModel


class OrderModel(BaseModel):
    productId: int
    merchantId: int
    buyerId: int
    creditCard: dict
    discount: float
