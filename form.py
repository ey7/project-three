from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

#  class for registration form
class UsernamePasswordConfirm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(),
                           Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#class for login form
class UsernamePassword(FlaskForm):

    username = StringField('Username', validators=[DataRequired(),
                           Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')