from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

from app.database import Base, get_db
from app.main import app

faker = Faker()

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/dbteste"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_schedule():
    response = client.post(
        "/scheduler/communication",
        json={
            "date_hour": f'{faker.date_time_this_year()}',
            "message": faker.text(),
            "status_send": faker.boolean(),
            "customer_id": 1,
            "channel_id": 2
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "success"


def teste_get_schedule():
    response = client.get(
        "/scheduler/communication"
    )
    assert response.status_code == 200, response.text


def teste_delete_schedule():
    response = client.delete(
        "/scheduler/communication/1"
    )
    assert response.status_code == 200, response.text    
