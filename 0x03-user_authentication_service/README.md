# User Authentication Service

This project is a user authentication service implemented in Python. It provides functionalities for user registration, login, password reset, and session management.

## Directory Structure

```
0x03-user_authentication_service/
├── app.py
├── auth.py
├── db.py
├── models.py
├── utils.py
└── README.md
```

## Files Description

- **app.py**: The main entry point of the application. It sets up the Flask application and defines the routes for user authentication.
- **auth.py**: Contains the authentication logic, including user registration, login, and password reset functionalities.
- **db.py**: Manages the database connection and provides helper functions for database operations.
- **models.py**: Defines the database models for the application, including the User model.
- **utils.py**: Contains utility functions used throughout the application, such as password hashing and token generation.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Henry4593/alx-backend-user-data.git
    cd alx-backend-user-data/0x03-user_authentication_service
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```sh
    cp .env.example .env
    ```

5. Run the application:
    ```sh
    flask run
    ```

## Usage

- **Register a new user**: Send a POST request to `/auth/register` with the user's email and password.
- **Login**: Send a POST request to `/auth/login` with the user's email and password.
- **Reset password**: Send a POST request to `/auth/reset_password` with the user's email.
- **Session management**: Use the provided endpoints to manage user sessions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.