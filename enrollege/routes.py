from enrollege import app, db
from enrollege.models import Users
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from enrollege.forms import RegisterForm, LoginForm


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/signup')
def signup_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data,
                               firstname=form.firstname.data,
                               lastname=form.lastname.data,
                               email_address=form.email_address.data,
                               password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Welcome to the community {user_to_create.firstname}!', category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error signing you up: {err_msg}', category='danger')
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
