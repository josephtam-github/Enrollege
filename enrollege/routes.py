from enrollege import app
from enrollege.models import Users
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def logout_page():
    return render_template('account.html')


@app.route('/profile')
def profile_page():
    return render_template('profile.html')


@app.route('/result')
def result_page():
    return render_template('result.html')


@app.route('/settings')
def settings_page():
    return render_template('settings.html')


@app.route('/rankings')
def rankings_page():
    return render_template('rankings.html')
