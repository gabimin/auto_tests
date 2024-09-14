# Automated Tests

This repository contains Python-based automated tests for a web application. It demonstrates the use of Selenium for web automation testing.

## Project Structure

- `test1_login.py`: This code automates the login process for the Sauce Demo application, inputs user credentials, verifies the successful login, and handles any potential errors during the process. 

- `test2_products.py`: This code automates the login process for the Sauce Demo application, verifies the successful login, retrieves the list of products from the inventory page, and handles any potential errors during the process.

- `test3_users.py`: This code automates the login process for the Sauce Demo application using a list of usernames, retrieves the inventory of products for each user, and handles potential errors.

- `test4_error_message.py`: This code automates the login process for the Sauce Demo application using a list of usernames, retrieves the inventory of products for each user, and handles potential errors. It also captures specific error messages for failed login attempts.

- `test5_prod_scr.py`: This code automates the login process for the Sauce Demo application using a list of usernames, retrieves the inventory of products for each user, and handles potential errors. It also captures product details and screenshots of each product page validating different user experiences.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Setup and Execution

1. Clone the repository.
2. Run individual test files:


```
bash
python3 test_name.py

```

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. For significant changes, please open an issue first to discuss what you would like to change.

## License
This little project is licensed under the MIT License. See the LICENSE file for details.