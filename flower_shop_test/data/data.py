import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    price: int
    # old_price: int
    # discount_price: int

card = Card(card_name='51 роза Ла Бель', price=4990)


@dataclasses.dataclass
class LoginWindow:
    title: str
    number: str


login_window = LoginWindow(title='Введите телефон, чтобы войти', number='1231231231')

@dataclasses.dataclass
class Catalog:
    category: str
    collection: str
    by_flower: str
    by_price: str
    by_color: str
    discount_bouqets: str
    by_photo: str
    all_catalog: str


catalog = Catalog(category='Категории', collection='Подборки букетов', by_flower='По цветку', by_price='По цене',
                  by_color='По цвету', discount_bouqets='Букет по акции', by_photo='Букет по фото',
                  all_catalog='Весь каталог')

