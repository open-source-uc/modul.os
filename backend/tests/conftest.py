import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    return client


@pytest.fixture(scope="module")
def test_db():
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/python_db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()