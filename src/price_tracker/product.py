from pydantic import BaseModel


class Price(BaseModel):
    value: float
    currency: str
    is_promo: bool = False


class Product(BaseModel):
    title: str
    price: Price
