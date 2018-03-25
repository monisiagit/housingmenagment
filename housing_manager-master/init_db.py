__author__ = 'Piotr Dyba'

from sqlalchemy import create_engine
from main import db
from src.entity import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    user = User()
    user.username = "piotr"
    user.password = bcrypt.generate_password_hash('pppp1234')
    user.email = 'piotr@dyba.com.pl'
    user.admin = True
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    db_start()
