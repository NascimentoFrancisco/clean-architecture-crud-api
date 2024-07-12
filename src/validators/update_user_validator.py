# pylint: disable=inconsistent-return-statements
from flask import Request
from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def update_user_validator(request: Request):
    """
    Validator of fields required to update user
        - paramenters:
            * request(Request): request of the Flask
        - return:
            * None
    """

    query_validator = Validator(
        {
            "user_id": {"type": "string", "required": True, "empty": False},
        }
    )

    body_validator = Validator(
        {
            "name": {"type": "string", "empty": False},
            "email": {"type": "string", "empty": False},
        }
    )

    response = query_validator.validate(request.args)
    body_response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)

    if body_response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
