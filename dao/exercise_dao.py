from.db_connector import get_cursor

def create_exercise(exercise_name, workout_program_id):
    with get_cursor() as cursor:
        query = "INSERT INTO Exercises (exercise_name, workout_program_id) VALUES (%s, %s)"
        cursor.execute(query, (exercise_name, workout_program_id))
        return cursor.lastrowid

def get_all_exercises():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Exercises")
        return cursor.fetchall()

def get_exercise_by_id(exercise_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Exercises WHERE exercise_id = %s", (exercise_id,))
        return cursor.fetchone()

def update_exercise(exercise_id, exercise_name, workout_program_id):
    with get_cursor() as cursor:
        query = "UPDATE Exercises SET exercise_name = %s, workout_program_id = %s WHERE exercise_id = %s"
        cursor.execute(query, (exercise_name, workout_program_id, exercise_id))
        return cursor.rowcount > 0

def delete_exercise(exercise_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Exercises WHERE exercise_id = %s", (exercise_id,))
        return cursor.rowcount > 0