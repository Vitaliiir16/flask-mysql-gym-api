from dao import equipment_dao

def create_equipment(data):
    return equipment_dao.create_equipment(data['equipment_name'])

def get_all_equipment():
    return equipment_dao.get_all_equipment()

def get_equipment_by_id(equipment_id):
    equipment = equipment_dao.get_equipment_by_id(equipment_id)
    if not equipment:
        raise ValueError("Equipment not found")
    return equipment

def update_equipment(equipment_id, data):
    if not equipment_dao.get_equipment_by_id(equipment_id):
        raise ValueError("Equipment not found")
    return equipment_dao.update_equipment(equipment_id, data['equipment_name'])

def delete_equipment(equipment_id):
    if not equipment_dao.get_equipment_by_id(equipment_id):
        raise ValueError("Equipment not found")
    return equipment_dao.delete_equipment(equipment_id)