from flask import Flask,request, jsonify,  session
from  models import db, User, Workout, Session, Exercise

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SECRET_KEY"] = "mysecretkey"
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)