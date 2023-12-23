import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    price: str
    # old_price: int
    # discount_price: int

card = Card(card_name='9 роз Лемон Айс', price='2 990 ₽')
