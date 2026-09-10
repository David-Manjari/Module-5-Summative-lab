# Create Initial Data for the Database to check if the database is working properly
from app import app
from models import User, Workout, Session, Exercise, db

with app.app_context():
    # Create the database tables
    db.create_all()

    # Create initial data
    user1 = User(username='john_doe', 
                email='john@example.com', 
                password='password')
    user2 = User(username='jane_doe', 
                email = "jane@example.com", 
                password = "password")
    workout1 = Workout(name='Workout 1',
                        description='This is the first workout',
                        date='2023-01-01',
                        user_id=1)
    workout2 = Workout(name='Workout 2',
                        description='This is the second workout',
                        date='2023-01-02',
                        user_id=2)
    session1 = Session(date='2023-01-01',
                        duration=60,
                        calories_burned=500,
                        workout_id=1)
    session2 = Session(date='2023-01-02',
                        duration=45,
                        calories_burned=400,
                        workout_id=2)   
    exercise1 = Exercise(name='Exercise 1',
                        description='This is the first exercise',
                        sets=3,
                        reps=10,
                        user_id=1,
                        workout_id=1,
                        session_id=1)
    exercise2 = Exercise(name='Exercise 2',
                        description='This is the second exercise',
                        sets=4,
                        reps=12,
                        user_id=2,
                        workout_id=2,
                        session_id=2)
    db.session.add_all([user1, user2, workout1, workout2, session1, session2, exercise1, exercise2])
    db.session.commit()
