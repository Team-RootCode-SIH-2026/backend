import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from ..core.config import settings
from ..db.database import Base
from ..models import *

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(url=settings.DATABASE_URL)

    Base.metadata.create_all(engine)
    yield engine

    Base.metadata.drop_all(engine)
    engine.dispose()
print("Created engine")

@pytest.fixture
def session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
            transaction.rollback()
            connection.close()
    Base.metadata.drop_all(engine)
