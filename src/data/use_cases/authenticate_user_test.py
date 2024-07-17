from src.infra.db.tests import UsersRpositorySpy, HashingServiseSpy
from .authenticate_user import AuthenticateUser


def test_authenticate_user():
    """Testing with credentials valid"""

    email = "teste@teste.com"
    password = "password"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    authenticate_user = AuthenticateUser(user_repository, hashing_service)
    response = authenticate_user.authenticate_user(email, password)

    # Testing input
    assert user_repository.select_user_by_email_attributes["email"] == email
    assert hashing_service.verify_password_attributes["raw_password"] == password

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_authenticate_user_email_invaid():
    """Testing with email invalid"""

    email = "testeteste.com"
    password = "password"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    authenticate_user = AuthenticateUser(user_repository, hashing_service)

    # Testing output
    try:
        authenticate_user.authenticate_user(email, password)
        assert False
    except Exception as exception:
        assert str(exception) == "Email inválido"


def test_authenticate_user_password_invaid():
    """Testing with password invalid"""

    email = "teste@teste.com"
    password = "passwordss"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()

    authenticate_user = AuthenticateUser(user_repository, hashing_service)

    # Testing output
    try:
        authenticate_user.authenticate_user(email, password)
        assert False
    except Exception as exception:
        assert str(exception) == "Credenciais fornecidas (email e senha) são inválidas"
