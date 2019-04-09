from ed_main import app, db,admin
from ed_main.models import * 
from flask_admin.contrib.sqla import ModelView 



class SubjectView(ModelView): 
    column_searchable_list = ['name'] 
    form_excluded_columns = ['questions']

    def create_model(self,form): 
        temp  = Subject.query.all()
        subject_names = [x.name for x in temp]

        if form.name.data not in subject_names: 
            db.session.add(Subject(name=form.name.data)) 
            db.session.commit()
            return 
        else: 
            raise NotImplementedError()

class DifficultyView(ModelView): 
    column_searchable_list = ['name'] 
    form_excluded_columns = ['questions']

    def create_model(self,form): 
        temp  = Difficulty.query.all()
        difficulty_names = [x.name for x in temp]

        if form.name.data not in difficulty_names: 
            db.session.add(Difficulty(name=form.name.data)) 
            db.session.commit()
            return 
        else: 
            raise NotImplementedError()

class GradeView(ModelView): 
    column_searchable_list = ['name'] 
    form_excluded_columns = ['questions']

    def create_model(self,form): 
        # temp  = Grade.query.all()
        # grade_names = [x.name for x in temp]

        # if form.name.data not in grade_names: 
        #     db.session.add(Difficulty(name=form.name.data)) 
        #     db.session.commit()
        #     return 
        # else: 
        #     raise NotImplementedError()

        try: 
            db.session.add(Grade(name=form.name.data))
            db.session.commit() 
        except: 
            raise NotImplementedError()
admin.add_view(SubjectView(Subject,db.session))
admin.add_view(DifficultyView(Difficulty,db.session))
admin.add_view(GradeView(Grade,db.session))
