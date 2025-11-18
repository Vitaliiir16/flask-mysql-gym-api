from flask import Blueprint, request
from services import schedule_service
from utils.response_utils import success_response, error_response


schedule_bp = Blueprint('schedules', __name__)


@schedule_bp.route('/', methods=['POST'])
def create_schedule():
    """
    Create a new schedule
    ---
    tags:
      - schedules
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with schedule data
        schema:
          type: object
          properties:
            service_id:
              type: integer
              example: 1
            day_of_week:
              type: string
              example: "Monday"
            open_time:
              type: string
              format: time
              example: "08:00:00"
            close_time:
              type: string
              format: time
              example: "20:00:00"
          required:
            - service_id
            - day_of_week
            - open_time
            - close_time
    responses:
      201:
        description: Schedule created successfully
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        schedule_id = schedule_service.create_schedule(data)
        return success_response(
            {"schedule_id": schedule_id},
            "Schedule created successfully",
            201
        )
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@schedule_bp.route('/', methods=['GET'])
def get_all_schedules():
    """
    Get all schedules
    ---
    tags:
      - schedules
    responses:
      200:
        description: List of schedules
    """
    try:
        schedules = schedule_service.get_all_schedules()
        return success_response(schedules)
    except Exception as e:
        return error_response(str(e))


@schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    """
    Get schedule by ID
    ---
    tags:
      - schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the schedule
    responses:
      200:
        description: Schedule data
      404:
        description: Schedule not found
    """
    try:
        schedule = schedule_service.get_schedule_by_id(schedule_id)
        return success_response(schedule)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@schedule_bp.route('/<int:schedule_id>', methods=['PUT', 'PATCH'])
def update_schedule(schedule_id):
    """
    Update schedule
    ---
    tags:
      - schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the schedule to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated schedule data
        schema:
          type: object
          properties:
            service_id:
              type: integer
            day_of_week:
              type: string
            open_time:
              type: string
              format: time
            close_time:
              type: string
              format: time
    responses:
      200:
        description: Schedule updated successfully
      400:
        description: Invalid input data
      404:
        description: Schedule not found
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        schedule_service.update_schedule(schedule_id, data)
        return success_response(message="Schedule updated successfully")
    except ValueError as e:
        return error_response(
            str(e),
            status_code=404 if "not found" in str(e) else 400
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    """
    Delete schedule
    ---
    tags:
      - schedules
    parameters:
      - name: schedule_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the schedule to delete
    responses:
      200:
        description: Schedule deleted successfully
      404:
        description: Schedule not found
    """
    try:
        schedule_service.delete_schedule(schedule_id)
        return success_response(message="Schedule deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
