from dao import workout_program_dao, trainer_dao

def _validate_foreign_keys(data):
    if 'trainer_id' in data and data['trainer_id'] is not None:
        if not trainer_dao.get_trainer_by_id(data['trainer_id']):
            raise ValueError(f"Invalid trainer_id: Trainer with id {data['trainer_id']} does not exist.")

def create_workout_program(data):
    _validate_foreign_keys(data)
    trainer_id = data.get('trainer_id')
    return workout_program_dao.create_workout_program(data['program_name'], trainer_id)

def get_all_workout_programs():
    return workout_program_dao.get_all_workout_programs()

def get_workout_program_by_id(workout_program_id):
    program = workout_program_dao.get_workout_program_by_id(workout_program_id)
    if not program:
        raise ValueError("Workout program not found")
    return program

def update_workout_program(workout_program_id, data):
    if not workout_program_dao.get_workout_program_by_id(workout_program_id):
        raise ValueError("Workout program not found")
    _validate_foreign_keys(data)
    trainer_id = data.get('trainer_id')
    return workout_program_dao.update_workout_program(workout_program_id, data['program_name'], trainer_id)

def delete_workout_program(workout_program_id):
    if not workout_program_dao.get_workout_program_by_id(workout_program_id):
        raise ValueError("Workout program not found")
    return workout_program_dao.delete_workout_program(workout_program_id)