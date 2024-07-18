from src.presentation.http_types import HttpResponse
from src.auth.tests import JwtServiceSpy
from src.data.tests import ChangePasswordUserSpy
from .change_password_user_controller import ChangePasswordUserController


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.body = {
            "new_password": "email@email.com",
            "password_confirmation": "password",
        }


def test_handle():
    """Testing the change password route"""

    http_request = HttpRequestMock()
    use_case = ChangePasswordUserSpy()
    jwt_service = JwtServiceSpy()
    change_password_user_controller = ChangePasswordUserController(
        use_case, jwt_service
    )

    response = change_password_user_controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]
