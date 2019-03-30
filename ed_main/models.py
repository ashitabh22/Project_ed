from ed_main import db


class Subject(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name= db.Column(db.String(40),nullable =False, unique= True) 

    def __repr__(self): 
         return f"Subject('{self.name}')" 
