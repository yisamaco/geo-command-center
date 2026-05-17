from __future__ import annotations

import os

from sqlalchemy import create_engine


def make_engine():
    database_url = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
    return create_engine(database_url, future=True)
