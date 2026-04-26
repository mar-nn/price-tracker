import pytest
from price_tracker.product import Product
from pydantic import ValidationError


def test_product_valid():
    product = Product(title="Elephant Videogame", price="59.99 €")

    assert product.title == "Elephant Videogame"
    assert product.price == "59.99 €"


def test_product_invalid_price():
    with pytest.raises(ValidationError):
        Product(
            title="Elephant Videogame",
            price=59.99,  # type: ignore
        )
