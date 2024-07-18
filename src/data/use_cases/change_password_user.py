import re
from typing import Type, Dict
from src.domain.use_cases import HashingServiseInterface
from src.data.interfaces import UserRepositoryInterface
from src.domain.use_cases import ChangePasswordUserInterface
from src.errors.types import HttpBadRequestError
from src.domain.entites import Users


class ChangePasswordUser(ChangePasswordUserInterface):
    """Class that implements the ChangePasswordUser use case"""

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        hashing_service: Type[HashingServiseInterface],
    ) -> None:
        self.__user_repository = user_repository
        self.__hashing_service = hashing_service

    def change_password(
        self, email: str, new_password: str, password_confirmation: str
    ) -> Dict:
        self.__check_passwords(new_password, password_confirmation)
        self.__validate_password(new_password)
        new_encrypted_password = self.__hashing_service.encrypt_password(new_password)
        user_password_changed = self.__user_repository.change_password_user(
            email, new_encrypted_password
        )

        return self.__format_response(user_password_changed)

    @classmethod
    def __check_passwords(cls, new_password: str, password_confirmation: str) -> None:
        if password_confirmation != new_password:
            raise HttpBadRequestError("Senha diferente da confirmação de senha")

    @classmethod
    def __validate_password(cls, password) -> None:
        if (
            len(password) < 8
            or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
            or not re.search(r"[a-z]", password)
            or not re.search(r"[0-9]", password)
        ):
            msg = "Senha inválida, a senha deve ter pelo menos 8 caracteres. Contendo"
            msg += " letras maiúsculas e minúsculas, numeros, e carcteres especiais"
            raise HttpBadRequestError(msg)

    @classmethod
    def __format_response(cls, user: Type[Users]) -> Dict:
        response = {
            "type": "users",
            "count": 1,
            "id": user.id,
            "attributes": {"message": "Senha alterado com sucesso"},
        }
        return response
