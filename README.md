Python Pytest Requests API Automation Framework

This project is an API Automation Testing Framework developed using Python, Pytest, and the Requests library.  
The framework is designed to perform automated Rest API validation including status code verification, response validation, and data-driven testing.

It follows scalable automation practices and can be easily extended for large API automation projects.


Tech Stack:

- Python
- Pytest
- Requests Library
- JSON
- Pytest Fixtures
- Logging
- Git

Framework Features:

- API automation using Requests library
- Pytest-based test execution
- Reusable fixtures
- Request and response validation
- Data-driven testing support
- Scalable project structure
- Easy integration with CI/CD pipelines

Project Structure:

Python-Pytest_Requests_API_Framework/
│
├── tests/                 # API test cases
├── utils/                 # Helper methods
├── data/                  # Test data files
├── reports/               # Test execution html/allure reports
├── path/                  # endpoints paths
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Project dependencies
└── README.md

Setup Instructions:

1. Clone the repository

git clone https://github.com/Vinayk-op/Python_Pytest_Requests_Framework.git

2. Navigate to project directory

cd Python-Pytest_Requests_Framework

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

Windows:
venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

Running Tests -

Run all tests: pytest

Run specific test file: pytest tests/test_users_api.py

Run tests with verbose output: pytest -v

Sample Validations Covered:

- Status code validation
- Response body validation
- JSON schema validation
- API response time validation
- Negative test scenarios

Author:

Vinay Kumar Gupta  
Senior QA Automation Engineer  
Python | Selenium | Pytest | API Automation
