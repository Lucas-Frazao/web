from app import app
from flask import render_template, flash, redirect, request, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse
from app.forms import LoginForm, RegistrationForm, HoursLoggingForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('some_authenticated_user_page'))

    form = LoginForm()
    if form.validate_on_submit():
        # Login logic here
        # Check if the username and password are correct
        # If so, log the user in and redirect to the user's home page
        return redirect(url_for('some_authenticated_user_page'))

    return render_template('index.html', form=form)


@app.route('/register', methods=['GET', 'POST']) #route for user registration
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    password_hash=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST']) #route for user login
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/loghours', methods=['GET', 'POST'])
@login_required
def log_hours():
    form = HoursLoggingForm()
    if form.validate_on_submit():
        hours = HoursModel(user_id=current_user.id, hours=form.hours.data)
        db.session.add(hours)
        db.session.commit()
        flash('Hours logged successfully.')
        return redirect(url_for('index'))
    return render_template('log_hours.html', title='Log Hours', form=form)

@app.route('/logout') #route for logging out
def logout():
    logout_user()
    return redirect(url_for('index'))



