from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# form used in signup.html to gather information given by user
# also used in app.py/signup to transfer data into app.py variables
class SignUpForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

# form used in signup.html to gather information given by user
# also used in app.py/signup to transfer data into app.py variables
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    