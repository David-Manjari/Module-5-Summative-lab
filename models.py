# Import the libraries for this project 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,sessionmaker

DATABASE_URI = 'sqlite:///instance/app.db'

engine = create_engine(DATABASE_URI)

class BaseModel:
    """Base model class that other models will inherit from."""
    id = Column(Integer, primary_key=True)

session = sessionmaker(bind=engine)()


# My models will be defined here
class User(BaseModel, db.Model):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    # create the relationship between the User Workout, session, and exercise models
    workouts = db.relationship('Workout', back_populates='user')
    sessions = db.relationship('Session', back_populates='user')
    exercises = db.relationship('Exercise', back_populates='user')
    def __repr__(self):

        return f'<User {self.username}>'

class Workout(BaseModel, db.Model):
    __tablename__ = 'workouts'
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    date = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    #  create the relationship between the Workout and Exercise models

    sessions = db.relationship('Session', back_populates='workout')
    exercises = db.relationship('Exercise', back_populates='workout')

    def __repr__(self):
        return f'<Workout {self.name}>''

class Session(BaseModel, db.Model):
    __tablename__ = 'sessions'
    date = Column(String(80), nullable=False)
    duration = Column(Integer, nullable=False)
    calories_burned = Column(Integer, nullable=False)

    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # create the relationship between the Session User, workout and Exercise models
    exercise = db.relationship('Exercise', back_populates='sessions')

    def __repr__(self):
        return f'<Session {self.date}>'

class Exercise(BaseModel, db.Model):
    __tablename__ = 'exercises'
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)

    def __repr__(self):
        return f'<Exercise {self.name}>'

