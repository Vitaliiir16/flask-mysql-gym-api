from dao import procedure_dao
import mysql.connector

VALID_COLUMNS = {
    'Trainers': ['name', 'surname', 'phone_number'],
    'Services': ['service_name', 'price'],
    'Clients': ['name', 'surname', 'phone_number', 'trainer_id'],
    'Workout_Programs': ['program_name', 'trainer_id'],
    'Trainer_Schedule': ['trainer_id', 'day_of_week'],
    'Equipment': ['equipment_name'],
    'Exercises': ['exercise_name', 'workout_program_id'],
    'Exercise_Equipment': ['exercise_id', 'equipment_id'],
    'Schedule': ['service_id', 'day_of_week', 'open_time', 'close_time'],
    'Memberships': ['client_id', 'membership_type', 'start_date', 'end_date']
}

VALID_TABLES = list(VALID_COLUMNS.keys())

VALID_STATS_OPERATIONS = ['COUNT', 'SUM', 'AVG', 'MIN', 'MAX', 'STDDEV', 'VAR']


def execute_insert_into_table(data):
    table = data['table_name']
    column = data['column_name']
    value = data['value']
    
    if table not in VALID_TABLES:
        raise ValueError(f"Invalid table name: {table}")
    if column not in VALID_COLUMNS.get(table,):
        raise ValueError(f"Invalid column name '{column}' for table '{table}'")
        
    procedure_dao.call_insert_into_table(table, column, value)

def execute_insert_equipment(data):
    procedure_dao.call_insert_equipment(data['equipment_name'])

def execute_add_exercise_equipment(data):
    try:
        procedure_dao.call_add_exercise_equipment(data['exercise_name'], data['equipment_name'])
    except mysql.connector.Error as err:
        if err.sqlstate == '45000':
            raise ValueError(err.msg)
        raise

def execute_insert_multiple_equipment():
    procedure_dao.call_insert_multiple_equipment()

def execute_get_column_stats(data):
    table = data['table_name']
    column = data['column_name']
    op = data['operation'].upper()

    if table not in VALID_TABLES:
        raise ValueError(f"Invalid table name: {table}")
    if op not in VALID_STATS_OPERATIONS:
        raise ValueError(f"Invalid operation: {op}. Must be one of {VALID_STATS_OPERATIONS}")
    
    if column not in VALID_COLUMNS.get(table,):
        if op == 'COUNT' and column == '*':
             pass
        else:
            raise ValueError(f"Invalid column name '{column}' for table '{table}'")
            
    result = procedure_dao.call_get_column_stats(table, column, op)
    
    try:
        return float(result)
    except (ValueError, TypeError):
        return result

def execute_split_table_randomly(data):
    table = data['table_name']
    if table not in VALID_TABLES:
        raise ValueError(f"Invalid table name: {table}")
    
    procedure_dao.call_split_table_randomly(table)