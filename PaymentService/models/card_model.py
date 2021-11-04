from pydantic import BaseModel


class CardModel(BaseModel):
    cardNumber: str
    expirationMonth: int
    expirationYear: int
    cvc: int
