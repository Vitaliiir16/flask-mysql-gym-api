from.db_connector import get_cursor

def link_exercise_to_equipment(exercise_id, equipment_id):
    with get_cursor() as cursor:
        query = "INSERT INTO Exercise_Equipment (exercise_id, equipment_id) VALUES (%s, %s)"
        cursor.execute(query, (exercise_id, equipment_id))
        return cursor.rowcount > 0

def unlink_exercise_from_equipment(exercise_id, equipment_id):
    with get_cursor() as cursor:
        query = "DELETE FROM Exercise_Equipment WHERE exercise_id = %s AND equipment_id = %s"
        cursor.execute(query, (exercise_id, equipment_id))
        return cursor.rowcount > 0

def get_equipment_for_exercise(exercise_id):
    with get_cursor() as cursor:
        query = """
            SELECT e.* FROM Equipment e
            JOIN Exercise_Equipment ee ON e.equipment_id = ee.equipment_id
            WHERE ee.exercise_id = %s
        """
        cursor.execute(query, (exercise_id,))
        return cursor.fetchall()

def get_exercises_for_equipment(equipment_id):
    with get_cursor() as cursor:
        query = """
            SELECT ex.* FROM Exercises ex
            JOIN Exercise_Equipment ee ON ex.exercise_id = ee.exercise_id
            WHERE ee.equipment_id = %s
        """
        cursor.execute(query, (equipment_id,))
        return cursor.fetchall()