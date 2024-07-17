from src.errors.types import HttpUnprocessableEntityError
from .authenticate_user_validator import authenticate_user_validator


class MockRequest:
    """Mock of the request"""

    def __init__(self) -> None:
        self.json = None


def test_iauthenticate_user_validator():
    """Testing if the validated works"""

    request = MockRequest()
    request.json = {"email": "email@email.com", "password": 12345}

    try:
        authenticate_user_validator(request)
    except HttpUnprocessableEntityError as exception:
        assert exception.status_code == 422
        assert exception.name == "UnprocessableEntity"
