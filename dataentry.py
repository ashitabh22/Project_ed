from ed_main import db
from ed_main.models import Subject

db.create_all()
math = Subject(name='Mathematics')
db.session.add(math)

phy= Subject(name='Physics')
db.session.add(phy)

chem= Subject(name='Chemistry')
db.session.add(chem)

hist= Subject(name='History')
db.session.add(hist)

compsci= Subject(name='Computer Science')
db.session.add(compsci)

db.session.commit()
