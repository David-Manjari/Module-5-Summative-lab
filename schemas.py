# schemas.py
from marshmallow import Schema, fields, validate, validates, ValidationError

# --- User Schemas ---
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True, 
        validate=validate.Length(min=3, max=50, error="Username must be between 3 and 50 characters.")
    )
    # Password is load_only so it is never sent back in API responses
    password = fields.Str(
        required=True, 
        load_only=True, 
        validate=validate.Length(min=6, error="Password must be at least 6 characters.")
    )

user_schema = UserSchema()

# --- Workout Schemas ---
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    
    # 3+ Meaningful fields for Workouts
    workout_type = fields.Str(
        required=True, 
        validate=validate.OneOf(
            ["Cardio", "Strength", "Flexibility", "Sports", "HIIT"], 
            error="Invalid workout type. Choose from: Cardio, Strength, Flexibility, Sports, HIIT."
        )
    )
    duration_minutes = fields.Int(
        required=True, 
        validate=validate.Range(min=1, error="Duration must be at least 1 minute.")
    )
    calories_burned = fields.Int(
        validate=validate.Range(min=0, error="Calories cannot be negative.")
    )
    notes = fields.Str()
    date = fields.Date(required=True)
    
    # user_id is dump_only because the backend assigns it based on the logged-in user
    user_id = fields.Int(dump_only=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True) # Used for returning lists (pagination)