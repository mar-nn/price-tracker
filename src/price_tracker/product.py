from pydantic import BaseModel, field_validator


class Price(BaseModel):
    value: float
    currency: str
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


class Product(BaseModel):
    title: str
    price: Price
