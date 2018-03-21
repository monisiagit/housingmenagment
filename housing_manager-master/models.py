__author__ = 'Piotr Dyba'



from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Boolean

from main import db

from flask_login import UserMixin

from main import lm







class User(db.Model, UserMixin):
    """
    User model for reviewers.
    """
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    active = Column(Boolean, default=True)
    email = Column(String(200), unique=True)
    password = Column(String(200), default='')
    admin = Column(Boolean, default=False)
    username = Column(String(200), unique=True)

    def is_active(self):
        """
        Returns if user is active.
        """
        return self.active

    def is_admin(self):
        """
        Returns if user is admin.
        """
        return self.admin

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
