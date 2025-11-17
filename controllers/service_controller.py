from flask import Blueprint, request
from services import service_service
from utils.response_utils import success_response, error_response

service_bp = Blueprint('services', __name__)


@service_bp.route('/', methods=['POST'])
def create_service():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        service_id = service_service.create_service(data)
        return success_response(
            {"service_id": service_id},
            "Service created successfully",
            201
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@service_bp.route('/', methods=['GET'])
def get_all_services():
    try:
        services = service_service.get_all_services()
        return success_response(services)
    except Exception as e:
        return error_response(str(e))


@service_bp.route('/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = service_service.get_service_by_id(service_id)
        return success_response(service)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@service_bp.route('/<int:service_id>', methods=['PUT', 'PATCH'])
def update_service(service_id):
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        service_service.update_service(service_id, data)
        return success_response(message="Service updated successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e), status_code=400)


@service_bp.route('/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service_service.delete_service(service_id)
        return success_response(message="Service deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
