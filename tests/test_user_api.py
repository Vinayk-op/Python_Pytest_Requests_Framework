import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_getuser_validation(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) > 0

def test_create_users(api_client):
    user_data = {
        "name": "Vinay",
        "username": "vinay123",
        "email": "vinay123@gmail.com"
    }
    response = api_client.post("users", user_data)
    assert response.status_code == 201
    print(response.json())
    id = response.json()["id"]
    response = api_client.get("users/" + str(id))
    assert response.status_code == 200
    assert response.json()["name"] ==  user_data["name"]

