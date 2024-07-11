class HttpBadRequestError(Exception):
    """Bad Request"""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRquest"
        self.status_code = 400
