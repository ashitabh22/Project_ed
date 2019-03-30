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

app = Flask(__name__) 
csrf=CSRFProtect(app)
app.config['SECRET_KEY']='f6eeaa4486447025a35ab182035a34a0'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from ed_main import routes
