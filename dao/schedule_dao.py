from .db_connector import get_cursor


def create_schedule(service_id, day_of_week, open_time, close_time):
    with get_cursor() as cursor:
        query = """
            INSERT INTO Schedule (service_id, day_of_week, open_time, close_time)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (service_id, day_of_week, open_time, close_time))
        return cursor.lastrowid


def get_all_schedules():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Schedule")
        return cursor.fetchall()


def get_schedule_by_id(schedule_id):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM Schedule WHERE schedule_id = %s", (schedule_id,))
        return cursor.fetchone()


def update_schedule(schedule_id, service_id, day_of_week, open_time, close_time):
    with get_cursor() as cursor:
        query = """
            UPDATE Schedule
            SET service_id = %s,
                day_of_week = %s,
                open_time = %s,
                close_time = %s
            WHERE schedule_id = %s
        """
        cursor.execute(
            query,
            (service_id, day_of_week, open_time, close_time, schedule_id)
        )
        return cursor.rowcount > 0


def delete_schedule(schedule_id):
    with get_cursor() as cursor:
        cursor.execute(
            "DELETE FROM Schedule WHERE schedule_id = %s",
            (schedule_id,)
        )
        return cursor.rowcount > 0
