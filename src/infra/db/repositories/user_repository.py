from src.infra.db.settings import DBConnectionHandler
from src.infra.db.models import Users
from src.data.interfaces import UserRepositoryInterface
from src.domain.entites import Users as UserEntity


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    def insert_user(self, name: str, email: str, password: str) -> Users:
        """
        Insert data from the User entity into the database
            * parameters:
                - name(str): name of  the user
                - email(str): email of  the user
                - password(str): password of  the user
            * retrun:
                - An object of the User entity
        """
        with DBConnectionHandler() as database:
            try:
                new_user = Users(name=name, email=email, password=password)

                database.session.add(new_user)
                database.session.commit()
                return UserEntity(
                    user_id=new_user.id,
                    name=new_user.name,
                    email=new_user.email,
                    password=new_user.password,
                )
            except Exception as exception:
                database.session.rollback()
                raise exception
