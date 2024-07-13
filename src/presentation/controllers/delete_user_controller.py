from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.domain.use_cases import DeleteUserInterface


class DeleteUserController(ControllerInterface):
    """Class to define the Route to DeleteUser use case"""

    def __init__(self, delete_user_use_case: Type[DeleteUserInterface]) -> None:
        self.__delete_user_use_case = delete_user_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        user_id = http_request.query_params["user_id"]
        response = self.__delete_user_use_case.delete(user_id)

        return HttpResponse(status_code=200, body={"data": response})
