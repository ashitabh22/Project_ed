from ed_main import db 
from ed_main.models import Subject

print(Subject.query.all())
