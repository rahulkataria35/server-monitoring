# Server Monitoring

Using `Python` and `Docker` with a combination of libraries like `psutil` for monitoring system resources, `Flask` for the web server, and `psycopg2` for data storage, you can create an efficient and scalable monitoring and alerting system.

This is a Server Monitoring application built with Flask, designed to monitor server metrics such as CPU usage, memory usage, and disk usage. Alerts are generated based on the thresholds and sent via email.

## Features

- Real-time monitoring of server metrics.
- Threshold-based alert generation.
- Alerts sent via email with detailed metrics.
- Configurable monitoring intervals and thresholds.
- Dockerized for easy deployment.
- Uses Gunicorn for production-ready server deployment.

## Project Structure



```
SERVER-MONITORING/
├── app/
│ ├── init.py # Application factory
│ ├── alerting.py # Alert generation logic
│ ├── db.py # Database interactions
│ ├── monitoring.py # Monitoring logic
│ ├── routes.py # Flask routes
│ ├── templates/
│ └── alert.html # HTML template for alert emails
├── .env # Environment variables
├── .gitignore # Git ignore file
├── config.py # Configuration settings
├── docker-compose.yml # Docker Compose configuration
├── Dockerfile # Dockerfile for building the image
├── loadEnv.ps1 # PowerShell script for loading environment variables
├── main.py # Entry point for the application
├── README.md # This README file
├── requirements.txt # Python dependencies

```


## Installation

### Prerequisites
- Docker
- Docker Compose
- Python 3.9

### Steps

1. **Clone the repository:**
    ```
    git clone https://github.com/rahulkataria35/server-monitoring.git
    cd server-monitoring
    ```

2. **Build and run the Docker containers:**
    ```
    docker-compose up --build
    ```

3. **Environment Variables:**
    - Ensure that you have a `.env` file in the root directory with the required environment variables. Example:
        ```
        # System thresholds
        CPU_THRESHOLD=85
        MEMORY_THRESHOLD=85
        DISK_THRESHOLD=85
       
        # SMTP settings
        SMTP_SERVER=smtp.gmail.com
        SMTP_PORT=587
        EMAIL_FROM=encoded_credentials
        EMAIL_TO=recipient@example.com
        STARTUP_MAIL_CC=cc@example.com

        # Database settings
        DB_NAME=monitoring
        DB_USER=postgres
        DB_PASSWORD=password
        DB_HOST=db
        DB_PORT=5432

        ```

## Generating Credentials

To generate credentials for the SMTP settings, you can encode your email and password in Base64 format. Here is how you can do it in Python:

```

import base64
import json

credentials = {
    "email": "your_email@gmail.com",
    "password": "your_password"
}

# Convert the credentials dictionary to a JSON string
credentials_json = json.dumps(credentials)

# Encode the JSON string in Base64
encoded_credentials = base64.b64encode(credentials_json.encode()).decode()

print(encoded_credentials)

```

- Replace "your_email@gmail.com" and "your_password" with your actual email and password. The output will be a Base64-encoded   string that you can use in your .env file.


## Usage

Once the Docker containers are running, the Flask app will be accessible at `http://localhost:5000`.

### Running in Development Mode

To run the application locally without Docker, you can use the following steps:

1. **Create a virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```
    python main.py
    ```

### Using Gunicorn for Production

If you prefer to run the application using Gunicorn without Docker, you can use the following command:

```bash
- gunicorn -w 4 -b 0.0.0.0:5000 main:app



#Configuration
- `config.py:` Contains configuration settings for different environments (development, testing, production).
- `.env`: Store environment-specific variables here.

# Contributing
Contributions are welcome! Please create an issue or pull request if you have any improvements or new features to propose.
