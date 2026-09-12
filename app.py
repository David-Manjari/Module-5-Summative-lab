from flask import Flask, request, jsonify
from models import db, User, Workout, Session, Exercise, bcrypt
from schemas import user_schema, workout_schema, workouts_schema
from marshmallow import ValidationError
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "dev-jwt-secret-key-change-in-production")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "username, email, and password are required"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already taken"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "user": {"id": user.id, "username": user.username, "email": user.email},
        "access_token": access_token
    }), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "username and password are required"}), 400

    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "user": {"id": user.id, "username": user.username, "email": user.email},
        "access_token": access_token
    }), 200


# ---------------------------------------------------------------------------
# Workout CRUD (Student 3 responsibility)
# All routes are protected with @jwt_required() and scoped to the logged-in
# user via get_jwt_identity() — a user can only ever see/change their own
# workouts, never anyone else's.
# ---------------------------------------------------------------------------

@app.route('/workouts', methods=['GET'])
@jwt_required()
def get_workouts():
    """Return the logged-in user's workouts, paginated."""
    user_id = int(get_jwt_identity())

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if page < 1:
        return jsonify({"error": "page must be 1 or greater"}), 400
    if per_page < 1 or per_page > 100:
        return jsonify({"error": "per_page must be between 1 and 100"}), 400

    pagination = Workout.query.filter_by(user_id=user_id).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        "workouts": workouts_schema.dump(pagination.items),
        "pagination": {
            "total_items": pagination.total,
            "total_pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev
        }
    }), 200


@app.route('/workouts', methods=['POST'])
@jwt_required()
def create_workout():
    """Create a new workout owned by the logged-in user."""
    user_id = int(get_jwt_identity())
    json_data = request.get_json()

    if not json_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        data = workout_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    if Workout.query.filter_by(name=data['name']).first():
        return jsonify({"error": "A workout with this name already exists"}), 400

    workout = Workout(
        name=data['name'],
        description=data['description'],
        date=data['date'],
        user_id=user_id
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 201


@app.route('/workouts/<int:workout_id>', methods=['PATCH'])
@jwt_required()
def update_workout(workout_id):
    """Update a workout, but only if it belongs to the logged-in user."""
    user_id = int(get_jwt_identity())
    workout = Workout.query.get(workout_id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    if workout.user_id != user_id:
        return jsonify({"error": "You do not have permission to update this workout"}), 403

    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        data = workout_schema.load(json_data, partial=True)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    if 'name' in data and data['name'] != workout.name:
        if Workout.query.filter_by(name=data['name']).first():
            return jsonify({"error": "A workout with this name already exists"}), 400
        workout.name = data['name']

    if 'description' in data:
        workout.description = data['description']

    if 'date' in data:
        workout.date = data['date']

    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 200


@app.route('/workouts/<int:workout_id>', methods=['DELETE'])
@jwt_required()
def delete_workout(workout_id):
    """Delete a workout, but only if it belongs to the logged-in user."""
    user_id = int(get_jwt_identity())
    workout = Workout.query.get(workout_id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    if workout.user_id != user_id:
        return jsonify({"error": "You do not have permission to delete this workout"}), 403

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
