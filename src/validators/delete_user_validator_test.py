from src.errors.types import HttpUnprocessableEntityError
from .select_user_validator import select_user_validator


class MockRequest:
    """Mock of the request"""

    def __init__(self) -> None:
        self.args = None


def test_delete_user_validator():
    """Testing if the validated works"""

    request = MockRequest()
    request.args = {"user": "12312"}

    try:
        select_user_validator(request)
    except HttpUnprocessableEntityError as exception:
        assert exception.status_code == 422
        assert exception.name == "UnprocessableEntity"
