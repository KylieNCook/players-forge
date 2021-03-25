from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_user, logout_user
from forms import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://playersforge:password@localhost/playersforge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

def create_app(config=None):
    login_manager.init_app(app)
    return app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mods')
def mods():
    return render_template('mods.html')

@app.route('/forums')
def forums():
    return render_template('forums.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        new_register = Users(email=email, username=username, password=password) 
        db.session.add(new_register)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)