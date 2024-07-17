import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.infra.db.settings import DBConnectionHandler
from .user_repository import UserRepository

db_connectionHandler = DBConnectionHandler()
connection = db_connectionHandler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    """Should Insert User"""

    name = "Francisco"
    email = "testes"
    password = "password"

    user_repository = UserRepository()
    user_repository.insert_user(name, email, password)

    sql = f"SELECT * FROM users WHERE email = '{email}'"

    response = connection.execute(text(sql))
    registry = response.fetchone()

    assert registry.name == name
    assert registry.email == email
    assert registry.password == password

    sql = f"DELETE FROM users WHERE email = '{email}'"
    connection.execute(text(sql))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_unique_email_insert_user():
    """Enter a unique email per user"""

    name = "Francisco"
    email = "testes@test"
    password = "password"

    name_duplicate = "Francisco"
    email_duplicate = "testes@test"
    password_duplicate = "password"

    user_repository = UserRepository()
    user_repository.insert_user(name, email, password)

    try:
        user_repository.insert_user(name_duplicate, email_duplicate, password_duplicate)
        assert False
    except IntegrityError as exception:
        assert exception.args[0].split()[0] == "(pymysql.err.IntegrityError)"

    sql = f"DELETE FROM users WHERE email = '{email}'"
    connection.execute(text(sql))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    """Testing select user in database"""

    name = "Francisco"
    email = "testes@teste"
    password = "password"

    user_repository = UserRepository()
    registry = user_repository.insert_user(name, email, password)
    user_select = user_repository.select_user(registry.id)

    # Testing output
    assert user_select.name == name
    assert user_select.email == email
    assert user_select.id == registry.id

    sql = f"DELETE FROM users WHERE id = '{registry.id}'"
    connection.execute(text(sql))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user_by_email():
    """Testing select user in database"""

    name = "Francisco"
    email = "testes@teste"
    password = "password"

    user_repository = UserRepository()
    registry = user_repository.insert_user(name, email, password)
    user_select = user_repository.select_user_by_email(registry.email)

    # Testing output
    assert user_select.name == name
    assert user_select.email == email
    assert user_select.id == registry.id

    sql = f"DELETE FROM users WHERE id = '{registry.id}'"
    connection.execute(text(sql))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_update_user():
    """Testing update user in database"""

    name = "Francisco"
    email = "testes@teste"
    password = "password"

    user_repository = UserRepository()
    registry = user_repository.insert_user(name, email, password)

    data = {"name": "Francisco Leite", "email": "francisco@email.com"}

    update_user = user_repository.update_user(registry.id, **data)

    # Testing output
    assert registry.id == update_user.id
    assert data["name"] == update_user.name
    assert data["email"] == update_user.email

    sql = f"DELETE FROM users WHERE id = '{registry.id}'"
    connection.execute(text(sql))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_delete_user():
    """Testing delete user in database"""

    name = "Francisco"
    email = "testes@teste"
    password = "password"

    user_repository = UserRepository()
    registry = user_repository.insert_user(name, email, password)

    user_deleted = user_repository.delete_user(registry.id)

    try:
        user_repository.select_user(user_deleted.id)
        assert False
    except Exception as exception:
        assert isinstance(exception, NoResultFound)
