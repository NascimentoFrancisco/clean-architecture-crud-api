from src.presentation.http_types import HttpResponse
from src.data.tests import DeleteUserSpy
from .delete_user_controller import DeleteUserController


class HttpRequestMock:
    """HttpRequest mock"""

    def __init__(self) -> None:
        self.query_params = {"user_id": "e123ewqwe"}


def test_handle():
    """Testing the delte route"""

    http_request = HttpRequestMock()
    use_case = DeleteUserSpy()
    delte_user_controller = DeleteUserController(use_case)

    response = delte_user_controller.handle(http_request)

    # Testing output
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]
