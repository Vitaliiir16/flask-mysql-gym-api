from flask import Blueprint, request
from services import exercise_service
from utils.response_utils import success_response, error_response

exercise_bp = Blueprint('exercises', __name__)


@exercise_bp.route('/', methods=['POST'])
def create_exercise():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        exercise_id = exercise_service.create_exercise(data)
        return success_response(
            {"exercise_id": exercise_id},
            "Exercise created successfully",
            201
        )
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@exercise_bp.route('/', methods=['GET'])
def get_all_exercises():
    try:
        exercises = exercise_service.get_all_exercises()
        return success_response(exercises)
    except Exception as e:
        return error_response(str(e))


@exercise_bp.route('/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    try:
        exercise = exercise_service.get_exercise_by_id(exercise_id)
        return success_response(exercise)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@exercise_bp.route('/<int:exercise_id>', methods=['PUT', 'PATCH'])
def update_exercise(exercise_id):
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        exercise_service.update_exercise(exercise_id, data)
        return success_response(message="Exercise updated successfully")
    except ValueError as e:
        return error_response(
            str(e),
            status_code=404 if "not found" in str(e) else 400
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@exercise_bp.route('/<int:exercise_id>', methods=['DELETE'])
def delete_exercise(exercise_id):
    try:
        exercise_service.delete_exercise(exercise_id)
        return success_response(message="Exercise deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
