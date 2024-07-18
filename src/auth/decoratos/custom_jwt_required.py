from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request
from src.errors import handler_errors


def custom_jwt_required():
    """Decorator customized"""

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except Exception as e:
                response = handler_errors(e)
                return jsonify(response.body), response.status_code
            return fn(*args, **kwargs)

        return wrapper

    return decorator
