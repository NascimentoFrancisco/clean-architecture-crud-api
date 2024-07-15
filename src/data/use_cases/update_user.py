import re
from typing import Dict, Type
from src.domain.entites.users import Users
from src.errors.types import HttpBadRequestError, HttpUnprocessableEntityError
from src.data.interfaces import UserRepositoryInterface
from src.domain.use_cases import UpdateUserInterface


class UpdateUser(UpdateUserInterface):
    """Class that implements the UpdateUser use case"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        self.__user_repository = user_repository

    def update(self, user_id: str, **kwargs) -> Dict:
        self.__validate_user_id(user_id)
        self.__validate_data(kwargs)
        update_user = self.__update_user(user_id, kwargs)

        return self.__format_response(update_user)

    @classmethod
    def __validate_user_id(cls, user_id: str) -> None:
        if not isinstance(user_id, str):
            raise HttpBadRequestError("Id inválido, o mesmo deve ser uma string")

    @classmethod
    def __validate_data(cls, data: Dict) -> None:
        if data == {}:
            raise HttpUnprocessableEntityError("name ou email deve ser informado")

        if "name" in data:
            if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", data["name"]):
                raise HttpBadRequestError("Nome inválido")

        if "email" in data:
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(pattern, data["email"]):
                raise HttpBadRequestError("Email inválido")

    def __update_user(self, user_id: str, data: Dict) -> Users:
        return self.__user_repository.update_user(user_id, **data)

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"name": user.name, "email": user.email},
        }
        return response
