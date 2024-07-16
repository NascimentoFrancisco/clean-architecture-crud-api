from flask import Blueprint, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.main.adapters import request_adapter
from src.main.composers import insert_user_composer
from src.main.composers import select_user_composer
from src.main.composers import update_user_composer
from src.main.composers import delete_user_composer
from src.errors import handler_errors
from src.validators import (
    insert_user_validator,
    select_user_validator,
    update_user_validator,
    delete_user_validator,
)

user_routes_bp = Blueprint("user_routes", __name__)
limiter = Limiter(key_func=get_remote_address)


@user_routes_bp.route("/user/create", methods=["POST"])
@limiter.limit("5 per minute")
def insert_user():
    """Route insert User"""

    http_response = None

    try:
        insert_user_validator(request)
        http_response = request_adapter(request, insert_user_composer())
    except Exception as exception:
        http_response = handler_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user/select", methods=["GET"])
@limiter.limit("10 per minute")
def select_user():
    """Route select User"""

    http_response = None

    try:
        select_user_validator(request)
        http_response = request_adapter(request, select_user_composer())
    except Exception as exception:
        http_response = handler_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user/update", methods=["PUT", "PATCH"])
@limiter.limit("5 per minute")
def update_user():
    """Route update User"""

    http_response = None

    try:
        update_user_validator(request)
        http_response = request_adapter(request, update_user_composer())
    except Exception as exception:
        http_response = handler_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user/delete", methods=["DELETE"])
@limiter.limit("5 per minute")
def delete_user():
    """Route delete User"""

    http_response = None

    try:
        delete_user_validator(request)
        http_response = request_adapter(request, delete_user_composer())
    except Exception as exception:
        http_response = handler_errors(exception)

    return jsonify(http_response.body), http_response.status_code
