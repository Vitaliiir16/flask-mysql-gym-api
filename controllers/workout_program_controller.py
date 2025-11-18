from flask import Blueprint, request
from services import workout_program_service
from utils.response_utils import success_response, error_response


workout_program_bp = Blueprint('workout_programs', __name__)


@workout_program_bp.route('/', methods=['POST'])
def create_workout_program():
    """
    Create a new workout program
    ---
    tags:
      - workout_programs
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with workout program data
        schema:
          type: object
          properties:
            program_name:
              type: string
              example: "Beginner Strength"
            trainer_id:
              type: integer
              example: 1
          required:
            - program_name
    responses:
      201:
        description: Workout program created
      400:
        description: Invalid input data
    """
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
    """
    Get all workout programs
    ---
    tags:
      - workout_programs
    responses:
      200:
        description: List of workout programs
    """
    try:
        programs = workout_program_service.get_all_workout_programs()
        return success_response(programs)
    except Exception as e:
        return error_response(str(e))


@workout_program_bp.route('/<int:program_id>', methods=['GET'])
def get_workout_program(program_id):
    """
    Get workout program by ID
    ---
    tags:
      - workout_programs
    parameters:
      - name: program_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the workout program
    responses:
      200:
        description: Workout program data
      404:
        description: Workout program not found
    """
    try:
        program = workout_program_service.get_workout_program_by_id(program_id)
        return success_response(program)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@workout_program_bp.route('/<int:program_id>', methods=['PUT', 'PATCH'])
def update_workout_program(program_id):
    """
    Update workout program
    ---
    tags:
      - workout_programs
    parameters:
      - name: program_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the workout program to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated workout program data
        schema:
          type: object
          properties:
            program_name:
              type: string
            trainer_id:
              type: integer
    responses:
      200:
        description: Workout program updated
      400:
        description: Invalid input data
      404:
        description: Workout program not found
    """
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
    """
    Delete workout program
    ---
    tags:
      - workout_programs
    parameters:
      - name: program_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the workout program to delete
    responses:
      200:
        description: Workout program deleted
      404:
        description: Workout program not found
    """
    try:
        workout_program_service.delete_workout_program(program_id)
        return success_response(message="Workout program deleted")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
