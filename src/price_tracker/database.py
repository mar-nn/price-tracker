import sqlite3
from datetime import datetime
from hashlib import sha256

from price_tracker.product import Product

DB_PATH = "prices.db"


def get_product_iid(url: str) -> str:
    return sha256(url.encode()).hexdigest()


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS prices (
                product_iid TEXT,
                title TEXT,
                price TEXT,
                timestamp TEXT
            )
            """
        )


def insert_price(
    url: str,
    product: Product,
) -> None:
    product_iid = get_product_iid(url)

    timestamp = datetime.utcnow().isoformat()

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO prices (
                product_iid,
                title,
                price,
                timestamp
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                product_iid,
                product.title,
                product.price,
                timestamp,
            ),
        )
