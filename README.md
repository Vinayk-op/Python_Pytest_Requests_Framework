# Python Pytest Requests API Automation Framework

This project is a **REST API Automation Testing Framework** developed using **Python, Pytest, and the Requests library**. The framework is designed to perform automated API validation including status code verification, response validation, schema validation, and data-driven testing.

The framework follows scalable automation practices and is designed to support **CI/CD-based execution for regression and scheduled test runs**, making it suitable for real-world API automation projects.

---

## 🚀 Tech Stack

* Python
* Pytest
* Requests Library
* JSON
* Pytest Fixtures
* Logging
* Git
* GitHub Actions (CI/CD)

---

## ✅ Framework Features

* API automation using Requests library
* Pytest-based test execution
* Reusable fixtures and utilities
* Request and response validation
* Data-driven testing support
* JSON schema validation
* API response time validation
* Negative test scenario coverage
* Scalable project structure
* CI/CD ready automation framework

---

## ⚙️ CI/CD Integration

The framework is integrated with **GitHub Actions** to enable automated regression execution.

Automation pipeline triggers:

* Execution on Pull Requests
* Execution on Code Push
* Scheduled execution for nightly regression runs

This ensures continuous API validation and early defect detection during development cycles.

---

## 📂 Project Structure

```
Python-Pytest_Requests_API_Framework/
│
├── tests/                 # API test cases
├── utils/                 # Helper methods
├── data/                  # Test data files
├── reports/               # Test execution reports
├── path/                  # API endpoint paths
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Project dependencies
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Vinayk-op/Python_Pytest_Requests_Framework.git
```

### 2. Navigate to project directory

```
cd Python-Pytest_Requests_Framework
```

### 3. Create virtual environment

```
python -m venv venv
```

### 4. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```
pytest
```

Run specific test file:

```
pytest tests/test_users_api.py
```

Run tests with verbose output:

```
pytest -v
```

---

## ✅ Sample Validations Covered

* Status code validation
* Response body validation
* JSON schema validation
* API response time validation
* Negative test scenarios

---

## 👨‍💻 Author

**Vinay Kumar Gupta**
Senior QA Automation Engineer
Python | Selenium | Pytest | API Automation
