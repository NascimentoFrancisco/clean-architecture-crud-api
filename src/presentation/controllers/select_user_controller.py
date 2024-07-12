from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.domain.use_cases import SelectUserInterface


class SelectUserController(ControllerInterface):
    """Class to define the Route to SelectUser use case"""

    def __init__(self, insert_user_use_case: Type[SelectUserInterface]) -> None:
        self.__insert_user_use_case = insert_user_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        user_id = http_request.query_params["user_id"]
        response = self.__insert_user_use_case.select(user_id)

        return HttpResponse(status_code=200, body={"data": response})
