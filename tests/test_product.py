import pytest
from pydantic import ValidationError

from price_tracker.product import Price, Product


def test_product_valid():
    product = Product(
        title="Elephant Videogame", price=Price(value=59.99, currency="€")
    )

    assert product.title == "Elephant Videogame"
    assert product.price.value == 59.99
    assert product.price.currency == "€"
    assert product.price.is_promo is False


def test_product_valid_promo():
    product = Product(
        title="Elephant Videogame",
        price=Price(value=49.99, currency="€", is_promo=True),
    )

    assert product.price.is_promo is True


def test_product_invalid_price():
    with pytest.raises(ValidationError):
        Product(
            title="Elephant Videogame",
            price=59.99,  # type: ignore
        )
