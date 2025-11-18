from flask import Blueprint, request
from services import equipment_service
from utils.response_utils import success_response, error_response


equipment_bp = Blueprint('equipment', __name__)


@equipment_bp.route('/', methods=['POST'])
def create_equipment():
    """
    Create a new equipment item
    ---
    tags:
      - equipment
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with equipment data
        schema:
          type: object
          properties:
            equipment_name:
              type: string
              example: "Бігову доріжку"
          required:
            - equipment_name
    responses:
      201:
        description: Equipment created successfully
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        equipment_id = equipment_service.create_equipment(data)
        return success_response(
            {"equipment_id": equipment_id},
            "Equipment created successfully",
            201
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@equipment_bp.route('/', methods=['GET'])
def get_all_equipment():
    """
    Get all equipment
    ---
    tags:
      - equipment
    responses:
      200:
        description: List of equipment items
    """
    try:
        equipment = equipment_service.get_all_equipment()
        return success_response(equipment)
    except Exception as e:
        return error_response(str(e))


@equipment_bp.route('/<int:equipment_id>', methods=['GET'])
def get_equipment(equipment_id):
    """
    Get equipment by ID
    ---
    tags:
      - equipment
    parameters:
      - name: equipment_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the equipment item
    responses:
      200:
        description: Equipment data
      404:
        description: Equipment not found
    """
    try:
        equipment = equipment_service.get_equipment_by_id(equipment_id)
        return success_response(equipment)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@equipment_bp.route('/<int:equipment_id>', methods=['PUT', 'PATCH'])
def update_equipment(equipment_id):
    """
    Update equipment
    ---
    tags:
      - equipment
    parameters:
      - name: equipment_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the equipment item to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated equipment data
        schema:
          type: object
          properties:
            equipment_name:
              type: string
    responses:
      200:
        description: Equipment updated successfully
      400:
        description: Invalid input data
      404:
        description: Equipment not found
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        equipment_service.update_equipment(equipment_id, data)
        return success_response(message="Equipment updated successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e), status_code=400)


@equipment_bp.route('/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """
    Delete equipment
    ---
    tags:
      - equipment
    parameters:
      - name: equipment_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the equipment item to delete
    responses:
      200:
        description: Equipment deleted successfully
      404:
        description: Equipment not found
    """
    try:
        equipment_service.delete_equipment(equipment_id)
        return success_response(message="Equipment deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
