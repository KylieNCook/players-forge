from flask import Flask, render_template, flash, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm, LoginForm, UploadForm # imports RegisterFrom, LoginForm, and UploadForm
from models import db, Users, Mods # imports db, Users models
from config import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, logout_user, login_user, login_required, current_user
import os

# homepage
@app.route('/')
def index():
    mods = Mods.query.all()
    featured = []

    for mod in mods:
        featured.append(mod)

    return render_template('index.html', featured=featured)

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

    mods = Mods.query.all()
    user_mods = []

    for mod in mods:
        if mod.username == current_user.username:
            user_mods.append(mod)

    # renders sign up page
    return render_template('profile.html', user_mods=user_mods)

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
    
    # load in SignUpForm with exisitng data to variable form
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

# mod uploading page (testing)
@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    
    # load in UploadForm with existing data to variable form
    form = UploadForm()

    # check if information submitted is valid
    if form.validate_on_submit():

        # take data from form/file and set into variables
        name = form.name.data
        description = form.description.data
        game = form.game.data
        file = request.files['inputFile']
        image = request.files['imageFile']

        # create a new mod with the given data and add it to the database
        
        new_mod = Mods(user_id=current_user.id, username=current_user.username, 
        game=game, name=name, description=description, data= 'uploads/' + file.filename, image='uploads/' + image.filename)

        db.session.add(new_mod)

        db.session.commit()

        file.save(os.path.join("static/uploads", file.filename))
        image.save(os.path.join("static/uploads", image.filename))

        return render_template('upload.html', form=form)

    return render_template('upload.html', form=form)

