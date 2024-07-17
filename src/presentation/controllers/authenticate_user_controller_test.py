from src.presentation.http_types import HttpResponse
from src.auth.tests import JwtServiceSpy
from src.data.tests import AuthenticateUserSpy
from .authenticate_user_controller import AuthenticateUserController


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.body = {"email": "email@email.com", "password": "pasword"}


def test_handle():
    """Testing the delte route"""

    http_request = HttpRequestMock()
    use_case = AuthenticateUserSpy()
    jwt_service = JwtServiceSpy()
    authenticate_user_controller = AuthenticateUserController(use_case, jwt_service)

    response = authenticate_user_controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]
