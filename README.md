# 🏋️ Secure Workouts API

## 📖 Project Description
The **Secure Workouts API** is a robust Flask RESTful backend designed to help users track their personal fitness routines. It allows authenticated users to securely create, read, update, and delete their workout logs. 

The API enforces strict **authorization rules**, ensuring that users can only view and modify their own private workout data. It features secure password hashing, JWT authentication, data validation via Marshmallow, and pagination for efficient data retrieval.

## 🛠️ Tech Stack
- **Backend Framework:** Flask
- **Database ORM:** SQLAlchemy & Flask-Migrate
- **Serialization/Validation:** Marshmallow
- **Security:** Flask-Bcrypt (Password Hashing), JWT (Authentication)
- **Testing:** Postman

---

## 🚀 Installation Instructions

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone [YOUR_GITHUB_REPO_URL_HERE]
cd [YOUR_PROJECT_FOLDER_NAME]

#
. Set Up the Virtual Environment
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# install dependences

Install Dependencies

# Set Up the Environment Variables
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=[your_super_secret_key]
JWT_SECRET_KEY=[your_jwt_secret_key]
# Initialize and Run Migrations
# Initialize migrations (only needed once)
flask --app app db init

# Create the migration script
flask --app app db migrate -m "create users and workouts tables"

# Apply the migrations to the database
flask --app app db upgrade
# Seed the Database (Optional)
python seed.py
# To start the Flask development server
flask --app app run --debug
or
python3 app.py
 *The API will be live at http://127.0.0.1:5555 (or the port specified in your configuration)*.
#  API Endpoints and Authentication 
Method      Endpoint       Description
post         /register     register a new user. Requires username and password.
POST        /login         Log in an existing user. Returns a JWT access token.

# Workouts (Protected Routes)
Method         Endpoint        Description
GET            /workouts       Get the logged-in user's workouts. Supports pagination (page=1).POST          /workouts        Create a new workout log.
PATCH         /workouts/<id>   Update an existing workout (only if owned by the user).
DELETE        /workouts/<id>   Delete a workout (only if owned by the user).


# Request/Response Examples
Create a Workout (POST /workouts)
Request Body:
{
  "workout_type": "Cardio",
  "duration_minutes": 45,
  "calories_burned": 400,
  "notes": "Felt great today!",
  "date": "2026-09-11"
}


# Get Paginated Workouts (GET /workouts?page=1)
Response:
{
  "workouts": [
    {
      "id": 1,
      "workout_type": "Cardio",
      "duration_minutes": 45,
      "calories_burned": 400,
      "notes": "Felt great today!",
      "date": "2026-09-11",
      "user_id": 1
    }
  ],
  "total_pages": 2,
  "current_page": 1
}

# 🧪 Testing
 User registration and login flows.
CRUD operations for workouts.
Authorization checks: Verified that User A cannot view, update, or delete User B's workouts. Validation checks: Verified that invalid data (e.g., negative duration) returns a 400 Bad Request.
 Pagination: Verified that creating 15+ records correctly splits them across multiple pages.

# Contributors
Group 5
Student 1: Models & Database
Student 2: Authentication & Security
Student 3: Resource CRUD & Pagination
Student 4: Schemas, Testing & Documentation

# ##





















