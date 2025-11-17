from dao import trainer_dao

def create_trainer(data):
    return trainer_dao.create_trainer(data['name'], data['surname'], data['phone_number'])

def get_all_trainers():
    return trainer_dao.get_all_trainers()

def get_trainer_by_id(trainer_id):
    trainer = trainer_dao.get_trainer_by_id(trainer_id)
    if not trainer:
        raise ValueError("Trainer not found")
    return trainer

def update_trainer(trainer_id, data):
    if not trainer_dao.get_trainer_by_id(trainer_id):
        raise ValueError("Trainer not found")
    return trainer_dao.update_trainer(trainer_id, data['name'], data['surname'], data['phone_number'])

def delete_trainer(trainer_id):
    if not trainer_dao.get_trainer_by_id(trainer_id):
        raise ValueError("Trainer not found")
    return trainer_dao.delete_trainer(trainer_id)