from flask import Blueprint, request
from services import exercise_equipment_service
from utils.response_utils import success_response, error_response


exercise_equipment_bp = Blueprint('exercise_equipment', __name__)


@exercise_equipment_bp.route('/', methods=['POST'])
def link_exercise_to_equipment():
    """
    Link exercise to equipment
    ---
    tags:
      - exercise_equipment
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with exercise and equipment IDs
        schema:
          type: object
          properties:
            exercise_id:
              type: integer
              example: 1
            equipment_id:
              type: integer
              example: 2
          required:
            - exercise_id
            - equipment_id
    responses:
      201:
        description: Link created successfully
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)

        exercise_equipment_service.link_exercise_to_equipment(data)
        return success_response(message="Link created successfully", status_code=201)
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@exercise_equipment_bp.route('/', methods=['DELETE'])
def unlink_exercise_from_equipment():
    """
    Unlink exercise from equipment
    ---
    tags:
      - exercise_equipment
    parameters:
      - name: exercise_id
        in: query
        required: true
        schema:
          type: integer
        description: ID of the exercise
      - name: equipment_id
        in: query
        required: true
        schema:
          type: integer
        description: ID of the equipment
    responses:
      200:
        description: Link deleted successfully
      400:
        description: Missing or invalid query parameters
      404:
        description: Link not found
    """
    try:
        exercise_id = request.args.get('exercise_id', type=int)
        equipment_id = request.args.get('equipment_id', type=int)

        if not exercise_id or not equipment_id:
            raise ValueError("Missing 'exercise_id' or 'equipment_id' query parameters")

        exercise_equipment_service.unlink_exercise_from_equipment(exercise_id, equipment_id)
        return success_response(message="Link deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404 if "not found" in str(e) else 400)
    except Exception as e:
        return error_response(str(e))


@exercise_equipment_bp.route('/exercise/<int:exercise_id>', methods=['GET'])
def get_equipment_for_exercise(exercise_id):
    """
    Get equipment for exercise
    ---
    tags:
      - exercise_equipment
    parameters:
      - name: exercise_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the exercise
    responses:
      200:
        description: List of equipment linked to the exercise
      404:
        description: Exercise or links not found
    """
    try:
        equipment = exercise_equipment_service.get_equipment_for_exercise(exercise_id)
        return success_response(equipment)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@exercise_equipment_bp.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_exercises_for_equipment(equipment_id):
    """
    Get exercises for equipment
    ---
    tags:
      - exercise_equipment
    parameters:
      - name: equipment_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the equipment
    responses:
      200:
        description: List of exercises linked to the equipment
      404:
        description: Equipment or links not found
    """
    try:
        exercises = exercise_equipment_service.get_exercises_for_equipment(equipment_id)
        return success_response(exercises)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
