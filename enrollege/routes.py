from enrollege import app
from enrollege.models import Users
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def home_page():
    return render_template('index.html')

