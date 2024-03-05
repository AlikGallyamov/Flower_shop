import pytest
from selene import browser, be, have
import allure

class BasePage:
    def __init__(self):

        self.price = browser.element('[class*="current"]')
        self.catalog_menu = browser.element('[class*="desktop_nav"] [class*="Catalogue_burger_menu"]')

    def open_url(self):
        with allure.step("Открываем главную страницу"):
            browser.open('/')

    def add_product(self, card):
        with allure.step("Кликаем 'Показать все'"):
            browser.element("//*[span[text()='Показать все']]").click()
        with allure.step(f"Кликаем 'заказать' у товара {card.card_name}"):
            browser.element('[href*="51-roza-la-bel"] [class*="cartButton"]').click()
        with allure.step("Проверяем количество товаров в корзине"):
            browser.all('[class*="ProductsList_list"]>li').should(have.size(1))
        with allure.step(f"Проверяем цену товара в корзине"):
            self.price.should(have.text('{0:,}'.format(card.price).replace(',', ' ')))
        with allure.step("Проверяем название товара в корзине"):
            browser.element('[class*="ProductsListItem_top"]').should(have.exact_text(card.card_name))

    def delete_product(self):
        with allure.step("Удаляем товар из корзины"):
            browser.element('[data-testid*=delete-product]').click()
        with allure.step("В корзине нет товара"):
            browser.element('[class*=empty__title]').should(have.text('В корзине пусто'))

    def search_product(self, card):
        with allure.step("Пишем название товара в поле поиска"):
            browser.element('[class*="SearchBar_input"]').should(be.blank).type(card.card_name)
        with allure.step("Проверяем всплывающую подсказку с названием товара"):
            browser.element('[class*="Dropdown_item__name"]>span').should(have.attribute('aria-label', card.card_name))
        with allure.step("Нажимаем поиск"):
            browser.element('[class*="SearchBar_input"]').press_enter()
        with allure.step("Найдены товары"):
            browser.all('[class*="Products"]>article').should(have.size_greater_than(1))
        with allure.step("Название товара соответствует запросу"):
            browser.element('[class*="ProductCard_name"]').should(have.exact_text(card.card_name))
        with allure.step(f"Цена товара равна {card.price}"):
            self.price.should(have.text('{0:,}'.format(card.price).replace(',', ' ')))

    def open_login_window(self, login_window):
        with allure.step("Нажимаем 'Войти'"):
            browser.element('[class*="HeaderMid"] [data-testid*="open-login"]').click()
        with allure.step("Открылось окно входа"):
            browser.element('[class*="login-modal_title"]').should(have.text(login_window.title))
        with allure.step("Отображается поле для ввода телефона"):
            browser.element('[class*="login-modal"] [id="phone"]').should(be.blank)

    def buy_without_authorization(self, login_window):
        with allure.step("Нажимаем 'Оформить заказ'"):
            browser.element('[class*="button_text"]').click()
        with allure.step("Открылось окно входа"):
            browser.element('[class*="login-modal_title"]').should(have.text(login_window.title))

    def open_catalog(self, catalog):
        with allure.step("Нажимаем 'Каталог'"):
            self.catalog_menu.click()
        with allure.step("Открылось окно выбора каталога"):
            browser.element('[class*="Navigation_heading"]').should(have.text('Каталог'))
        with allure.step("Проверяем список каталога"):
            browser.all('[class*="firstLevelMenu"]>li').should(
                have.texts(catalog.category, catalog.collection, catalog.by_flower, catalog.by_price,
                           catalog.by_color, catalog.discount_bouqets, catalog.by_photo, catalog.all_catalog))

    def open_category_flowers(self):
        with allure.step("Нажимаем 'Каталог'"):
            self.catalog_menu.click()
        with allure.step("Открывем 'Категории'"):
            browser.element('[alt="Категории"]').hover()
        with allure.step("Проверяем количество категорий"):
            browser.all('[class*="Submenu_list"]>li').should(have.size(10))
        with allure.step("Кликаем 'Цветы'"):
            browser.element('[href*="catalog/cvety"]').click()
        with allure.step("Проверяем, что перешли в каталог"):
            browser.element('[class*="Catalog_heading"]').should(have.text('Каталог'))
        with allure.step("Проверяем, что выбран 1 фильтр"):
            browser.all('[class*="Catalog_selected"]>li').should(have.size(1))
        with allure.step("Отображается товар '25 оранжево-желтых тюльпанов М24'"):
            browser.element('[href*="27-oranzhevo-zheltyh-tyulpanov"] [class*="Card_name"]').should(have.exact_text('25 оранжево-желтых тюльпанов М24'))
