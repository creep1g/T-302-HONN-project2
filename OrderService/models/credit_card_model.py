from pydantic import BaseModel


class CreditCardModel(BaseModel):
    cardNumber: str
    expirationMonth: int
    expirationYear: int
    cvc: int
