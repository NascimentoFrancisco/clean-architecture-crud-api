from typing import Type
from src.presentation.http_types import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interface import ControllerInterface
from src.domain.use_cases import UpdateUserInterface


class UpdateUserController(ControllerInterface):
    """Class to define the Route to UpdateUser use case"""

    def __init__(self, update_user_use_case: Type[UpdateUserInterface]) -> None:
        self.___update_user_use_case = update_user_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Method to call use case
        * parameters:
                - http_request(HttpRequest): request object
            * retrun:
                - An object of the HttpResponse
        """
        user_id = http_request.query_params["user_id"]
        data = http_request.body

        response = self.___update_user_use_case.update(user_id, **data)
        return HttpResponse(status_code=200, body={"data": response})
