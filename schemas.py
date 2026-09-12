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
# NOTE: fields here match the actual Workout model in models.py
# (name, description, date, user_id) — NOT the earlier draft schema,
# which referenced fields (workout_type, duration_minutes, calories_burned)
# that don't exist on the model. Keeping the model as the source of truth
# avoids a mid-week migration that would affect Session/Exercise too.
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=80, error="Name is required and must be under 80 characters.")
    )
    description = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=200, error="Description is required and must be under 200 characters.")
    )
    # Stored as a plain string in the model (not a Date column), so we
    # validate it as a string but still enforce YYYY-MM-DD format.
    date = fields.Str(
        required=True,
        validate=validate.Regexp(
            r"^\d{4}-\d{2}-\d{2}$",
            error="Date must be in YYYY-MM-DD format."
        )
    )

    # user_id is dump_only because the backend assigns it based on the
    # logged-in user (from the JWT), never from client input.
    user_id = fields.Int(dump_only=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)  # Used for returning lists (pagination)