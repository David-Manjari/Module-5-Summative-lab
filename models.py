# Import the libraries for this project 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData



convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

user_workout = db.Table('user_workout',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('workout_id', db.Integer, db.ForeignKey('workouts.id'), primary_key=True),
    db.Column('session_id', db.Integer, db.ForeignKey('sessions.id'), primary_key=True)
)
class BaseModel:
    """Base model class that other models will inherit from."""
    id = Column(Integer, primary_key=True)



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
    user = db.relationship('User', back_populates='workouts')
    sessions = db.relationship('Session', back_populates='workout')
    exercises = db.relationship('Exercise', back_populates='workout')

    def __repr__(self):
        return f'<Workout {self.name}>'

class Session(BaseModel, db.Model):
    __tablename__ = 'sessions'
    name = Column(String(80), unique=True, nullable=False)
    date = Column(String(80), nullable=False)
    duration = Column(Integer, nullable=False)
    calories_burned = Column(Integer, nullable=False)

    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # create the relationship between the Session User, workout and Exercise models
    user = db.relationship('User', back_populates='sessions')
    workout = db.relationship('Workout', back_populates='sessions')
    exercises = db.relationship('Exercise', back_populates='sessions')

    def __repr__(self):
        return f'<Session {self.date}>'

class Exercise(BaseModel, db.Model):
    __tablename__ = 'exercises'
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)

    # create the relationship between the Exercise User, workout and session models
    user = db.relationship('User', back_populates='exercises')
    workout = db.relationship('Workout', back_populates='exercises')    
    sessions = db.relationship('Session', back_populates='exercises')

    def __repr__(self):
        return f'<Exercise {self.name}>'

