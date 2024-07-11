from typing import Callable, Type
from flask import Request
from src.presentation.http_types import HttpRequest, HttpResponse


def request_adapter(request: Type[Request], controller: Type[Callable]) -> HttpResponse:
    """
    Request adapter
        * parameters:
            - request(Request): request of the Flask
            - controller(Callable): Function of the controller
        * retrun:
            - An object of the HttpResponse
    """

    body = None

    if request.data:
        body = request.json

    http_request = HttpRequest(
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
        body=body,
    )

    http_response = controller(http_request)
    return http_response
