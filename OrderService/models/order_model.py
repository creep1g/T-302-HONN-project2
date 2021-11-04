from pydantic import BaseModel
from typing import Optional


class OrderModelSend(BaseModel):
    orderId: Optional[int]
    productId: int
    merchantId: int
    buyerId: int
    creditCard: dict
    discount: float
    totalPrice: Optional[float]


class OrderModelGet(BaseModel):
    productId: int
    merchantId: int
    buyerId: int
    cardNumber: str
    totalPrice: float
