from flask import Blueprint, request
from services import workout_program_service
from utils.response_utils import success_response, error_response

workout_program_bp = Blueprint('workout_programs', __name__)

@workout_program_bp.route('/', methods=['POST'])
def create_workout_program():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        program_id = workout_program_service.create_workout_program(data)
        return success_response({"workout_program_id": program_id}, "Workout program created", 201)
    except ValueError as e:
        # логіка з ValueError збережена як у тебе
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)

@workout_program_bp.route('/', methods=['GET'])
def get_all_workout_programs():
    try:
        programs = workout_program_service.get_all_workout_programs()
        return success_response(programs)
    except Exception as e:
        return error_response(str(e))

@workout_program_bp.route('/<int:program_id>', methods=['GET'])
def get_workout_program(program_id):
    try:
        program = workout_program_service.get_workout_program_by_id(program_id)
        return success_response(program)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))

@workout_program_bp.route('/<int:program_id>', methods=['PUT', 'PATCH'])
def update_workout_program(program_id):
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        workout_program_service.update_workout_program(program_id, data)
        return success_response(message="Workout program updated")
    except ValueError as e:
        return error_response(str(e), status_code=404 if "not found" in str(e) else 400)
    except Exception as e:
        return error_response(str(e), status_code=400)

@workout_program_bp.route('/<int:program_id>', methods=['DELETE'])
def delete_workout_program(program_id):
    try:
        workout_program_service.delete_workout_program(program_id)
        return success_response(message="Workout program deleted")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
