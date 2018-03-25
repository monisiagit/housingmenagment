from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean

from main import db, lm

bcrypt = Bcrypt()


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def encode_password(raw_password):
        return bcrypt.generate_password_hash(raw_password)

    @classmethod
    def create(cls, username, email, raw_password):
        return User(username=username, email=email, password=cls.encode_password(raw_password))

    @staticmethod
    def authenticate(username, raw_password):
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(raw_password):
            return user
        return False

    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def verify_password(self, raw_password):
        return bcrypt.check_password_hash(self.password, raw_password)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

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

