from src.infra.db.settings import DBConnectionHandler
from src.infra.db.models import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, email: str, password: str) -> None:
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
            except Exception as exception:
                database.session.rollback()
                raise exception
