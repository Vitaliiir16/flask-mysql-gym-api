from dao import schedule_dao, service_dao
from datetime import time, timedelta, date

def _convert_times(schedule):
    if schedule:
        if 'open_time' in schedule and isinstance(schedule['open_time'], timedelta):
            schedule['open_time'] = str(schedule['open_time'])
        if 'close_time' in schedule and isinstance(schedule['close_time'], timedelta):
            schedule['close_time'] = str(schedule['close_time'])
    return schedule

def _validate_foreign_keys(data):
    if 'service_id' in data and data['service_id'] is not None:
        if not service_dao.get_service_by_id(data['service_id']):
            raise ValueError(f"Invalid service_id: Service {data['service_id']} does not exist.")

def create_schedule(data):
    _validate_foreign_keys(data)
    return schedule_dao.create_schedule(
        data['service_id'], data['day_of_week'], data['open_time'], data['close_time']
    )

def get_all_schedules():
    schedules = schedule_dao.get_all_schedules()
    return [_convert_times(s) for s in schedules]

def get_schedule_by_id(schedule_id):
    schedule = schedule_dao.get_schedule_by_id(schedule_id)
    if not schedule:
        raise ValueError("Schedule not found")
    return _convert_times(schedule)

def update_schedule(schedule_id, data):
    if not schedule_dao.get_schedule_by_id(schedule_id):
        raise ValueError("Schedule not found")
    _validate_foreign_keys(data)
    return schedule_dao.update_schedule(
        schedule_id, data['service_id'], data['day_of_week'], data['open_time'], data['close_time']
    )

def delete_schedule(schedule_id):
    if not schedule_dao.get_schedule_by_id(schedule_id):
        raise ValueError("Schedule not found")
    return schedule_dao.delete_schedule(schedule_id)