from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.app_context().push()

# SQLAlchemy configuration
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_name = 'enrollege.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, db_name)
app.config['SECRET_KEY'] = os.urandom(24)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy instantiation
db = SQLAlchemy(app)
