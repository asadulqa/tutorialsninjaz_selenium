

# Tutorialsninja.com/demo Automation Testing 

This repository contains a **Selenium** test automation framework using **Python** and **Behave** for BDD (Behavior Driven Development). The framework is designed to automate the testing of web applications using Selenium WebDriver and follows the Page Object Model (POM) design pattern.

## Features
- **Behavior Driven Development (BDD)** with Behave framework.
- **Selenium WebDriver** integration for browser automation.
- **Page Object Model (POM)** to improve test maintainability.
- **Random data generation** utilities for dynamic testing.
- Supports cross-browser testing.

## Project Structure

### Requirements

To run this framework, you need the following:

- Python 3.x
- Chrome WebDriver (or any other browser driver)
- Selenium (`selenium`)
- Behave (`behave`)

#### You can install all the dependencies by running:


``pip install -r requirements.txt``

### Run Test 
``behave -D headless=true -f allure_behave.formatter:AllureFormatter -o reports``
