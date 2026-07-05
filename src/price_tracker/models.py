from datetime import datetime, timezone
from typing import Optional

from pydantic import field_validator
from sqlmodel import Field, SQLModel


class Price(SQLModel):
    value: float = Field(..., description="Item's value")
    currency: str = Field(
        ..., description="Must be a 3-letter ISO 4217 code.", min_length=3, max_length=3
    )
    is_promo: bool = False

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, v: str) -> str:
        VALID_CURRENCIES = {"EUR", "USD", "GBP"}
        v = v.upper()
        if v not in VALID_CURRENCIES:
            raise ValueError(
                f"Invalid currency: {v!r}. Must be a 3-letter ISO 4217 code."
            )
        return v


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

    def to_record(self, url: str) -> ProductRecord:
        return ProductRecord(
            title=self.title,
            url=url,
            price_value=self.price.value,
            currency=self.price.currency,
            is_promo=self.price.is_promo,
        )
