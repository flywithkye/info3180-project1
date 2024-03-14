from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, ValidationError

def isint_check(form, field):
    if isinstance(field.data, int):
        raise ValidationError('Must be in integer')
    
class PropertyForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    title = StringField('Title', validators=[InputRequired()])
    num_bedrooms = StringField('No. of Bedrooms', validators=[InputRequired(), isint_check])
    num_bathrooms = StringField('No. of Bathrooms', validators=[InputRequired(), isint_check])
    location = StringField('Location', validators=[InputRequired()]) 
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', choices=['House', 'Apartment']) 
    description = StringField('Description', validators=[InputRequired()], widget=TextArea())
    