from flask import Flask, render_template , request, redirect,url_for
from ed_main import app , db
from ed_main.forms import Question_form ,SearchForm
from ed_main.models import Subject, Difficulty, Grade, Question 









@app.route('/', methods =['get','post'])
def home(): 
    form = Question_form()
    main_sub=[(subject.id,subject.name) for subject in Subject.query.all()]
    diff_level=[(level.id,level.name) for level  in Difficulty.query.all()]
    grades = [(grade.id,grade.name) for grade in Grade.query.all()]

    form.subject.choices=main_sub
    form.difficulty.choices=diff_level
    form.grades.choices=grades

    # if form.validate_on_submit():
    # else: 

    return render_template('index.html', form = form) 

@app.route('/view_search/<search>')
def view_search(search): 
    # print('I am here')
    print(search)
    return '<h1> hi </h1>'

@app.route('/question_viewer', methods = ['get', 'post'])
def question_viewer(): 
    # form = SearchForm()
    # print( form.validate_on_submit())
    if request.method=="POST":
        # print(request.form['search_question'])
        return redirect(url_for('view_search',search = request.form['search_question']))
    return render_template('question_viewer.html',questions =Question.query.all()) 
    
