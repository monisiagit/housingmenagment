from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .flats_landlords import FlatsLandlords
from main import db


class Flat(db.Model):
    __tablename__ = 'flat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    storey = Column(Integer, nullable=False, default=None)
    number = Column(String(10, convert_unicode=True), nullable=False, default=None)
    stairway = Column(String(10, convert_unicode=True), nullable=True, default=None)
    personCount = Column(Integer, nullable=False, default=0)

    landlords = relationship('Landlord', secondary=FlatsLandlords, back_populates='flats')
    rents = relationship('Rent', back_populates='flat')
    payments = relationship('Payment', back_populates='flat')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
