from src.infra.db.tests import UsersRpositorySpy
from .update_user import UpdateUser


def test_update_user():
    """Testing with user_id valid"""

    user_id = "2121212"
    data = {"name": "testes", "email": "teste@eamil.com"}

    user_repository = UsersRpositorySpy()
    update_user_case = UpdateUser(user_repository)

    response = update_user_case.update(user_id, **data)

    # Testing input
    assert user_repository.update_user_attributes["user_id"] == user_id
    assert user_repository.update_user_attributes["name"] == data["name"]
    assert user_repository.update_user_attributes["email"] == data["email"]

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_update_user_user_id_invalid():
    """Testing with user_id invalid"""

    user_id = 2121212
    data = {"name": "testes", "email": "teste@eamil.com"}

    user_repository = UsersRpositorySpy()
    update_user_case = UpdateUser(user_repository)

    try:
        update_user_case.update(user_id, **data)
        assert False
    except Exception as exception:
        assert str(exception) == "Id inválido, o mesmo deve ser uma string"


def test_update_user_name_or_email_invalid():
    """Testing with name and email invalid"""

    user_id = "1331313"
    data = {"name": "testes1231", "email": "teste@eamil.com"}

    user_repository = UsersRpositorySpy()
    update_user_case = UpdateUser(user_repository)

    try:
        update_user_case.update(user_id, **data)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome inválido"

    data["name"] = "nome valido"
    data["email"] = "teste"

    try:
        update_user_case.update(user_id, **data)
        assert False
    except Exception as exception:
        assert str(exception) == "Email inválido"


def test_update_user_data_null():
    """Testing with data null"""

    user_id = "1331313"
    data = {}

    user_repository = UsersRpositorySpy()
    update_user_case = UpdateUser(user_repository)

    try:
        update_user_case.update(user_id, **data)
        assert False
    except Exception as exception:
        assert str(exception) == "name ou email deve ser informado"
