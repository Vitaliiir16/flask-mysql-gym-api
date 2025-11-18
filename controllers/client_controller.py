from flask import Blueprint, request
from services import client_service
from utils.response_utils import success_response, error_response


client_bp = Blueprint('clients', __name__)


@client_bp.route('/', methods=['POST'])
def create_client():
    """
    Create a new client
    ---
    tags:
      - clients
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with client data
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Petro"
            surname:
              type: string
              example: "Mostavchuk"
            phone_number:
              type: string
              example: "123-456-7891"
            trainer_id:
              type: integer
              example: 1
          required:
            - name
            - surname
    responses:
      201:
        description: Client created successfully
      400:
        description: Invalid input data
    """
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
    """
    Get all clients
    ---
    tags:
      - clients
    responses:
      200:
        description: List of clients
    """
    try:
        clients = client_service.get_all_clients()
        return success_response(clients)
    except Exception as e:
        return error_response(str(e))


@client_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """
    Get client by ID
    ---
    tags:
      - clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the client
    responses:
      200:
        description: Client data
      404:
        description: Client not found
    """
    try:
        client = client_service.get_client_by_id(client_id)
        return success_response(client)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@client_bp.route('/<int:client_id>', methods=['PUT', 'PATCH'])
def update_client(client_id):
    """
    Update client
    ---
    tags:
      - clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the client to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated client data
        schema:
          type: object
          properties:
            name:
              type: string
            surname:
              type: string
            phone_number:
              type: string
            trainer_id:
              type: integer
    responses:
      200:
        description: Client updated successfully
      400:
        description: Invalid input data
      404:
        description: Client not found
    """
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
    """
    Delete client
    ---
    tags:
      - clients
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the client to delete
    responses:
      200:
        description: Client deleted successfully
      404:
        description: Client not found
    """
    try:
        client_service.delete_client(client_id)
        return success_response(message="Client deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
