from flask import Blueprint, request
from services import exercise_service
from utils.response_utils import success_response, error_response


exercise_bp = Blueprint('exercises', __name__)


@exercise_bp.route('/', methods=['POST'])
def create_exercise():
    """
    Create a new exercise
    ---
    tags:
      - exercises
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with exercise data
        schema:
          type: object
          properties:
            exercise_name:
              type: string
              example: "Біг"
            workout_program_id:
              type: integer
              example: 1
          required:
            - exercise_name
    responses:
      201:
        description: Exercise created successfully
      400:
        description: Invalid input data
    """
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
    """
    Get all exercises
    ---
    tags:
      - exercises
    responses:
      200:
        description: List of exercises
    """
    try:
        exercises = exercise_service.get_all_exercises()
        return success_response(exercises)
    except Exception as e:
        return error_response(str(e))


@exercise_bp.route('/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    """
    Get exercise by ID
    ---
    tags:
      - exercises
    parameters:
      - name: exercise_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the exercise
    responses:
      200:
        description: Exercise data
      404:
        description: Exercise not found
    """
    try:
        exercise = exercise_service.get_exercise_by_id(exercise_id)
        return success_response(exercise)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@exercise_bp.route('/<int:exercise_id>', methods=['PUT', 'PATCH'])
def update_exercise(exercise_id):
    """
    Update exercise
    ---
    tags:
      - exercises
    parameters:
      - name: exercise_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the exercise to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated exercise data
        schema:
          type: object
          properties:
            exercise_name:
              type: string
            workout_program_id:
              type: integer
    responses:
      200:
        description: Exercise updated successfully
      400:
        description: Invalid input data
      404:
        description: Exercise not found
    """
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
    """
    Delete exercise
    ---
    tags:
      - exercises
    parameters:
      - name: exercise_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the exercise to delete
    responses:
      200:
        description: Exercise deleted successfully
      404:
        description: Exercise not found
    """
    try:
        exercise_service.delete_exercise(exercise_id)
        return success_response(message="Exercise deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))

