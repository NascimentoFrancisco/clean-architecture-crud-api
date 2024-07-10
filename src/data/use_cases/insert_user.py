# pylint: disable = broad-exception-raised
import re
from typing import Type, Dict
from src.domain.use_cases import InsertUserInterface
from src.data.interfaces import UserRepositoryInterface
from src.domain.entites import Users


class InsertUser(InsertUserInterface):
    """Class that implements the InsertUser use case"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        self.__user_repository = user_repository

    def insert(self, name: str, email: str, password: str) -> None:
        self.__validate_name(name)
        self.__validate_email(email)
        self.__validate_password(password)

        user = self.__save_user_informations(name, email, password)
        return self.__format_response(user)

    @classmethod
    def __validate_name(cls, name: str):
        if not name.isalpha():
            raise Exception("Nome inválido")

    @classmethod
    def __validate_email(cls, email: str):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise Exception("Email inválido")

    @classmethod
    def __validate_password(cls, password):
        if (
            len(password) < 8
            and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
            and not re.search(r"[a-z]", password)
            and not re.search(r"[0-9]", password)
        ):
            msg = "Senha inválida, a senha deve ter pelo menos 8 caracteres. Contendo"
            msg += " letras maiúsculas e minúsculas, numeros, e carcteres especiais"
            raise Exception(msg)

    def __save_user_informations(self, name: str, email: str, password: str) -> Users:
        return self.__user_repository.insert_user(name, email, password)

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"name": user.name, "email": user.email},
        }
        return response
