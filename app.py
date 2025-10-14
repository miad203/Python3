from flask import Flask, render_template, url_for, redirect, flash, session
from forms import RegisterForm, LoginForm, ContentForm
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from os import path
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'noP@ssworD!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usr_info.db'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

from models import User, Note


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            encrypted = encrypt_password(form.password.data)
            usr = User(username=form.username.data,
                       email=form.email.data, password=encrypted)
            db.session.add(usr)
            db.session.commit()
            session.permanent = True
            session['email'] = usr.email
            session['password'] = usr.password
            flash("Account created successfully!", "info")
            return redirect(url_for('home'))
        except Exception as error:
            flash(f'{error}', 'danger')
    return render_template('register.html', form=form, title="Sign Up")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'email' and 'password' in session:
        flash('You already logged in!', 'info')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        encrypted = encrypt_password(form.password.data)
        if user:
            if encrypted == user.password:
                session.permanent = True
                session['email'] = user.email
                session['password'] = user.password
                flash("Successfully logged in!", "success")
                return redirect(url_for('home'))
            flash('Check your information and try again!', 'danger')
        else:
            flash('No User found with this email!', 'warning')
            return redirect(url_for('register'))
    return render_template('login.html', form=form, title="Log In")


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('password', None)
    flash("You've been logged out!", "primary")
    return redirect(url_for('login'))


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    if 'email' and 'password' not in session:
        flash('Please log in your account', 'danger')
        return redirect(url_for('login'))

    form = ContentForm()
    if form.validate_on_submit():
        post = Note(content=form.content.data)
        db.session.add(post)
        db.session.commit()

    note = Note.query.all()
    return render_template('home.html', title="Home", form=form, note=note)


if __name__ == "__main__":
    if not path.exists('NoteBook/instance/usr_info.db'):
        with app.app_context():
            db.create_all()

    def encrypt_password(psk):
        algarithm = hashlib.sha256()
        algarithm.update(psk.encode())
        return algarithm.hexdigest()

    app.run(debug=True)
