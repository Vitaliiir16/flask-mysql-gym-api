import mysql.connector.pooling
import os
from contextlib import contextmanager


db_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="api_pool",
    pool_size=10,
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)


@contextmanager
def get_cursor():
    conn = db_pool.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
        # якщо дійшли сюди без виключень, фіксуємо транзакцію
        conn.commit()
    except Exception:
        # у разі помилки відкочуємо
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
