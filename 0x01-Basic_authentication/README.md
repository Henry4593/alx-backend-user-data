# Basic Authentication

## Overview
This repository contains the implementation of basic authentication for a web application.
The goal is to provide a simple and secure way to authenticate users.

## Features
-Basic Authenthication

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Henry4593/alx-backend-user-data.git
    ```
2. Navigate to the project directory:
    ```bash
    cd alx-backend-user-data/0x01-Basic_authentication
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the server:
    ```bash
    API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```
2. Access the application at `http://localhost:5000`.

## API Endpoints
- `GET /api/v1/unauthorized`:
- `GET /api/v1/forbidden`:
- `GET /api/v1/users`:
- `GET /api/v1/status/`: 

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)
