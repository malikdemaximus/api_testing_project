
# 🧪 API Automation Testing Project

This is a real-world simulation project for practicing API automation using Python, Pytest, and JSON Schema validation. The purpose is to demonstrate key QA skills for job applications and interviews.

---

## 📁 Project Structure

```
.
├── tests/                      # API test cases
│   ├── test_users.py          # Tests for user-related endpoints
│   └── test_products.py       # Tests for product-related endpoints
│
├── utils/                     # Helper modules
│   ├── api_client.py          # Generic API request handler
│   └── schema_validator.py    # JSON schema validation functions
│
├── data/
│   └── schemas/               # JSON schemas for API response validation
│       ├── user_schema.json
│       └── product_schema.json
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (you are here)
```

---

## 🚀 Technologies Used

- **Python 3**
- **Pytest** – test framework
- **Requests** – HTTP library
- **JSONSchema** – for validating API response structure
- **Allure** (optional) – for generating test reports

---

## ✅ How to Run the Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pytest requests jsonschema
```

---

### 2. Run all tests

```bash
pytest tests/
```

---

### 3. (Optional) Generate Allure Report

```bash
pip install allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🧠 What You Learn

- Writing clean API test cases
- Using Pytest fixtures and structure
- Validating API responses with JSON schema
- Organizing real-life QA projects for GitHub and interviews

---

## 💼 About This Project

This project was built as part of a QA Automation learning path to simulate real working experience and build a portfolio. All tests and structures follow good practices in modern QA teams.

---

## 📬 Author

This project is maintained by a QA Automation enthusiast preparing for professional QA roles.
