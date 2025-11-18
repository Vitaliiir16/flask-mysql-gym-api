from flask import Blueprint, request
from services import membership_service
from utils.response_utils import success_response, error_response


membership_bp = Blueprint('memberships', __name__)



@membership_bp.route('/', methods=['POST'])
def create_membership():
    """
    Create a new membership
    ---
    tags:
      - memberships
    parameters:
      - in: body
        name: body
        required: true
        description: JSON payload with membership data
        schema:
          type: object
          properties:
            client_id:
              type: integer
              example: 1
            membership_type:
              type: string
              example: "Monthly"
            start_date:
              type: string
              format: date
              example: "2025-01-01"
            end_date:
              type: string
              format: date
              example: "2025-01-31"
          required:
            - client_id
            - membership_type
            - start_date
    responses:
      201:
        description: Membership created successfully
      400:
        description: Invalid input data
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        membership_id = membership_service.create_membership(data)
        return success_response(
            {"membership_id": membership_id},
            "Membership created successfully",
            201
        )
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@membership_bp.route('/', methods=['GET'])
def get_all_memberships():
    """
    Get all memberships
    ---
    tags:
      - memberships
    responses:
      200:
        description: List of memberships
    """
    try:
        memberships = membership_service.get_all_memberships()
        return success_response(memberships)
    except Exception as e:
        return error_response(str(e))


@membership_bp.route('/<int:membership_id>', methods=['GET'])
def get_membership(membership_id):
    """
    Get membership by ID
    ---
    tags:
      - memberships
    parameters:
      - name: membership_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the membership
    responses:
      200:
        description: Membership data
      404:
        description: Membership not found
    """
    try:
        membership = membership_service.get_membership_by_id(membership_id)
        return success_response(membership)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@membership_bp.route('/<int:membership_id>', methods=['PUT', 'PATCH'])
def update_membership(membership_id):
    """
    Update membership
    ---
    tags:
      - memberships
    parameters:
      - name: membership_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the membership to update
      - in: body
        name: body
        required: true
        description: JSON payload with updated membership data
        schema:
          type: object
          properties:
            client_id:
              type: integer
            membership_type:
              type: string
            start_date:
              type: string
              format: date
            end_date:
              type: string
              format: date
    responses:
      200:
        description: Membership updated successfully
      400:
        description: Invalid input data
      404:
        description: Membership not found
    """
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        membership_service.update_membership(membership_id, data)
        return success_response(message="Membership updated successfully")
    except ValueError as e:
        return error_response(
            str(e),
            status_code=404 if "not found" in str(e) else 400
        )
    except Exception as e:
        return error_response(str(e), status_code=400)


@membership_bp.route('/<int:membership_id>', methods=['DELETE'])
def delete_membership(membership_id):
    """
    Delete membership
    ---
    tags:
      - memberships
    parameters:
      - name: membership_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the membership to delete
    responses:
      200:
        description: Membership deleted successfully
      404:
        description: Membership not found
    """
    try:
        membership_service.delete_membership(membership_id)
        return success_response(message="Membership deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
