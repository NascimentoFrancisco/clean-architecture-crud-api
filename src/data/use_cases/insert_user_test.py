# pylint: disable = broad-exception-caught
from src.infra.db.tests import UsersRpositorySpy, HashingServiseSpy
from .insert_user import InsertUser


def test_insert_user():
    """Test with the correct data"""

    name = "Teste dos testes"
    email = "teste@teste.com"
    password = "Teste#123"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()
    insert_user = InsertUser(user_repository, hashing_service)
    response = insert_user.insert(name, email, password)

    # Testing input
    assert user_repository.insert_user_attributes["name"] == name
    assert user_repository.insert_user_attributes["email"] == email
    assert hashing_service.encrypt_password_attributes["encrypt_password"] == password

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_insert_user_name_invalid():
    """Test with the incorrect name"""

    name = "Teste1234"
    email = "teste@teste.com"
    password = "Teste#123"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()
    insert_user = InsertUser(user_repository, hashing_service)

    # Testing output
    try:
        insert_user.insert(name, email, password)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome inválido"


def test_insert_user_email_invalid():
    """Test with the incorrect email"""

    name = "Teste dos testes"
    email = "testeteste.com"
    password = "Teste#123"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()
    insert_user = InsertUser(user_repository, hashing_service)

    # Testing output
    try:
        insert_user.insert(name, email, password)
        assert False
    except Exception as exception:
        assert str(exception) == "Email inválido"


def test_insert_user_password_invalid():
    """Test with the incorrect password"""

    name = "Teste dos testes"
    email = "teste@teste.com"
    password = "Teste"

    user_repository = UsersRpositorySpy()
    hashing_service = HashingServiseSpy()
    insert_user = InsertUser(user_repository, hashing_service)

    # Testing output
    try:
        insert_user.insert(name, email, password)
        assert False
    except Exception as exception:
        msg = "Senha inválida, a senha deve ter pelo menos 8 caracteres. Contendo"
        msg += " letras maiúsculas e minúsculas, numeros, e carcteres especiais"
        assert str(exception) == msg
