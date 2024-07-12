from src.data.tests import UpdateUserSpy
from src.presentation.http_types import HttpResponse
from .update_user_controller import UpdateUserController


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.body = {
            "name": "Testes",
            "email": "testes@teste.com",
        }
        self.query_params = {"user_id": "e123ewqwe"}


def test_handle():
    """Testing update route"""

    http_request = HttpRequestMock()
    update_use_case = UpdateUserSpy()
    controller = UpdateUserController(update_use_case)

    response = controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]
