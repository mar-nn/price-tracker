from pydantic import BaseModel


<<<<<<< 10-create-a-product-schema
class Price(BaseModel):
    value: float
    currency: str
    is_promo: bool = False


class Product(BaseModel):
    title: str
    price: Price
=======
class Product(BaseModel):
    title: str
    price: str
>>>>>>> master
