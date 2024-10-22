from sqlalchemy.exc import IntegrityError, NoResultFound
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from src.presentation.http_types import HttpResponse
from .types import (
    HttpConflictError,
    HttpBadRequestError,
    HttpNotFoundError,
    HttpUnauthorizedError,
    HttpUnprocessableEntityError,
)


def handler_errors(error: Exception) -> HttpResponse:
    """Handler errors"""

    if isinstance(error, IntegrityError):
        exception = HttpConflictError("Email já existente no sistema")
        return HttpResponse(
            status_code=exception.status_code,
            body={"errors": [{"title": exception.name, "detail": exception.message}]},
        )

    if isinstance(error, NoResultFound):
        exception = HttpNotFoundError("Usuário não encontrado")
        return HttpResponse(
            status_code=exception.status_code,
            body={"errors": [{"title": exception.name, "detail": exception.message}]},
        )

    if isinstance(
        error, (NoAuthorizationError, ExpiredSignatureError, InvalidSignatureError)
    ):
        exception = HttpUnauthorizedError(str(error))
        return HttpResponse(
            status_code=exception.status_code,
            body={"errors": [{"title": exception.name, "detail": exception.message}]},
        )

    if isinstance(
        error,
        (HttpBadRequestError, HttpUnprocessableEntityError, HttpUnauthorizedError),
    ):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"erros": [{"title": "Server Error", "detail": str(error)}]},
    )
