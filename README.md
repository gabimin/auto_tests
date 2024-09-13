# Auto Tests

This repository contains automated tests for web applications using Selenium and Python. The tests cover user interactions, form submissions, and verification of page elements for consistent functionality.

## Features

- Automated login functionality.
- Verification of web elements after authentication.
- Extraction of data from dynamically generated pages.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (matching version of Chrome installed)
- Selenium

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gabimin/auto_tests.git
    ```
2. Navigate to the project directory:
    ```bash
    cd auto_tests
    ```
3. Ensure that **ChromeDriver** is installed and accessible in your system's PATH. You can download the appropriate version of ChromeDriver from [here](https://mirrors.huaweicloud.com/chromedriver//).

## Usage

To run the automated tests, use the following command:

```bash
python3 test_login.py
python3 test_products.py
```
