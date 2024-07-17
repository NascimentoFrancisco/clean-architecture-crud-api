from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.presentation.interface import JwtServiceInterface
from src.domain.use_cases import AuthenticateUserInterface


class AuthenticateUserController(ControllerInterface):
    """Class to define the Route to AuthenticateUser use case"""

    def __init__(
        self,
        authenticate_user_use_case: Type[AuthenticateUserInterface],
        jwt_service: Type[JwtServiceInterface],
    ) -> None:
        self.__authenticate_user_use_case = authenticate_user_use_case
        self.__jwt_service = jwt_service

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        email = http_request.body["email"]
        password = http_request.body["password"]

        response = self.__authenticate_user_use_case.authenticate_user(email, password)
        data = self.__jwt_service.generate_access_token(response["attributes"]["email"])

        return HttpResponse(status_code=200, body={"data": data})
