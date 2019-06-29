from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# custom validation function
def email_exiists(form, field):

    email = User.query.filter_by(user_email = field.data).first()

    if email:
        raise ValidationError(message='Email Already Exists')



class RegistrationForm(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired(), Length(3, 30, message='your name must be between 3 to 30 characters')])
    email = StringField('Enter Email Address', validators=[DataRequired(), Email(), email_exiists])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    stay_logged_in = BooleanField('Stay Logged-in')
    submit = SubmitField('Login')