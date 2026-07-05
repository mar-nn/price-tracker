import pytest
from pydantic import ValidationError

from price_tracker.models import Price, Product


def test_product_valid():
    product = Product(
        title="Elephant Videogame", price=Price(value=59.99, currency="EUR")
    )

    assert product.title == "Elephant Videogame"
    assert product.price.value == 59.99
    assert product.price.currency == "EUR"
    assert product.price.is_promo is False


def test_product_valid_promo():
    product = Product(
        title="Elephant Videogame",
        price=Price(value=49.99, currency="EUR", is_promo=True),
    )

    assert product.price.is_promo is True


def test_product_invalid_price():
    with pytest.raises(ValidationError):
        Product(title="Elephant Videogame", price="59.99 €")  # type: ignore


def test_price_valid_currency():
    price = Price(value=59.99, currency="EUR")
    assert price.currency == "EUR"


def test_price_currency_normalized_to_uppercase():
    price = Price(value=59.99, currency="eur")
    assert price.currency == "EUR"


def test_price_invalid_currency():
    with pytest.raises(ValidationError):
        Price(value=59.99, currency="FOO")


def test_price_invalid_currency_not_a_code():
    with pytest.raises(ValidationError):
        Price(value=59.99, currency="€")
