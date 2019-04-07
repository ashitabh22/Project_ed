from ed_main import db
from ed_main.models import *

db.create_all()
db.session.add(Difficulty(name='1'))
db.session.add(Difficulty(name='2'))
db.session.add(Difficulty(name='3'))
db.session.add(Difficulty(name='4'))
db.session.add(Difficulty(name='5'))
db.session.add(Difficulty(name='6'))
db.session.add(Difficulty(name='7'))
db.session.add(Difficulty(name='8'))
db.session.add(Difficulty(name='9'))
db.session.add(Difficulty(name='10'))

db.session.commit()
