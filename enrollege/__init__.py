from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
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

# Instantiate login_manger and bcrypt
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login_page'
login_manager.login_message = 'You need to login in order to get recommendations'
login_manager.login_message_category = 'info'

from enrollege import routes
