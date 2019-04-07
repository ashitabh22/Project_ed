from flask import Flask, render_template , request, redirect,url_for
from ed_main import app , db
from ed_main.forms import Question_form ,SearchForm
from ed_main.models import Subject, Difficulty, Grade, Question, Tags
import flask_whooshalchemy



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

@app.route('/search_results')
def view_search(): 
    answer=[]
    try: 
        result = Question.query.whoosh_search(request.args.get('search_question')).all()
        answer = answer + result
    except: 
        tag_results = Tags.query.whoosh_search(request.args.get('search_question')).all()
        temp = [ Question.query.filter_by(id = x.question_id).first() for x in tag_results]
        answer = answer + temp
    # else: 
    #     tag_results = Tags.query.whoosh_search(request.args.get('search_question')).all()
    #     temp = [ Question.query.filter_by(id = x.question_id).first() for x in tag_results]
        # answer = answer + temp


    return render_template('question_viewer.html', questions = answer) 

@app.route('/question_viewer', methods = ['get','post'])
def question_viewer(): 
    # if request.method=="POST":
    #     # print(request.form['search_question'])
    #     # results = Question.query.whoosh_search(request.form['search_question']).all()
    #     return redirect(url_for('view_search', query = request.form['search_question']))
    #     # return redirect(url_for('view_search',search = request.form['search_question']))
    questions = Question.query.all()
    return render_template('question_viewer.html', questions = questions) 
    
@app.errorhandler(500)
def database_error(error): 
    db.session.rollback()
    return redirect(url_for('question_viewer'))
