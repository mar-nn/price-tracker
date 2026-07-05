import os

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from price_tracker.models import Product

DB_URL = os.getenv("DATABASE_URL", "sqlite:///price_tracker.db")


def get_engine() -> Engine:
    engine = create_engine(DB_URL)
    SQLModel.metadata.create_all(engine)
    return engine


def insert_price(engine: Engine, url: str, product: Product) -> None:
    record = product.to_record(url)
    with Session(engine) as session:
        session.add(record)
        session.commit()
