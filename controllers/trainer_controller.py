from flask import Blueprint, request
from services import trainer_service
from utils.response_utils import success_response, error_response

trainer_bp = Blueprint('trainers', __name__)

@trainer_bp.route('/', methods=['POST'])
def create_trainer():
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
    try:
        trainers = trainer_service.get_all_trainers()
        return success_response(trainers)
    except Exception as e:
        return error_response(str(e))

@trainer_bp.route('/<int:trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    try:
        trainer = trainer_service.get_trainer_by_id(trainer_id)
        return success_response(trainer)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))

@trainer_bp.route('/<int:trainer_id>', methods=['PUT', 'PATCH'])
def update_trainer(trainer_id):
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
    try:
        trainer_service.delete_trainer(trainer_id)
        return success_response(message="Trainer deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
