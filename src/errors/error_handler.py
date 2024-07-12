from sqlalchemy.exc import IntegrityError, NoResultFound
from src.presentation.http_types import HttpResponse
from .types import (
    HttpConflictError,
    HttpBadRequestError,
    HttpNotFoundError,
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

    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"erros": [{"title": "Server Error", "detail": str(error)}]},
    )
