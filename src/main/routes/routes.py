from flask import Blueprint, request, jsonify
from src.main.adapters import request_adapter
from src.main.composers import insert_user_composer
from src.errors import handler_errors
from src.validators import insert_user_validator

user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route("/user/create", methods=["POST"])
def insert_user():
    """Route insert User"""

    http_response = None

    try:
        insert_user_validator(request)
        http_response = request_adapter(request, insert_user_composer())
    except Exception as exception:
        http_response = handler_errors(exception)

    return jsonify(http_response.body), http_response.status_code
