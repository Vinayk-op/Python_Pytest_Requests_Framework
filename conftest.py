import pytest
from datetime import datetime
import json
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("starting setup")
    yield
    print("starting teardown")

@pytest.fixture
def get_test_data():
    json_data = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    with open(json_data) as json_file:
        data = json.load(json_file)
    return data
