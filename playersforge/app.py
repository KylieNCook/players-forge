from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm, LoginForm # imports RegisterFrom and LoginForm
from models import db, Users # imports db, Users models
from config import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, logout_user, login_user, login_required, current_user

# homepage
@app.route('/')
def index():
    return render_template('index.html')

# mods page
@app.route('/mods')
def mods():
    return render_template('mods.html')

# forums page
@app.route('/forums')
def forums():
    return render_template('forums.html')

# profile page
@app.route('/profile')
# user has to be logged in to have this page show up
@login_required
def profile():

    # renders sign up page
    return render_template('profile.html')

# logout page
@app.route('/logout')
# user has to be logged in to have this page show up
@login_required
def logout():

    # logs user out
    logout_user()

    # redirects to homepage
    return redirect(url_for('index'))

# login page
@app.route('/login', methods = ['GET', 'POST'])
def login():

    # load in LoginForm with exisitng data to variable form
    form = LoginForm()
    error = None

    # check if information submitted is valid
    if form.validate_on_submit():

        # take data from form and set into variables
        email = form.email.data
        password = form.password.data 

        # find the user data given
        user = Users.query.filter_by(email=email, password=password).first()

        # if the use data is found, login and move to profile
        if user:
            login_user(user)
            return redirect(url_for('profile'))
        
        error = "I can't find those credentials"

    return render_template('login.html', form=form, error=error)

# signup page
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    
    # load in RegisterForm with exisitng data to variable form
    form = SignUpForm()

    # check if information submitted is valid
    if form.validate_on_submit():

        # take data from form and set into variables
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # create a new user with data given
        new_user = Users(email=email, username=username, password=password) 

        # add the user into the database
        db.session.add(new_user)

        # commit the user into the database
        db.session.commit()

        # logs in new user
        login_user(new_user)

        # redirect to the homepage
        return redirect(url_for('profile'))
    
    # render signup page
    return render_template('signup.html', form=form)
