from flask import Blueprint, request
from services import schedule_service
from utils.response_utils import success_response, error_response


schedule_bp = Blueprint('schedules', __name__)


@schedule_bp.route('/', methods=['POST'])
def create_schedule():
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
    try:
        schedules = schedule_service.get_all_schedules()
        return success_response(schedules)
    except Exception as e:
        return error_response(str(e))


@schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    try:
        schedule = schedule_service.get_schedule_by_id(schedule_id)
        return success_response(schedule)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@schedule_bp.route('/<int:schedule_id>', methods=['PUT', 'PATCH'])
def update_schedule(schedule_id):
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
    try:
        schedule_service.delete_schedule(schedule_id)
        return success_response(message="Schedule deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
