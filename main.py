from os import path

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
lm = LoginManager()
lm.init_app(app)

app.static_path = path.join(path.abspath(__file__), 'static')

if __name__ == '__main__':
    from src.views.views import *

    app.run(debug=True)
