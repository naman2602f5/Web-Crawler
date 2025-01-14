from http.client import HTTPException
from flask import jsonify


def handle_error(error, status=500):
    error_message = str(error)
    status_code = status

    if isinstance(error, HTTPException):
        error_message = error.description
        status_code = error.code

    response = {
        "message": error_message,
        "status": status_code
    }

    return jsonify(response), status_code