import os

from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from price_tracker.models import Product

DB_URL = os.getenv("DATABASE_URL", "sqlite:///price_tracker.db")


def get_engine() -> Engine:
    return create_engine(DB_URL)


def insert_price(engine: Engine, url: str, product: Product) -> None:
    record = product.to_orm(url)
    with Session(engine) as session:
        session.add(record)
        session.commit()
