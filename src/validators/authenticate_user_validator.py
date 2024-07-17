# pylint: disable=inconsistent-return-statements
from flask import Request
from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def authenticate_user_validator(request: Request) -> None:
    """
    Validator of fields required to  authenticate user
        - paramenters:
            * request(Request): request of the Flask
        - return:
            * None
    """

    body_validator = Validator(
        {
            "email": {"type": "string", "required": True, "empty": False},
            "password": {"type": "string", "required": True, "empty": False},
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
