from flask_sqlalchemy import SQLAlchemy
from config import app

# connect to the database
db = SQLAlchemy(app)

# Users database model that carries an id (automatically increments in database),
# email, username, and password
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
