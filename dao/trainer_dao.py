from.db_connector import get_cursor

def create_trainer(name, surname, phone_number):
    with get_cursor() as cursor:
        query = "INSERT INTO Trainers (name, surname, phone_number) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, surname, phone_number))
        return cursor.lastrowid

def get_all_trainers():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Trainers")
        return cursor.fetchall()

def get_trainer_by_id(trainer_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Trainers WHERE trainer_id = %s", (trainer_id,))
        return cursor.fetchone()

def update_trainer(trainer_id, name, surname, phone_number):
    with get_cursor() as cursor:
        query = "UPDATE Trainers SET name = %s, surname = %s, phone_number = %s WHERE trainer_id = %s"
        cursor.execute(query, (name, surname, phone_number, trainer_id))
        return cursor.rowcount > 0

def delete_trainer(trainer_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Trainers WHERE trainer_id = %s", (trainer_id,))
        return cursor.rowcount > 0