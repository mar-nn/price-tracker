from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class Price(SQLModel):
    value: float
    currency: str
    is_promo: bool = False


class ProductBase(SQLModel):
    title: str
    url: str
    price_value: float
    currency: str
    is_promo: bool = False
    scraped_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProductRecord(ProductBase, table=True):
    product_iid: Optional[int] = Field(default=None, primary_key=True)


class Product(SQLModel):
    title: str
    price: Price

    def to_orm(self, url: str) -> ProductRecord:
        return ProductRecord(
            title=self.title,
            url=url,
            price_value=self.price.value,
            currency=self.price.currency,
            is_promo=self.price.is_promo,
        )
