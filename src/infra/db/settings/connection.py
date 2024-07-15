import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """SqlAlchemy database donnection"""

    def __init__(self) -> None:

        host = os.getenv("HOST")
        user = os.getenv("USER_DATABASE")
        password = os.getenv("MYSQL_ROOT_PASSWORD")
        port = os.getenv("PORT")
        database = os.getenv("MYSQL_DATABASE")

        self.__connection_string = (
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        """
        Returns the engine used to connect to the database
            * parameters:
                - None
                - object of engine
            * retrun:
                - object of engine
        """
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
