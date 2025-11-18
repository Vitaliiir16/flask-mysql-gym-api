from flask import Blueprint, request
from services import service_service
from utils.response_utils import success_response, error_response


service_bp = Blueprint('services', __name__)


@service_bp.route('/', methods=['POST'])
def create_service():
    """
    Create a new service
    ---
    tags:
      - services
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with service data
        schema:
          type: object
          properties:
            service_name:
              type: string
              example: "Personal Training"
            price:
              type: number
              format: float
              example: 500.0
          required:
            - service_name
    responses:
      201:
        description: Service created successfully
      400:
        description: Invalid input data
    """
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
    """
    Get all services
    ---
    tags:
      - services
    responses:
      200:
        description: List of services
    """
    try:
        services = service_service.get_all_services()
        return success_response(services)
    except Exception as e:
        return error_response(str(e))


@service_bp.route('/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Get service by ID
    ---
    tags:
      - services
    parameters:
      - name: service_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the service
    responses:
      200:
        description: Service data
      404:
        description: Service not found
    """
    try:
        service = service_service.get_service_by_id(service_id)
        return success_response(service)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@service_bp.route('/<int:service_id>', methods=['PUT', 'PATCH'])
def update_service(service_id):
    """
    Update service
    ---
    tags:
      - services
    parameters:
      - name: service_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the service to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated service data
        schema:
          type: object
          properties:
            service_name:
              type: string
            price:
              type: number
              format: float
    responses:
      200:
        description: Service updated successfully
      400:
        description: Invalid input data
      404:
        description: Service not found
    """
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
    """
    Delete service
    ---
    tags:
      - services
    parameters:
      - name: service_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the service to delete
    responses:
      200:
        description: Service deleted successfully
      404:
        description: Service not found
    """
    try:
        service_service.delete_service(service_id)
        return success_response(message="Service deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
