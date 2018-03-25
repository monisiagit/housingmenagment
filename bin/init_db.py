__author__ = 'Piotr Dyba'

from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine

from src.model import User
from ..main import db

bcrypt = Bcrypt()


def db_start():
    create_engine('sqlite:///../var/tmp/test.db', convert_unicode=True)
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
