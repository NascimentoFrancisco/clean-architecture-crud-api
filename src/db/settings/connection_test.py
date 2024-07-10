import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    """Database connection test"""

    bd_connection_handler = DBConnectionHandler()
    engine = bd_connection_handler.get_engine()

    assert engine is not None
