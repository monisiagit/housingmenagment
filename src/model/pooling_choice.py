from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from main import db


class PoolingChoice(db.Model):
    __tablename__ = 'pooling_choice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.now())
    login_id = Column(Integer, ForeignKey('user.id'), nullable=False, default=None)
    pooling_id = Column(Integer, ForeignKey('pooling.id'), nullable=False, default=None)
    choice = Column(Integer, nullable=True, default=None)

    login = relationship('User')
    pooling = relationship('Pooling', back_populates='choices')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
