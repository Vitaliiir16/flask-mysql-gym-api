from dao import client_dao, trainer_dao

def _validate_foreign_keys(data):
    if 'trainer_id' in data and data['trainer_id'] is not None:
        if not trainer_dao.get_trainer_by_id(data['trainer_id']):
            raise ValueError(f"Invalid trainer_id: Trainer with id {data['trainer_id']} does not exist.")

def create_client(data):
    _validate_foreign_keys(data)
    trainer_id = data.get('trainer_id')
    return client_dao.create_client(data['name'], data['surname'], data['phone_number'], trainer_id)

def get_all_clients():
    return client_dao.get_all_clients()

def get_client_by_id(client_id):
    client = client_dao.get_client_by_id(client_id)
    if not client:
        raise ValueError("Client not found")
    return client

def update_client(client_id, data):
    if not client_dao.get_client_by_id(client_id):
        raise ValueError("Client not found")
    _validate_foreign_keys(data)
    trainer_id = data.get('trainer_id')
    return client_dao.update_client(client_id, data['name'], data['surname'], data['phone_number'], trainer_id)

def delete_client(client_id):
    if not client_dao.get_client_by_id(client_id):
        raise ValueError("Client not found")
    return client_dao.delete_client(client_id)