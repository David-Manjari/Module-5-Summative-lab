# Secure Workouts API

This project is a demonstration of a secure RESTful API built with Flask for managing personal workout records. The application allows authenticated users to create, view, update, and delete their workout data while ensuring that users can only access and modify their own records.

## Project Overview

### Problem

The application addresses the need for a secure system where users can record and manage their personal workout routines.

The API provides authenticated users with the ability to:

- Register an account
- Log in securely
- Create workout records
- View their workout records
- Edit their workout records
- Delete their workout records
- Retrieve workout records using pagination

The application uses JWT authentication and authorization to ensure that private workout data can only be accessed by the user who owns it.

## Features

- User registration
- User login and authentication
- Password hashing
- JWT-based authentication
- Create workout records
- View workout records
- Edit workout records
- Delete workout records
- User-specific authorization
- Workout data validation
- Pagination for workout records
- Database migrations
- API testing using Postman

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- Flask-Bcrypt
- JWT Authentication
- SQLite
- Postman
- Git & GitHub

## Project Structure

Secure-Workouts-API/

    * app.py
    * models.py
    * schemas.py
    * seed.py
    * requirements.txt
    * README.md
    * migrations/
    * instance/

## Installation

### 1. Clone the Repository

    git clone [GitHub Repository URL]
    cd Secure-Workouts-API

### 2. Create a Virtual Environment

    python -m venv venv

### 3. Activate the Virtual Environment

Windows:

    venv\Scripts\activate

Linux/macOS:

    source venv/bin/activate

### 4. Install Dependencies

    pip install -r requirements.txt

### 5. Set Up Environment Variables

Create the required environment variables for the application.

    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_super_secret_key
    JWT_SECRET_KEY=your_jwt_secret_key

Replace the example secret keys with secure values when setting up the application.

### 6. Initialize the Database

Initialize Flask-Migrate:

    flask --app app db init

Create the migration:

    flask --app app db migrate -m "create users and workouts tables"

Apply the migration:

    flask --app app db upgrade

### 7. Seed the Database

If sample data is required, run:

    python seed.py

## Running the Application

After installing the dependencies and setting up the database, start the Flask development server using:

    flask --app app run --debug

Or:

    python3 app.py

The API will be available at:

    http://127.0.0.1:5555

The port may differ depending on the application's configuration.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | /register | Register a new user using a username and password |
| POST | /login | Log in an existing user and receive a JWT access token |

### Workouts

The workout endpoints are protected and require a valid JWT access token.

| Method | Endpoint | Description |
|---|---|---|
| GET | /workouts | Get the logged-in user's workouts |
| POST | /workouts | Create a new workout record |
| PATCH | /workouts/<id> | Update an existing workout owned by the user |
| DELETE | /workouts/<id> | Delete a workout owned by the user |

### Pagination

The workouts endpoint supports pagination using the `page` query parameter.

Example:

    GET /workouts?page=1

This allows workout records to be retrieved in smaller sets rather than returning all records at once.

## Authentication and Authorization

The API uses JWT authentication to protect private workout data.

After successfully logging in, the user receives a JWT access token. The token must be included when accessing protected workout endpoints.

Authorization ensures that a user can only view, update, or delete workouts belonging to their own account.

## Testing

The API can be tested using Postman.

Testing includes:

- User registration
- User login
- JWT authentication
- Creating workouts
- Retrieving workouts
- Updating workouts
- Deleting workouts
- Testing authorization between different users
- Testing pagination
- Testing validation errors

## Future Improvements

- Add workout categories
- Add exercise tracking
- Add workout statistics
- Add progress tracking
- Add user profiles
- Add workout history and analytics
- Add automated API testing
- Deploy the API to a production server

## License

This project is licensed under the MIT License.

## Contributors

Group 5

- DAVID MANJARI: Models & Database
- SONIA NGARUIYA: Authentication & Security
- TREVOR KAMANGUYA: Resource CRUD & Pagination
- OKETCH ODHIAMBO: Schemas, Testing & Documentation
