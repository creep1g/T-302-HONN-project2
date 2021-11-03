from pydantic import BaseModel
from typing import Optional


class InventoryModel(BaseModel):
    merchantId: int
    productName: str
    price: float
    quantity: int
    reserved: Optional[int]
