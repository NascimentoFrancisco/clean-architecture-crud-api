from src.presentation.controllers import SelectUserController
from src.data.tests import SelectUserSpy
from src.presentation.http_types import HttpResponse


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.query_params = {"user_id": "e123ewqwe"}


def test_handle():
    """Testing the select route"""

    http_request = HttpRequestMock()
    use_case = SelectUserSpy()
    insert_user_controller = SelectUserController(use_case)

    response = insert_user_controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]
