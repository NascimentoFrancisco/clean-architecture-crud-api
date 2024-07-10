import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
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
