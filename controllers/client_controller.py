from flask import Blueprint, request
from services import client_service
from utils.response_utils import success_response, error_response

client_bp = Blueprint('clients', __name__)


@client_bp.route('/', methods=['POST'])
def create_client():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        client_id = client_service.create_client(data)
        return success_response(
            {"client_id": client_id},
            "Client created successfully",
            201
        )
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@client_bp.route('/', methods=['GET'])
def get_all_clients():
    try:
        clients = client_service.get_all_clients()
        return success_response(clients)
    except Exception as e:
        return error_response(str(e))


@client_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    try:
        client = client_service.get_client_by_id(client_id)
        return success_response(client)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@client_bp.route('/<int:client_id>', methods=['PUT', 'PATCH'])
def update_client(client_id):
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        client_service.update_client(client_id, data)
        return success_response(message="Client updated successfully")
    except ValueError as e:
        return error_response(
            str(e),
            status_code=404 if "not found" in str(e) else 400
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@client_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        client_service.delete_client(client_id)
        return success_response(message="Client deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
