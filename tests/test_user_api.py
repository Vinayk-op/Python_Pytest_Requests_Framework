import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_getuser_validation(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) > 0

def test_create_users(api_client, get_test_data):
    user_data = get_test_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    response = api_client.post("users", user_data)
    assert response.status_code == 201
    print(response.json())
    id = response.json()["id"]
    print("new created id: ", id)
    # response = api_client.get("users/" + str(id))  # Unable to fetch realtime id bcs jsonplaceholder is a fake API and it doesn't store the data we post, it just returns a response with a new id.
    response = api_client.get(f"users/10")
    assert response.status_code == 200
    print(response.json())

def test_update_user(api_client, get_test_data):
    user_data = get_test_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    response = api_client.put("users/1", user_data)
    assert response.status_code == 200
    print(response.json())

def test_delete_user(api_client):
    response = api_client.delete("users/1")
    assert response.status_code == 200



