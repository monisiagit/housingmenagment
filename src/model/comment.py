from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from main import db


class Comment(db.Model):
    __tablename__ = 'comment'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.now())
    login_id = Column(Integer, ForeignKey('user.id'), nullable=False, default=None)
    pooling_id = Column(Integer, ForeignKey('pooling.id'), nullable=True, default=None)
    announcement_id = Column(Integer, ForeignKey('announcement.id'), nullable=True, default=None)
    content = Column(String(300, convert_unicode=True), nullable=False, default=None)
    is_deleted = Column(Boolean, nullable=False, default=True)

    login = relationship('User')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
