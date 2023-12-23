import pytest
from selene import browser, be, have


class BasePage:
    def __init__(self):
        self.price = browser.element('[class*="current"]')

    def open_url(self):
        browser.open('/')

    def add_product(self, card):
        browser.element('[href*="na-1-sentyabrya"]').click()
        browser.element('[class*="Rubric_title"]').should(have.text('Хит продаж'))
        browser.element('[href*="9-roz-lemon-ajs"] [class*="cartButton"]').click()
        browser.all('[class*="ProductsList_list"]>li').should(have.size(1))
        self.price.should(have.exact_text(card.price))
        browser.element('[class*="ProductsListItem_top"]').should(have.exact_text(card.card_name))

    def delete_product(self, card):
        self.add_product(card)
        browser.element('[data-testid*=delete-product]').click()
        browser.element('[class*=empty__title]').should(have.text('В корзине пусто'))

    def search_product(self, card):
        browser.element('[class*="SearchBar_input"]').should(be.blank).type(card.card_name)
        browser.element('[class*="Dropdown_item__name"]>span').should(have.attribute('aria-label', card.card_name))
        browser.element('[class*="SearchBar_input"]').press_enter()
        browser.all('[class*="Products"]>article').should(have.size(1))
        browser.element('[class*="ProductCard_name"]').should(have.exact_text(card.card_name))
        self.price.should(have.exact_text(card.price))
