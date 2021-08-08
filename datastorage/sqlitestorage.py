import sqlite3
from typing import cast


def write_data(user_id: int, city: str):
    with sqlite3.connect('data/data.db') as conn:
        cursor = conn.cursor()
        query = "INSERT INTO user_city (user_id, user_city) VALUES (?, ?)"
        cursor.execute(query, (user_id, city))


def get_city(user_id) -> str:
    with sqlite3.connect('data/data.db') as conn:
        cursor = conn.cursor()
        query = "SELECT user_city.user_city FROM user_city WHERE user_id = ?"
        return cast(str, cursor.execute(query, (user_id,)).fetchone())

