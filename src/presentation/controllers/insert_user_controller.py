from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.domain.use_cases import InsertUserInterface


class InsertUserController(ControllerInterface):
    """Class to define the Route to InsertUser use case"""

    def __init__(self, insert_user_use_case: Type[InsertUserInterface]) -> None:
        self.__insert_user_use_case = insert_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        name = http_request.body["name"]
        email = http_request.body["email"]
        password = http_request.body["password"]

        response = self.__insert_user_use_case.insert(name, email, password)

        return HttpResponse(status_code=201, body={"data": response})
