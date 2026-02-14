import pytest
from utils.apis import APIS


@pytest.fixture(scope="module")
def apis():
    return APIS()


def test_getuser_validation(apis):
    response = apis.get("users")
    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) > 0
