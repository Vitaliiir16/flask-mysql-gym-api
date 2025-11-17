from.db_connector import get_cursor

def create_workout_program(program_name, trainer_id):
    with get_cursor() as cursor:
        query = "INSERT INTO Workout_Programs (program_name, trainer_id) VALUES (%s, %s)"
        cursor.execute(query, (program_name, trainer_id))
        return cursor.lastrowid

def get_all_workout_programs():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Workout_Programs")
        return cursor.fetchall()

def get_workout_program_by_id(workout_program_id):
    with get_cursor() as cursor:
        query = "SELECT * FROM Workout_Programs WHERE workout_program_id = %s"
        cursor.execute(query, (workout_program_id,))
        return cursor.fetchone()

def update_workout_program(workout_program_id, program_name, trainer_id):
    with get_cursor() as cursor:
        query = "UPDATE Workout_Programs SET program_name = %s, trainer_id = %s WHERE workout_program_id = %s"
        cursor.execute(query, (program_name, trainer_id, workout_program_id))
        return cursor.rowcount > 0

def delete_workout_program(workout_program_id):
    with get_cursor() as cursor:
        query = "DELETE FROM Workout_Programs WHERE workout_program_id = %s"
        cursor.execute(query, (workout_program_id,))
        return cursor.rowcount > 0