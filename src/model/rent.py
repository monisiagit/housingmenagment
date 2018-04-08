from sqlalchemy import Column, Integer, Numeric, String, DateTime, Text, ForeignKey
from datetime import datetime
from main import db

from sqlalchemy.orm import relationship

class Rent(db.Model):
    __tablename__ = 'rent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flat_id = Column(Integer, ForeignKey('flat.id'), nullable=False, default=None)
    value = Column(Numeric(precision=22, scale=2), nullable=False, default=0.0)
    startDate = Column(DateTime, nullable=False, default=datetime.now())
    finishDate = Column(DateTime, nullable=False, default=datetime.now())
    iban = Column(String(36, convert_unicode=True), nullable=False, default=None)
    title = Column(Text(convert_unicode=True), nullable=True, default=None)

    flat = relationship('Flat', back_populates='rents')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
