from models.card_model import CardModel
from luhn import verify


class Validator:
    def validate(self, card: CardModel):
        '''Returns a boolean response validating if card is valid'''
        return self.__check_date(card) == self.__check_number(card)

    def __check_date(self, card: CardModel):
        '''Check if expiration month is within limits and that
        expiration year is 4 digits long'''
        if card.expirationMonth > 12 or card.expirationMonth < 1:
            return False
        if len(str(card.expirationYear)) != 4:
            return False
        else:
            return True

    def __check_number(self, card: CardModel):
        '''Using luhns algorithm verifies if card number is valid'''
        return verify(card.cardNumber)
