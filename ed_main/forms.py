from flask import Flask 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField,BooleanField, SubmitField, TextField, SelectField,IntegerField, RadioField, SelectMultipleField ,widgets
from wtforms.validators import DataRequired, Length ,Email,EqualTo




class Question_form(FlaskForm): 
    # question = TextField('Question', validators =[ DataRequired()] )
    classes = SelectField('Class', choices=[('None', 'None'),
       ('Class 1','1'), ('Class 2','2'), ('Class 3','3'), ('Class 4','4'), ('Class 5','5'), ('Class 6','6'), ('Class 7','7'), ('Class 8','8'), ('Class 9','9'),
       ('Class 10','10'), ('Class 11','11'), ('Class 12','12') ])
    subject = SelectField('Subject', choices=  [('math','Mathematics'),('phy','Physics')])
    # difficulty= SelectField('Difficulty', choices = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'),
        # ('8','8'), ('9','9'), ('10','10') ])

    submit = SubmitField('Add Question') 


