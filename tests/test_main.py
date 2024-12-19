import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "REST API service" in response.json()["message"]


def test_count_unique_persons(client):
    response = client.get("/count-unique-persons?n_days=7")
    assert response.status_code == 200
    assert response.json() == {"n_days": 7, "unique_person_count": 145118}


def test_count_unique_persons_wrong_data(client):
    response = client.get("/count-unique-persons?n_days=-1")
    assert response.status_code == 422


def test_providers_and_persons_wrong_data(client):

    response = client.get("/number-providers-and-persons?procedure_type=1")
    assert response.status_code == 422
    assert response.json() == {"detail": "Procedure type 1 not supported. Please, choose from 38000251, 38000269"}
