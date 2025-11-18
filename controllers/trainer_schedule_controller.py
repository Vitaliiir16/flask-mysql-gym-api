from flask import Blueprint, request
from services import trainer_schedule_service
from utils.response_utils import success_response, error_response


trainer_schedule_bp = Blueprint('trainer_schedules', __name__)


@trainer_schedule_bp.route('/', methods=['POST'])
def create_trainer_schedule():
    """
    Create a new trainer schedule
    ---
    tags:
      - trainer_schedules
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with trainer schedule data
        schema:
          type: object
          properties:
            trainer_id:
              type: integer
              example: 1
            day_of_week:
              type: string
              example: "Monday"
          required:
            - trainer_id
            - day_of_week
    responses:
      201:
        description: Trainer schedule created
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        schedule_id = trainer_schedule_service.create_trainer_schedule(data)
        return success_response({"schedule_id": schedule_id}, "Trainer schedule created", 201)
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@trainer_schedule_bp.route('/', methods=['GET'])
def get_all_trainer_schedules():
    """
    Get all trainer schedules
    ---
    tags:
      - trainer_schedules
    responses:
      200:
        description: List of trainer schedules
    """
    try:
        schedules = trainer_schedule_service.get_all_trainer_schedules()
        return success_response(schedules)
    except Exception as e:
        return error_response(str(e))


@trainer_schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_trainer_schedule(schedule_id):
    """
    Get trainer schedule by ID
    ---
    tags:
      - trainer_schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer schedule
    responses:
      200:
        description: Trainer schedule data
      404:
        description: Trainer schedule not found
    """
    try:
        schedule = trainer_schedule_service.get_trainer_schedule_by_id(schedule_id)
        return success_response(schedule)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@trainer_schedule_bp.route('/<int:schedule_id>', methods=['PUT', 'PATCH'])
def update_trainer_schedule(schedule_id):
    """
    Update trainer schedule
    ---
    tags:
      - trainer_schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer schedule to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated trainer schedule data
        schema:
          type: object
          properties:
            trainer_id:
              type: integer
            day_of_week:
              type: string
    responses:
      200:
        description: Trainer schedule updated
      400:
        description: Invalid input data
      404:
        description: Trainer schedule not found
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        trainer_schedule_service.update_trainer_schedule(schedule_id, data)
        return success_response(message="Trainer schedule updated")
    except ValueError as e:
        return error_response(str(e), status_code=404 if "not found" in str(e) else 400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@trainer_schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
def delete_trainer_schedule(schedule_id):
    """
    Delete trainer schedule
    ---
    tags:
      - trainer_schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the trainer schedule to delete
    responses:
      200:
        description: Trainer schedule deleted
      404:
        description: Trainer schedule not found
    """
    try:
        trainer_schedule_service.delete_trainer_schedule(schedule_id)
        return success_response(message="Trainer schedule deleted")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
