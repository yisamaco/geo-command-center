from __future__ import annotations

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def make_engine():
    database_url = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
    return create_engine(database_url, future=True)


def run_sql_file(path: str) -> None:
    engine = make_engine()
    sql = open(path, "r", encoding="utf-8").read()
    with engine.begin() as conn:
        conn.exec_driver_sql(sql)


def fetch_all(sql: str):
    engine = make_engine()
    with Session(engine) as session:
        return session.execute(sql).all()
