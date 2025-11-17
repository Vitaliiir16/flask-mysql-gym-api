from flask import Blueprint, request
from services import membership_service
from utils.response_utils import success_response, error_response

membership_bp = Blueprint('memberships', __name__)


@membership_bp.route('/', methods=['POST'])
def create_membership():
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        membership_id = membership_service.create_membership(data)
        return success_response({"membership_id": membership_id},
                                "Membership created successfully", 201)
    except ValueError as e:
        return error_response(str(e), status_code=400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@membership_bp.route('/', methods=['GET'])
def get_all_memberships():
    try:
        memberships = membership_service.get_all_memberships()
        return success_response(memberships)
    except Exception as e:
        return error_response(str(e))


@membership_bp.route('/<int:membership_id>', methods=['GET'])
def get_membership(membership_id):
    try:
        membership = membership_service.get_membership_by_id(membership_id)
        return success_response(membership)
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))


@membership_bp.route('/<int:membership_id>', methods=['PUT', 'PATCH'])
def update_membership(membership_id):
    try:
        data = request.get_json(silent=True) or {}
        if not data:
            return error_response("Invalid or missing JSON body", status_code=400)
        membership_service.update_membership(membership_id, data)
        return success_response(message="Membership updated successfully")
    except ValueError as e:
        return error_response(str(e),
                              status_code=404 if "not found" in str(e) else 400)
    except Exception as e:
        return error_response(str(e), status_code=400)


@membership_bp.route('/<int:membership_id>', methods=['DELETE'])
def delete_membership(membership_id):
    try:
        membership_service.delete_membership(membership_id)
        return success_response(message="Membership deleted successfully")
    except ValueError as e:
        return error_response(str(e), status_code=404)
    except Exception as e:
        return error_response(str(e))
