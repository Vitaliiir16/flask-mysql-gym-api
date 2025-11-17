from dao import service_dao
from decimal import Decimal

def _convert_decimals(service):
    if service and 'price' in service:
        service['price'] = float(service['price'])
    return service

def create_service(data):
    return service_dao.create_service(data['service_name'], data['price'])

def get_all_services():
    services = service_dao.get_all_services()
    return [_convert_decimals(s) for s in services]

def get_service_by_id(service_id):
    service = service_dao.get_service_by_id(service_id)
    if not service:
        raise ValueError("Service not found")
    return _convert_decimals(service)

def update_service(service_id, data):
    if not service_dao.get_service_by_id(service_id):
        raise ValueError("Service not found")
    return service_dao.update_service(service_id, data['service_name'], data['price'])

def delete_service(service_id):
    if not service_dao.get_service_by_id(service_id):
        raise ValueError("Service not found")
    return service_dao.delete_service(service_id)