# pylint: disable=not-callable
from sqlalchemy import Column, String, DateTime, func
from src.infra.db.mixins import UUIDMixin
from src.infra.db.settings.base import Base


class Users(Base, UUIDMixin):
    """Model class for the User entity to perform operations on the database"""

    __tablename__ = "users"

    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User [name={self.name}, email={self.email}]"

    def __eq__(self, value: object) -> bool:
        if self.id == value.id and self.name == value.name and self.email == value.name:
            return True
        return False
