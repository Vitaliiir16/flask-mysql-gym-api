from.db_connector import get_cursor
import mysql.connector

def call_insert_into_table(table_name, column_name, value):
    with get_cursor() as cursor:
        cursor.callproc('insert_into_table', [table_name, column_name, value])

def call_insert_equipment(equipment_name):
    with get_cursor() as cursor:
        cursor.callproc('insert_equipment', [equipment_name])

def call_add_exercise_equipment(exercise_name, equipment_name):
    try:
        with get_cursor() as cursor:
            cursor.callproc('add_exercise_equipment', [exercise_name, equipment_name])
    except mysql.connector.Error as err:
        if err.sqlstate == '45000':
            raise ValueError(err.msg)
        raise

def call_insert_multiple_equipment():
    with get_cursor() as cursor:
        cursor.callproc('insert_multiple_equipment')

def call_get_column_stats(table_name, column_name, operation):
    with get_cursor() as cursor:
        cursor.callproc('get_column_stats', [table_name, column_name, operation])
        for result in cursor.stored_results():
            res = result.fetchone()
            return res['result'] if res else None

def call_split_table_randomly(table_name):
    with get_cursor() as cursor:
        cursor.callproc('split_table_randomly', [table_name])