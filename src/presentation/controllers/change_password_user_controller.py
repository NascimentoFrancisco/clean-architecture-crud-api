from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.presentation.interface import JwtServiceInterface
from src.domain.use_cases import ChangePasswordUserInterface


class ChangePasswordUserController(ControllerInterface):
    """Class to define the Route to ChangePasswordUser use case"""

    def __init__(
        self,
        change_password_user_use_case: Type[ChangePasswordUserInterface],
        jwt_service: Type[JwtServiceInterface],
    ) -> None:
        self.__change_password_user_use_case = change_password_user_use_case
        self.__jwt_service = jwt_service

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        email = self.__jwt_service.get_logged_user_identity()
        new_password = http_request.body["new_password"]
        password_confirmation = http_request.body["password_confirmation"]

        response = self.__change_password_user_use_case.change_password(
            email, new_password, password_confirmation
        )

        return HttpResponse(status_code=200, body={"data": response})
