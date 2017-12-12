# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationFrom(FlaskForm):

    """ 
    Form for user registration/account creation
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            return ValidationError('Username already in use')

class LoginForm(FlaskForm):

    """ 
    Form for user login
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')