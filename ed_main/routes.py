from flask import Flask, render_template 
from ed_main import app , db
from ed_main.forms import Question_form 
from ed_main.models import Subject 




@app.route('/', methods =['get','post'])
def home(): 
    form = Question_form()
    main_sub=[]
    for sub in Subject.query.all():
        main_sub.append(sub.name) 
    return render_template('index.html', form = form,subjects = main_sub ) 
