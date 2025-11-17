from.db_connector import get_cursor

def create_trainer_schedule(trainer_id, day_of_week):
    with get_cursor() as cursor:
        query = "INSERT INTO Trainer_Schedule (trainer_id, day_of_week) VALUES (%s, %s)"
        cursor.execute(query, (trainer_id, day_of_week))
        return cursor.lastrowid

def get_all_trainer_schedules():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Trainer_Schedule")
        return cursor.fetchall()

def get_trainer_schedule_by_id(schedule_id):
    with get_cursor() as cursor:
        query = "SELECT * FROM Trainer_Schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id,))
        return cursor.fetchone()

def update_trainer_schedule(schedule_id, trainer_id, day_of_week):
    with get_cursor() as cursor:
        query = "UPDATE Trainer_Schedule SET trainer_id = %s, day_of_week = %s WHERE schedule_id = %s"
        cursor.execute(query, (trainer_id, day_of_week, schedule_id))
        return cursor.rowcount > 0

def delete_trainer_schedule(schedule_id):
    with get_cursor() as cursor:
        query = "DELETE FROM Trainer_Schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id,))
        return cursor.rowcount > 0