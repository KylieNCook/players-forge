from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm # imports the RegisterForm and its data
from models import db, Users # imports db and Users model
from config import app

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

# profile page (currently renders to homepage)
@app.route('/profile')
def profile():
    return render_template('index.html')

# signup page
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    
    # load in RegisterForm with exisitng data to variable form
    form = RegisterForm()

    # check if information submitted is valid
    if form.validate_on_submit():

        # take data from form and set into variables
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # create a new user with data given
        new_register = Users(email=email, username=username, password=password) 

        # add the user into the database
        db.session.add(new_register)

        # commit the user into the database
        db.session.commit()

        # redirect to the homepage
        return redirect(url_for('index'))
    
    # render signup page
    return render_template('signup.html', form=form)
