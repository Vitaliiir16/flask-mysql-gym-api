from flask import jsonify

def success_response(data=None, message="Operation successful", status_code=200):
    response = {
        "status": "success",
        "message": message
    }
    if data is not None:
        response["data"] = data
    return jsonify(response), status_code

def error_response(message="An error occurred", details=None, status_code=500):
    response = {
        "status": "error",
        "message": message
    }
    if details is not None:
        response["details"] = details
    return jsonify(response), status_code