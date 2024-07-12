from src.infra.db.tests import UsersRpositorySpy
from .select_user import SelectUser


def test_select_user():
    """Test with the correct user_id"""

    user_id = "123456sfdfsadfsf"
    user_repository = UsersRpositorySpy()
    select_user = SelectUser(user_repository)

    response = select_user.select(user_id)

    # Testing input
    assert user_repository.select_user_attributes["user_id"] == user_id

    # Testing output
    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"]


def test_select_user_user_id_invalid():
    """Test with the incorrect user_id"""

    user_id = 123
    user_repository = UsersRpositorySpy()
    select_user = SelectUser(user_repository)

    try:
        select_user.select(user_id)
        assert False
    except Exception as exception:
        assert str(exception) == "Id inválido, o mesmo deve ser uma string"


def test_select_user_not_found():
    """Test with non-existent user"""

    user_id = "not found"
    user_repository = UsersRpositorySpy()
    select_user = SelectUser(user_repository)

    try:
        select_user.select(user_id)
        assert False
    except Exception as exception:
        assert str(exception) == "Usuário não encontrado"
