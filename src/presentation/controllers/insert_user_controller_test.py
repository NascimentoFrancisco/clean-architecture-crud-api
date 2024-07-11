from src.presentation.controllers import InsertUserController
from src.data.tests import InsertUserSpy
from src.presentation.http_types import HttpResponse


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.body = {
            "name": "Testes",
            "email": "testes@teste.com",
            "password": "Teste123#",
        }


def test_handle():
    """Testing the registration route"""

    http_request = HttpRequestMock()
    use_case = InsertUserSpy()
    insert_user_controller = InsertUserController(use_case)

    response = insert_user_controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body["data"]
