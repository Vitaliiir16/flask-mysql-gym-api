from flask import Blueprint, request
from services import trainer_service
from utils.response_utils import success_response, error_response


trainer_bp = Blueprint('trainers', __name__)


@trainer_bp.route('/', methods=['POST'])
def create_trainer():
    """
    Create a new trainer
    ---
    tags:
      - trainers
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with trainer data
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Vitalii"
            surname:
              type: string
              example: "Savchuk"
            phone_number:
              type: string
              example: "123-456-7890"
          required:
            - name
            - surname
    responses:
      201:
        description: Trainer created successfully
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        trainer_id = trainer_service.create_trainer(data)
        return success_response({"trainer_id": trainer_id}, "Trainer created successfully", 201)
    except Exception as e:
        return error_response(str(e), status_code=400)


@trainer_bp.route('/', methods=['GET'])
def get_all_trainers():
    """
    Get all trainers
    ---
    tags:
      - trainers
    responses:
      200:
        description: List of trainers
    """
    try:
        trainers = trainer_service.get_all_trainers()
        return success_response(trainers)
    except Exception as e:
        return error_response(str(e))


@trainer_bp.route('/<int:trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    """
    Get trainer by ID
    ---
    tags:
      - trainers
    parameters:
      - name: trainer_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer
    responses:
      200:
        description: Trainer data
      404:
        description: Trainer not found
    """
    try:
        trainer = trainer_service.get_trainer_by_id(trainer_id)
        return success_response(trainer)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@trainer_bp.route('/<int:trainer_id>', methods=['PUT', 'PATCH'])
def update_trainer(trainer_id):
    """
    Update trainer
    ---
    tags:
      - trainers
    parameters:
      - name: trainer_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated trainer data
        schema:
          type: object
          properties:
            name:
              type: string
            surname:
              type: string
            phone_number:
              type: string
    responses:
      200:
        description: Trainer updated successfully
      400:
        description: Invalid input data
      404:
        description: Trainer not found
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        trainer_service.update_trainer(trainer_id, data)
        return success_response(message="Trainer updated successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e), status_code=400)


@trainer_bp.route('/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id):
    """
    Delete trainer
    ---
    tags:
      - trainers
    parameters:
      - name: trainer_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer to delete
    responses:
      200:
        description: Trainer deleted successfully
      404:
        description: Trainer not found
    """
    try:
        trainer_service.delete_trainer(trainer_id)
        return success_response(message="Trainer deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
