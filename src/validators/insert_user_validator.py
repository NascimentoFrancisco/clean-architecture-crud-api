# pylint: disable=inconsistent-return-statements
from flask import Request
from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def insert_user_validator(request: Request) -> None:
    """
    Validator of fields required to insert user
        - paramenters:
            * request(Request): request of the Flask
        - return:
            * None
    """

    body_validator = Validator(
        {
            "name": {"type": "string", "required": True, "empty": False},
            "email": {"type": "string", "required": True, "empty": False},
            "password": {"type": "string", "required": True, "empty": False},
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
