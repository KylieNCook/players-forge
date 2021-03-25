from flask import Flask

# starting the app
app = Flask(__name__)

# secret key to make some stuff work
app.config['SECRET_KEY'] = 'hardsecretkey'

# connects the app to the playersforge database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://playersforge:password@localhost/playersforge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
