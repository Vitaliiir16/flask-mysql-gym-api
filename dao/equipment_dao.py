from.db_connector import get_cursor

def create_equipment(equipment_name):
    with get_cursor() as cursor:
        query = "INSERT INTO Equipment (equipment_name) VALUES (%s)"
        cursor.execute(query, (equipment_name,))
        return cursor.lastrowid

def get_all_equipment():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Equipment")
        return cursor.fetchall()

def get_equipment_by_id(equipment_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Equipment WHERE equipment_id = %s", (equipment_id,))
        return cursor.fetchone()

def update_equipment(equipment_id, equipment_name):
    with get_cursor() as cursor:
        query = "UPDATE Equipment SET equipment_name = %s WHERE equipment_id = %s"
        cursor.execute(query, (equipment_name, equipment_id))
        return cursor.rowcount > 0

def delete_equipment(equipment_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM Equipment WHERE equipment_id = %s", (equipment_id,))
        return cursor.rowcount > 0