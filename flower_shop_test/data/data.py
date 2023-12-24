import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    price: int
    # old_price: int
    # discount_price: int

card = Card(card_name='9 роз Лемон Айс', price=2990)
