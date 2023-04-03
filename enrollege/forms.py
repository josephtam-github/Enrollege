from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from enrollege.models import Users
import re


class RegisterForm(FlaskForm):
    def validate_username(self, user_name_to_check):
        user = Users.query.filter_by(username=user_name_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        elif re.findall('\W', user_name_to_check.data):
            raise ValidationError('Username must have only characters from a-Z, digits from 0-9, and underscore (_)')

    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_firstname(self, first_name_to_check):
        if re.findall('\W', first_name_to_check.data):
            raise ValidationError('Firstname must have only characters from a-Z, digits from 0-9, and underscore (_)')

    def validate_lastname(self, last_name_to_check):
        if re.findall('\W', last_name_to_check.data):
            raise ValidationError('Lastname must have only characters from a-Z, digits from 0-9, and underscore (_)')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    firstname = StringField(label='Firstname:', validators=[Length(min=2, max=30), DataRequired()])
    lastname = StringField(label='Lastname:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confpassword = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Submit')
