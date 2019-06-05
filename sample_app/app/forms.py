from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from app.models import Writing

class WriteForm(FlaskForm):
   author = StringField('Author', validators=[DataRequired()])
   text = TextAreaField('Writing', validators=[DataRequired()])
   submit = SubmitField('Submit')


