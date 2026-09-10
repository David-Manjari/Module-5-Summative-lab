# Create Initial Data for the Database to check if the database is working properly
from app import app
from models import User, Workout, Session, Exercise, db

with app.app_context():
