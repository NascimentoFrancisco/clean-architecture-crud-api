from src.errors.types import HttpUnprocessableEntityError
from .update_user_validator import update_user_validator


class MockRequest:
    """Mock of the request"""

    def __init__(self) -> None:
        self.json = None
        self.args = None


def test_update_user_validator():
    """Testing if the validated works"""

    request = MockRequest()
    request.json = {"first_name": "Nome", "last_name": "alguma coisa", "age": 22}
    request.args = {"id": "122"}

    try:
        update_user_validator(request)
    except HttpUnprocessableEntityError as exception:
        assert exception.status_code == 422
        assert exception.name == "UnprocessableEntity"
