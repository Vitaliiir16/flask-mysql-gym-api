from.db_connector import get_cursor
from decimal import Decimal

def create_service(service_name, price):
    with get_cursor() as cursor:
        query = "INSERT INTO Services (service_name, price) VALUES (%s, %s)"
        cursor.execute(query, (service_name, Decimal(price)))
        return cursor.lastrowid

def get_all_services():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Services")
        return cursor.fetchall()

def get_service_by_id(service_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Services WHERE service_id = %s", (service_id,))
        return cursor.fetchone()

def update_service(service_id, service_name, price):
    with get_cursor() as cursor:
        query = "UPDATE Services SET service_name = %s, price = %s WHERE service_id = %s"
        cursor.execute(query, (service_name, Decimal(price), service_id))
        return cursor.rowcount > 0

def delete_service(service_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Services WHERE service_id = %s", (service_id,))
        return cursor.rowcount > 0