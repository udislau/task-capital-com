# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.storage import get_storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_storage():
    """
    Clear the lru_cache for get_storage to ensure each test gets a fresh Storage instance.
    """
    get_storage.cache_clear()


def test_get_without_post():
    """Test that GET returns a 404 if no value has been stored."""
    response = client.get("/store")
    assert response.status_code == 404
    assert response.json() == {"detail": "No value stored."}


def test_post_and_get():
    """Test that a value can be stored with POST and then retrieved with GET."""
    test_string = "Hello, FastAPI!"
    post_response = client.post("/store", json={"value": test_string})
    assert post_response.status_code == 201
    assert post_response.json() == {"message": "Value stored successfully."}

    get_response = client.get("/store")
    assert get_response.status_code == 200
    assert get_response.json() == {"value": test_string}


def test_post_invalid_payload():
    """Test that an invalid payload results in a 422 Unprocessable Entity error."""
    response = client.post("/store", json={"invalid": "data"})
    assert response.status_code == 422
