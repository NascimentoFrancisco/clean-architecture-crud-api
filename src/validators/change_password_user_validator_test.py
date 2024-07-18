from src.errors.types import HttpUnprocessableEntityError
from .change_password_user_validator import change_password_user_validator


class MockRequest:
    """Mock of the request"""

    def __init__(self) -> None:
        self.json = None


def test_change_passwor_validator():
    """Testing if the validated works"""

    request = MockRequest()
    request.json = {"new_password": 12345, "password_confirmation": "alguma coisa"}

    try:
        change_password_user_validator(request)
    except HttpUnprocessableEntityError as exception:
        assert exception.status_code == 422
        assert exception.name == "UnprocessableEntity"
