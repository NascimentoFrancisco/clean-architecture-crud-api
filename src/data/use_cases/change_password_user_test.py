from src.infra.db.tests import UsersRpositorySpy, HashingServiseSpy
from .change_password_user import ChangePasswordUser


def test_change_password_user():
    """Testing change password valid"""

    email = "teste@teste.com"
    new_password = "Teste#123"
    password_confirmation = "Teste#123"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    change_password_user = ChangePasswordUser(user_repository, hashing_service)
    response = change_password_user.change_password(
        email, new_password, password_confirmation
    )

    # Testing input
    assert (
        hashing_service.encrypt_password_attributes["encrypt_password"] == new_password
    )
    assert user_repository.change_password_user_user_attributes["email"] == email

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_change_password_user_different():
    """Testing change password different"""

    email = "teste@teste.com"
    new_password = "Teste#123"
    password_confirmation = "Teste#12"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    change_password_user = ChangePasswordUser(user_repository, hashing_service)

    # Testing output
    try:
        change_password_user.change_password(email, new_password, password_confirmation)
        assert False
    except Exception as exception:
        assert str(exception) == "Senha diferente da confirmação de senha"


def test_change_password_user_invalid():
    """Testing change password invalid"""

    email = "teste@teste.com"
    new_password = "Teste"
    password_confirmation = "Teste"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    change_password_user = ChangePasswordUser(user_repository, hashing_service)

    # Testing output
    try:
        change_password_user.change_password(email, new_password, password_confirmation)
        assert False
    except Exception as exception:
        msg = "Senha inválida, a senha deve ter pelo menos 8 caracteres. Contendo"
        msg += " letras maiúsculas e minúsculas, numeros, e carcteres especiais"
        assert str(exception) == msg


def test_change_password_user_not_found():
    """Testing change password not_found"""

    email = "email"
    new_password = "Teste#123"
    password_confirmation = "Teste#123"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    change_password_user = ChangePasswordUser(user_repository, hashing_service)

    # Testing output
    try:
        change_password_user.change_password(email, new_password, password_confirmation)
        assert False
    except Exception as exception:
        assert str(exception) == "'NoneType' object has no attribute 'id'"