How your teammates will use your work:
Serialization (dump): When Student 3 fetches a workout from the database, they will use workout_schema.dump(workout) to convert the SQLAlchemy object into a JSON-friendly dictionary for the API response.
Deserialization (load): When a user sends a POST/PATCH request, Student 3 will use workout_schema.load(request.json) to validate the incoming data and convert it into a Python dictionary to create the database record.
2. Postman Testing Strategy
You are responsible for proving the API works. Create a Postman Collection with the following structure and test scenarios.
Setup Environment Variables in Postman:
base_url: http://127.0.0.1:5555 (or whatever port your group uses)
token_user1: (Save this after logging in as User 1)
token_user2: (Save this after logging in as User 2)
Test Scenarios to Execute & Document:
Authentication Flow:
POST /register: Create User 1 and User 2. Check for 201 Created.
POST /login: Log in as both users. Extract the JWT/Session tokens and save them to your Postman variables.
CRUD & Ownership (Authorization):
POST /workouts: Create a workout using User 1's token. Note the id of the created workout.
GET /workouts: Use User 1's token. Verify you only see User 1's workouts.
Crucial Test: Try to PATCH /workouts/<user1_workout_id> using User 2's token. It must return 403 Forbidden or 404 Not Found (depending on how Student 3 implements it) to prove authorization works.
Validation:
POST /workouts: Send a request with duration_minutes: -5 or an invalid workout_type. Verify it returns 400 Bad Request with your custom error messages.
Pagination:
Create at least 15 workouts using User 1.
GET /workouts?page=1 -> Verify it returns a subset (e.g., 10 items).
GET /workouts?page=2 -> Verify it returns the remaining items.



# Secure Workouts API

## Project Description
The Secure Workouts API is a robust Flask RESTful backend designed to help users track their personal fitness routines. It allows authenticated users to securely create, read, update, and delete their workout logs. The API enforces strict authorization rules, ensuring users can only access and modify their own private workout data. It also features data validation, pagination, and secure password hashing.

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd secure-workouts-api


   Create and activate a virtual environment
      python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate



   Install dependencies
      pip install -r requirements.txt




      Set up the environment:
Create a .env file in the root directory and add your secret keys:
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   JWT_SECRET_KEY=your_jwt_secret_key




   Run database migrations
   flask --app app db upgrade



   Seed the database (Optional)
   python seed.py




   Run Instructions
To start the Flask development server, run:
flask --app app run --debug



The API will be available at http://127.0.0.1:5555.
API Endpoints
Authentication


Method
Endpoint
Purpose
POST
/register
Register a new user (requires username, password).
POST
/login
Log in an existing user. Returns a JWT token.




Workouts (Protected Routes)
Note: All workout endpoints require a valid JWT token in the Authorization: Bearer <token> header.


Method
Endpoint
Purpose
GET
/workouts
Get the logged-in user's workouts. Supports pagination (?page=1).
POST
/workouts
Create a new workout log.
PATCH
/workouts/<id>
Update an existing workout (only if owned by the user).
DELETE
/workouts/<id>
Delete a workout (only if owned by the use


{
  "workout_type": "Cardio",
  "duration_minutes": 45,
  "calories_burned": 400,
  "notes": "Felt great today!",
  "date": "2026-09-11"
}





---

### 4. Git & Collaboration Advice for Student 4

Since you are working in a group, here is how you should manage your Git workflow to ensure clean commit history:

1.  **Create your feature branch:**
    ```bash
    git checkout main
    git pull origin main
    git checkout -b feature/schemas-testing
    ```
2.  **Make meaningful commits as you work:**
    Don't wait until Friday to commit. As you finish parts of your work, commit them:
    *   `git add schemas.py` -> `git commit -m "Add Marshmallow schemas for User and Workout with validation"`
    *   `git add Postman_Collection.json` -> `git commit -m "Add Postman collection for API and authorization testing"`
    *   `git add README.md` -> `git commit -m "Write comprehensive README and endpoint documentation"`
3.  **Push and Merge:**
    ```bash
    git push origin feature/schemas-testing
    ```
    Then, ask a teammate to review your code on GitHub and merge it into `main`. Once merged, pull the latest main so you have everyone else's work (Models, Auth, CRUD) to do your final integration testing!

### Final Checklist for Your Role:
- [ ] Are `dump()` and `load()` clearly understood and utilized by the CRUD routes?
- [ ] Did you test with **at least two different users** in Postman to prove authorization works?
- [ ] Did you test **pagination** with enough records to prove multiple pages work?
- [ ] Is the README fully populated and formatted correctly?
- [ ] Did you remove any debug `print()` statements or commented-out code before your final push?

Good luck to Group 4! Let me know if you need help tweaking the schemas or writing specific Postman test scripts.



git add .
git commit -m "Added workout schemas and README"
git push origin feature/schemas-and-docs

git checkout main
git pull origin main