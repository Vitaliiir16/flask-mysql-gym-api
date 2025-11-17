from flask import Blueprint, request
from services import procedure_service
from utils.response_utils import success_response, error_response


procedure_bp = Blueprint('procedures', __name__)


@procedure_bp.route('/insert-into-table', methods=['POST'])
def insert_into_table():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        procedure_service.execute_insert_into_table(data)
        return success_response(message="Data inserted successfully via procedure")
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@procedure_bp.route('/insert-equipment', methods=['POST'])
def insert_equipment():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        procedure_service.execute_insert_equipment(data)
        return success_response(message="Equipment inserted successfully via procedure")
    except Exception as e:
        return error_response(str(e), status_code=400)


@procedure_bp.route('/add-exercise-equipment', methods=['POST'])
def add_exercise_equipment():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        procedure_service.execute_add_exercise_equipment(data)
        return success_response(
            message="Exercise-Equipment link added successfully via procedure"
        )
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e), status_code=400)


@procedure_bp.route('/insert-multiple-equipment', methods=['POST'])
def insert_multiple_equipment():
    try:
        procedure_service.execute_insert_multiple_equipment()
        return success_response(
            message="Multiple equipment inserted successfully via procedure"
        )
    except Exception as e:
        return error_response(str(e))


@procedure_bp.route('/get-column-stats', methods=['POST'])
def get_column_stats():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        result = procedure_service.execute_get_column_stats(data)
        return success_response({"result": result})
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@procedure_bp.route('/split-table-randomly', methods=['POST'])
def split_table_randomly():
    try:
        data = request.get_json(silent=True) or {}
        if not data or "table_name" not in data:
            return error_response("Missing 'table_name' in JSON body", status_code=400)
        procedure_service.execute_split_table_randomly(data)
        return success_response(
            message=f"Table '{data['table_name']}' split successfully"
        )
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e))
