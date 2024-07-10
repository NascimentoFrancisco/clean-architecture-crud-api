import uuid
from sqlalchemy import Column, String


class UUIDMixin:
    """Mixin class to set model id as uuid"""

    id = Column(
        String(38),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
