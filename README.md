# E-Commerce Test Automation Framework

## Project Overview

This project is a Python-based web automation testing framework developed using Selenium WebDriver and PyTest.

The framework automates important e-commerce workflows such as user login, product search, adding products to the cart, and cart verification.

The framework follows the Page Object Model (POM) design pattern and includes reusable utilities for test data, configuration management, logging, screenshots, and HTML reporting.

---

## Technologies Used

- Python 3.11
- Selenium WebDriver
- PyTest
- Unittest
- Page Object Model (POM)
- CSV
- ConfigParser
- PyTest HTML
- Python Logging

---

## Application Under Test

Automation Exercise

https://automationexercise.com/

---

## Framework Features

- Selenium WebDriver automation
- Page Object Model
- PyTest test execution
- Unittest support
- Explicit waits
- CSV-based test data
- Configuration management
- Logging
- Automatic screenshots on test failure
- HTML test reports
- Reusable page classes
- PyTest fixtures

---

## Project Structure

```text
Wipro_Automation_Project/
│
├── config/
│   └── config.ini
│
├── data/
│   └── test_data.csv
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── logger.py
│   └── screenshot.py
│
├── tests/
│   ├── test_cart.py
│   └── test_login_unittest.py
│
├── screenshots/
├── reports/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

## Test Scenarios

### 1. Product Cart Test

The PyTest test performs:

1. Open the application
2. Login using CSV test data
3. Navigate to Products
4. Search for a product
5. Add the product to the cart
6. Open the cart
7. Verify that the product is present

### 2. Login Test

The Unittest test performs:

1. Start Chrome browser
2. Open the application
3. Read login credentials from CSV
4. Login to the application
5. Verify successful login
6. Close the browser

---

## Page Object Model

The framework separates page-specific locators and actions into individual classes.

### LoginPage

Handles:
- Opening the login page
- Entering email
- Entering password
- Clicking Login

### HomePage

Handles:
- Navigation to Products
- Waiting for the Products page

### ProductsPage

Handles:
- Product search
- Search result verification
- Adding a product to the cart

### CartPage

Handles:
- Opening the cart
- Verifying the product in the cart

---

## Test Data Management

Test data is stored separately in a CSV file.

Example:

```csv
email,password,product
example@gmail.com,password123,Dress

The CSVReader utility reads the data and passes it to the test cases.

Actual credentials should not be committed to source control.

Configuration Management

Application configuration is stored in:

config/config.ini

Example:

[DEFAULT]
base_url = https://automationexercise.com/
browser = chrome
timeout = 10

The ConfigReader utility reads these configuration values.

Logging

The framework uses Python's logging module.

Logs are stored in:

logs/automation.log

Logging records important test execution steps such as:

Starting the test
Opening the website
Login
Product search
Adding product to cart
Cart verification

Passwords are not written to the logs.

Screenshot on Failure

The framework automatically captures a screenshot whenever a PyTest test fails.

Screenshots are stored in:

screenshots/

HTML Reporting

HTML reports are generated using pytest-html.

Run:

pytest -v --html=reports/report.html --self-contained-html

The report will be generated at:

reports/report.html

Installation

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Running Tests

Run the complete PyTest suite:

pytest -v

Generate an HTML report:

pytest -v --html=reports/report.html --self-contained-html

Run the Unittest test separately:

python -m unittest tests/test_login_unittest.py -v
Framework Architecture
                 Test Cases
                     │
          ┌──────────┴──────────┐
          │                     │
        PyTest               Unittest
          │                     │
          └──────────┬──────────┘
                     │
              Page Object Model
                     │
       ┌─────────────┼─────────────┐
       │             │             │
   LoginPage    ProductsPage    CartPage
       │             │             │
       └─────────────┼─────────────┘
                     │
               Selenium WebDriver
                     │
              Automation Exercise
Key Benefits
Reusable page objects
Separation of test logic and UI locators
Externalized test data
Centralized configuration
Automatic failure screenshots
Execution logging
HTML test reporting
Support for both PyTest and Unittest
Maintainable and scalable test structure

## Test Data Management

Test data is maintained separately from test scripts using CSV files.

Example test data format:

```csv
email,password,product
example@gmail.com,example_password,Dress

Author

Shreyanka Roy

B.Tech Computer Science and Engineering (AI)