# pylint: disable=inconsistent-return-statements
from flask import Request
from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def delete_user_validator(request: Request):
    """
    Validator of fields required to delete user
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

    response = query_validator.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
