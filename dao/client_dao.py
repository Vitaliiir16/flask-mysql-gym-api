from.db_connector import get_cursor

def create_client(name, surname, phone_number, trainer_id):
    with get_cursor() as cursor:
        query = "INSERT INTO Clients (name, surname, phone_number, trainer_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, surname, phone_number, trainer_id))
        return cursor.lastrowid

def get_all_clients():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Clients")
        return cursor.fetchall()

def get_client_by_id(client_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Clients WHERE client_id = %s", (client_id,))
        return cursor.fetchone()

def update_client(client_id, name, surname, phone_number, trainer_id):
    with get_cursor() as cursor:
        query = "UPDATE Clients SET name = %s, surname = %s, phone_number = %s, trainer_id = %s WHERE client_id = %s"
        cursor.execute(query, (name, surname, phone_number, trainer_id, client_id))
        return cursor.rowcount > 0

def delete_client(client_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Clients WHERE client_id = %s", (client_id,))
        return cursor.rowcount > 0