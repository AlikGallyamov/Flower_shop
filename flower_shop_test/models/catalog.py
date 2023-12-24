import dataclasses


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
                  by_color='По цвету', discount_bouqets='Акционные букеты', by_photo='Букет по фото',
                  all_catalog='Весь каталог')
