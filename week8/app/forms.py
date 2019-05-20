from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Register')

   # The validate_{field name} methods get called automatically when validate_on_submit is called on the form
   # That method looks for any class methods with the prefix validate and then a field name
   # It calls all of those for validation.
   def validate_username(self, username):
      user = User.query.filter_by(username=username.data).first()
      if user is not None:
         raise ValidationError('Please use a different username.')
   
   def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user is not None:
         raise ValidationError('Please use a different email address.')
      
   
class PostForm(FlaskForm):
   post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
   submit = SubmitField('Submit')
