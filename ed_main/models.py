from ed_main import db
from datetime import datetime

class Subject(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name= db.Column(db.String(40),nullable =False, unique= True) 
    questions = db.relationship('Question',backref= 'subject') 

    def __repr__(self): 
         return f"({self.id},{self.name})" 

class Difficulty(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name=db.Column(db.Integer, nullable = False,unique =True)
    questions = db.relationship('Question',backref='difficulty')
    def __repr__(self): 
         return f"({self.id}, {self.name})" 

class Grade(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10), nullable = False, unique= True)
    questions = db.relationship('Question',backref='grade')
    def __repr__(self): 
         return f"({self.id}, {self.name})" 


class Question(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    question_text = db.Column(db.String(10000),nullable=False)
    difficulty_id = db.Column(db.Integer,db.ForeignKey('difficulty.id'))
    subject_id = db.Column(db.String(40),db.ForeignKey('subject.id'))
    grade_id = db.Column(db.String(10),db.ForeignKey('grade.id'))
    answers = db.Column(db.JSON)

    istag = db.relationship('Tags', backref = 'question_tags') 
    def __repr__(self): 
         return f"({self.id}, {self.question_text}, {self.grade_id}, {self.subject_id}, {self.difficulty_id})" 


class Tags(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), unique=True) 
    tags = db.Column(db.String(500)) 

    def __repr__(self) : 
        return f"{self.id} | {self.question_id} | {self.tags}"


