from src.infra.db.settings import DBConnectionHandler
from src.infra.db.models import Users
from src.data.interfaces import UserRepositoryInterface
from src.domain.entites import Users as UserEntity


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    def insert_user(self, name: str, email: str, password: str) -> UserEntity:
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

    def select_user(self, user_id: str) -> UserEntity:
        """
        Selects a user from the database using their id
            * parameters:
                - user_id(str): id of  the user
            * retrun:
                - An object of the User entity
        """

        with DBConnectionHandler() as database:
            try:
                user = database.session.query(Users).filter(Users.id == user_id).one()
                return UserEntity(
                    user_id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                )
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_user(self, user_id: str, **kwargs) -> UserEntity:
        """
        Updates a user's data by searching for their ID
            * parameters:
                - user_id: id of the user(necessary parameter to identify the user for the role)
                - name(str): name of  the user(Default value null if none provided)
                - email(str): email of  the user(Default value null if none provided)
            * retrun:
                - An object of the User entity
        """
        with DBConnectionHandler() as database:
            try:
                user = database.session.query(Users).filter(Users.id == user_id).one()
                columns = [c.name for c in user.__table__.columns]

                for col in columns:
                    if col in kwargs:
                        setattr(user, col, kwargs[col])

                database.session.commit()
                database.session.refresh(user)

                return UserEntity(
                    user_id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                )
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_user(self, user_id: str) -> UserEntity:
        """
        Delete a user from the database using their id
            * parameters:
                - user_id(str): id of  the user
            * retrun:
                - True if the operation goes well, False otherwise
        """
        with DBConnectionHandler() as database:
            try:
                user = database.session.query(Users).filter(Users.id == user_id).one()
                database.session.delete(user)
                database.session.commit()
                return UserEntity(
                    user_id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                )
            except Exception as exception:
                database.session.rollback()
                raise exception
