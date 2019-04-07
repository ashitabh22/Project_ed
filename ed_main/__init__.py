# from flask import Flask 
# from flask_wtf.csrf import CSRFProtect, CSRFError 
# from flask_sqlalchemy import SQLAlchemy 

# app = Flask(__name__) 
# csrf=CSRFProtect(app)
# app.config['SECRET_KEY']='f6eeaa4486447025a35ab182035a34a0'
# app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:///site.db'
# db = SQLAlchemy(app)

# from ed_main import routes





# converting your app into a package structure. 
from flask import Flask
from flask_wtf.csrf import CSRFProtect, CSRFError 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from whoosh.analysis import StemmingAnalyzer 
import flask_whooshalchemy

app = Flask(__name__) 
csrf=CSRFProtect(app)
app.config['SECRET_KEY']='f6eeaa4486447025a35ab182035a34a0'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONAS'] = True 
app.config['WHOOSH_BASE'] = 'whoosh'
app.config['WHOOSH_ANALYZER'] = StemmingAnalyzer()


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from ed_main import routes

