# Create Initial Data for the Database to check if the database is working properly
from app import app
from models import User, Workout, Session, Exercise, db

with app.app_context():
    # Create the database tables
    db.create_all()

    # Create initial data
    user1 = User(username='John Muchiri', 
                email='john@thisapp.com', 
                password='password')
    user2 = User(username='Ruth Onyango', 
                email = "ruth@thisapp.com", 
                password = "password")
    workout1 = Workout(name='Shoulders and Arms',
                        description='This is a workout to get bigger, more defined and powerful shoulders and arms',
                        date='2023-01-01',
                        user_id=1)
    workout2 = Workout(name='Chest and Triceps',
                        description='This is a workout to get bigger, more defined and powerful chest and triceps',
                        date='2023-01-02',
                        user_id=2)
    session1 = Session(name='MorningSession',    
                        date='2023-01-01',
                        duration=60,
                        calories_burned=500,
                        workout_id=1,
                        user_id=1)
    session2 = Session(name='Evening Session',
                        date='2023-01-02',
                        duration=45,
                        calories_burned=400,
                        workout_id=2,
                        user_id=2)   
    exercise1 = Exercise(name='Barbell Shoulder Press',
                        description='This is the first exercise',
                        sets=3,
                        reps=10,
                        steps=5,
                        user_id=1,
                        workout_id=1,
                        session_id=1)
    exercise2 = Exercise(name='Dumbbell Lateral Raise',
                        description='This is the second exercise',
                        sets=4,
                        reps=12,
                        steps=6,
                        user_id=2,
                        workout_id=2,
                        session_id=2)

    # Seed the relationships between the models
    workout1.exercises.append(exercise1)
    workout2.exercises.append(exercise2)
    session1.exercises.append(exercise1)
    session2.exercises.append(exercise2)
    db.session.add_all([user1, user2, workout1, workout2, session1, session2, exercise1, exercise2])
    db.session.commit()
