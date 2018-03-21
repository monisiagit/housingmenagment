#!/usr/bin/env python
# encoding: utf-8
from main import app
from main import db
from main import bcrypt
from main import lm
from models import User
from forms import RegistrationForm

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user , logout_user , current_user , login_required
app.secret_key = 'random string'

@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('info.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('info'))
    error = None

    if request.method == 'POST':
        gosc = User.query.filter_by(username=request.form['Username']).first()
        if gosc is None:
            error = 'Złe hasło lub nazwa użytkwanika! Spróbuj jeszcze raz'
        else:
            if bcrypt.check_password_hash(gosc.password, request.form['Password']):
                flash('Logowanie zakończone sukcesem')
                login_user(gosc)
                return redirect(url_for('info'))
            else:
                error= 'Złe hasło lub nazwa użytkwanika! Spróbuj jeszcze raz'

    return render_template('logowanie.html', error=error)

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
        user.password=bcrypt.generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('rejestracja.html', title='Register', form=form)