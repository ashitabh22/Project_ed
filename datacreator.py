from ed_main import db
import ed_main.models
from ed_main.models import * 

db.create_all() 


for x in range(1,11): 
    diff = Difficulty(name=f"{x}")
    db.session.add(diff) 
    # db.session.commit() 


for x in range(1,11): 
    grades = Grade(name=f"grade_{x}")
    db.session.add(grades) 
    # db.session.commit() 


subs = [' Math', 'History', 'Computer Science', 'Psychology', 'Physics','Chemistry']

for x in subs: 
    sub = Subject(name=x) 
    db.session.add(sub) 
    # db.session.commit() 


ques_1 =Question(question_text= 'Pyhsics, angle force, newton pulled by block', difficulty_id =3,subject_id=5,grade_id=4,answers = { "1": 23, "2":45, "3":11})
ques_2 =Question(question_text= 'Chemistry,reaction atoms molecules', difficulty_id =4,subject_id=6,grade_id=2,answers = { "1": 23, "2":45, "3":11})
ques_3 =Question(question_text= 'Mathematics,add,subtract,integrate', difficulty_id =3,subject_id=1,grade_id=4,answers = { "1": 23, "2":45, "3":11})
ques_4 =Question(question_text= 'akbar, history , very old', difficulty_id =3,subject_id=2,grade_id=4,answers = { "1": 23, "2":45, "3":11})
ques_5 =Question(question_text= 'C code, pointers, binary searching, sorting', difficulty_id =3,subject_id=3,grade_id=4,answers = { "1": 23, "2":45, "3":11})


ques_list = [ques_1,ques_2,ques_3,ques_4,ques_5]

for x in ques_list: 
    db.session.add(x) 
    # db.session.commit() 



tag_list=['physics,newton,waves,light,sound,angle,force','molecules,atoms,reactions','intergration,subtraction,numbers 123','year, something,1986','pointers,something']

for x in range(0,5): 
    tag_cur = Tags(tags=tag_list[x], question = ques_list[x])
    db.session.add(tag_cur) 
    # db.session.commit()
db.session.commit()
