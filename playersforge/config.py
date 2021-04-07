from flask import Flask
from flask_wtf.csrf import CSRFProtect

# starting the app
app = Flask(__name__)
CSRFProtect(app)

# secret key to make some stuff work
app.config['SECRET_KEY'] = 'hardsecretkey'

# connects the app to the playersforge database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://playersforge:password@localhost/playersforge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
