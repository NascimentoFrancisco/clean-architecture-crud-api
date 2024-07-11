from flask import Blueprint, request, jsonify
from src.main.adapters import request_adapter
from src.main.composers import insert_user_composer


user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route("/user/create", methods=["POST"])
def insert_user():
    """Route insert User"""

    http_response = request_adapter(request, insert_user_composer())

    return jsonify(http_response.body), http_response.status_code
