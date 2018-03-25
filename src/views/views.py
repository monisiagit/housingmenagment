#!/usr/bin/env python
# encoding: utf-8
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_bcrypt import Bcrypt
from forms import RegistrationForm
from main import app, db
from src.model import User

bcrypt = Bcrypt()


app.secret_key = 'random string'

messages = {
    'login.invalid': ('Incorrect password or username', 'danger'),
    'login.correct': ('You have been succesfuly logged in', 'success'),
    'login.new': ('Wellcome, you have been succesfully registered', 'success')
}


@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('info.html')


@app.route('/check_login', methods=['POST'])
def check_login():
    user = User.authenticate(request.form['Username'], request.form['Password'])
    if user:
        login_user(user)
        flash(*messages['login.correct'])
    else:
        flash(*messages['login.invalid'])

    return redirect('/login')


@app.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('info'))

    return render_template('logowanie.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('info'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('info'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.password = bcrypt.generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(*messages['login.new'])
        return redirect(url_for('login'))
    return render_template('rejestracja.html', title='Register', form=form)
