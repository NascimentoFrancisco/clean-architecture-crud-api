from typing import Type, Any


class HttpResponse:
    """Class http_response representation"""

    def __init__(self, status_code: int, body: Type[Any]) -> None:
        self.status_code = status_code
        self.body = body
