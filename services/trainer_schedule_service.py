from dao import trainer_schedule_dao, trainer_dao

def _validate_foreign_keys(data):
    if 'trainer_id' in data and data['trainer_id'] is not None:
        if not trainer_dao.get_trainer_by_id(data['trainer_id']):
            raise ValueError(f"Invalid trainer_id: Trainer with id {data['trainer_id']} does not exist.")

def create_trainer_schedule(data):
    _validate_foreign_keys(data)
    return trainer_schedule_dao.create_trainer_schedule(data['trainer_id'], data['day_of_week'])

def get_all_trainer_schedules():
    return trainer_schedule_dao.get_all_trainer_schedules()

def get_trainer_schedule_by_id(schedule_id):
    schedule = trainer_schedule_dao.get_trainer_schedule_by_id(schedule_id)
    if not schedule:
        raise ValueError("Trainer schedule not found")
    return schedule

def update_trainer_schedule(schedule_id, data):
    if not trainer_schedule_dao.get_trainer_schedule_by_id(schedule_id):
        raise ValueError("Trainer schedule not found")
    _validate_foreign_keys(data)
    return trainer_schedule_dao.update_trainer_schedule(schedule_id, data['trainer_id'], data['day_of_week'])

def delete_trainer_schedule(schedule_id):
    if not trainer_schedule_dao.get_trainer_schedule_by_id(schedule_id):
        raise ValueError("Trainer schedule not found")
    return trainer_schedule_dao.delete_trainer_schedule(schedule_id)