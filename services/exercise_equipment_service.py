from dao import exercise_equipment_dao, exercise_dao, equipment_dao
import mysql.connector

def link_exercise_to_equipment(data):
    exercise_id = data['exercise_id']
    equipment_id = data['equipment_id']
    
    if not exercise_dao.get_exercise_by_id(exercise_id):
        raise ValueError("Exercise not found")
    if not equipment_dao.get_equipment_by_id(equipment_id):
        raise ValueError("Equipment not found")
    
    try:
        return exercise_equipment_dao.link_exercise_to_equipment(exercise_id, equipment_id)
    except mysql.connector.Error as err:
        if err.errno == 1062:
            raise ValueError("This link already exists")
        raise

def unlink_exercise_from_equipment(exercise_id, equipment_id):
    deleted = exercise_equipment_dao.unlink_exercise_from_equipment(exercise_id, equipment_id)
    if not deleted:
        raise ValueError("Link not found")
    return deleted

def get_equipment_for_exercise(exercise_id):
    if not exercise_dao.get_exercise_by_id(exercise_id):
        raise ValueError("Exercise not found")
    return exercise_equipment_dao.get_equipment_for_exercise(exercise_id)

def get_exercises_for_equipment(equipment_id):
    if not equipment_dao.get_equipment_by_id(equipment_id):
        raise ValueError("Equipment not found")
    return exercise_equipment_dao.get_exercises_for_equipment(equipment_id)