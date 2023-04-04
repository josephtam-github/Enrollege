from enrollege import app
from enrollege.models import Users
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from enrollege.forms import RegisterForm, LoginForm


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/signup')
def signup_page():
    form = RegisterForm()
    return render_template('signup.html', form=form)


@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    return render_template('login.html')


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
