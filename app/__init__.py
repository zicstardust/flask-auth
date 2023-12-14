from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRETE_KEY'] = 'dSdwqe2le2'

login_manager = LoginManager(app)
db = SQLAlchemy(app)
