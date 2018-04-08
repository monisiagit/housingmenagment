from sqlalchemy import Column, Integer, Text, DateTime, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from main import db


class Announcement(db.Model):
    __tablename__ = 'announcement'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(), nullable=False, default=datetime.now())
    login_id = Column(Integer, ForeignKey('user.id'), nullable=False, default=None)
    content = Column(Text(convert_unicode=True), nullable=False, default=None)
    title = Column(String(60, convert_unicode=True), nullable=False, default=None)
    is_deleted = Column(Boolean, nullable=False, default=True)

    comments = relationship('Comment')
    login = relationship('User')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
