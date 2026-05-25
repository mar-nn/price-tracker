import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("price_tracker.db")


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            product_iid   INTEGER PRIMARY KEY AUTOINCREMENT,
            url           TEXT NOT NULL,
            title         TEXT NOT NULL,
            price_value   REAL NOT NULL,
            currency      TEXT NOT NULL,
            is_promo      INTEGER NOT NULL DEFAULT 0,
            scraped_at    TEXT NOT NULL
        )
    """)
    conn.commit()


def insert_price(conn: sqlite3.Connection, url: str, product) -> None:
    conn.execute(
        """
        INSERT INTO prices (url, title, price_value, currency, is_promo, scraped_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            url,
            product.title,
            product.price.value,
            product.price.currency,
            int(product.price.is_promo),
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
