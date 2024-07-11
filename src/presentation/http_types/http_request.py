from typing import Any


class HttpRequest:
    """Class http_request representation"""

    def __init__(
        self,
        headers: Any = None,
        body: Any = None,
        query_params: Any = None,
        path_params: Any = None,
        url: Any = None,
        ipv4: Any = None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
