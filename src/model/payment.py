from sqlalchemy import Column, Integer, Numeric, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from main import db


class Payment(db.Model):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Numeric(precision=22, scale=2), nullable=False, default=0.0)
    paymentTime = Column(DateTime, nullable=False, default=datetime.now())
    flat_id = Column(Integer, ForeignKey('flat.id'), nullable=False, default=None)
    iban = Column(String(36, convert_unicode=True), default='')
    title = Column(Text(convert_unicode=True), nullable=True, default=None)

    flat = relationship('Flat', back_populates='payments')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
