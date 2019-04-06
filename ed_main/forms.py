from flask import Flask 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField,BooleanField, SubmitField, TextField, SelectField,IntegerField, RadioField, SelectMultipleField ,widgets
from wtforms.validators import DataRequired, Length ,Email,EqualTo




class Question_form(FlaskForm): 
    question = TextField('Question', validators =[ DataRequired()] )
    classes = SelectField('Class', choices=[])
    subject = SelectField('Subject', choices=[])
    difficulty= SelectField('Difficulty', choices=[]) 
    grades = SelectField('Grades', choices =[]) 
    submit = SubmitField('Add Question') 

class SearchForm(FlaskForm): 
    search =TextField('Search', validators = [DataRequired()])
    submit = SubmitField('Search')
