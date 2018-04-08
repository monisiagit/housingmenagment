from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from main import db


class Pooling(db.Model):
    __tablename__ = 'pooling'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=True, default=datetime.now())
    login_id = Column(Integer, ForeignKey('user.id'), nullable=False, default=None)
    flat_id = Column(Integer, ForeignKey('flat.id'), nullable=True, default=None)
    landlord_id = Column(Integer, ForeignKey('landlord.id'), nullable=True, default=None)
    title = Column(Text(convert_unicode=True), nullable=True, default=None)
    startDate = Column(DateTime, nullable=True, default=datetime.now())
    finishDate = Column(DateTime, nullable=True, default=None)
    is_deleted = Column(Boolean, nullable=False, default=True)

    flat = relationship('Flat')
    login = relationship('User')
    landlord = relationship('Landlord')
    comments = relationship('Comment')
    choices = relationship('PoolingChoice', back_populates='pooling')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
