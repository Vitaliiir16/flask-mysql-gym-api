from dao import exercise_dao, workout_program_dao

def _validate_foreign_keys(data):
    if 'workout_program_id' in data and data['workout_program_id'] is not None:
        if not workout_program_dao.get_workout_program_by_id(data['workout_program_id']):
            raise ValueError(f"Invalid workout_program_id: Program {data['workout_program_id']} does not exist.")

def create_exercise(data):
    _validate_foreign_keys(data)
    program_id = data.get('workout_program_id')
    return exercise_dao.create_exercise(data['exercise_name'], program_id)

def get_all_exercises():
    return exercise_dao.get_all_exercises()

def get_exercise_by_id(exercise_id):
    exercise = exercise_dao.get_exercise_by_id(exercise_id)
    if not exercise:
        raise ValueError("Exercise not found")
    return exercise

def update_exercise(exercise_id, data):
    if not exercise_dao.get_exercise_by_id(exercise_id):
        raise ValueError("Exercise not found")
    _validate_foreign_keys(data)
    program_id = data.get('workout_program_id')
    return exercise_dao.update_exercise(exercise_id, data['exercise_name'], program_id)

def delete_exercise(exercise_id):
    if not exercise_dao.get_exercise_by_id(exercise_id):
        raise ValueError("Exercise not found")
    return exercise_dao.delete_exercise(exercise_id)