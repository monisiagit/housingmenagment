from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .flats_landlords import FlatsLandlords
from main import db


class Landlord(db.Model):
    __tablename__ = 'landlord'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login_id = Column(Integer, ForeignKey('user.id'), nullable=False, default=None)
    share = Column(Float, nullable=False, default=0.0)
    name = Column(String(50, convert_unicode=True), nullable=False, default=None)
    surname = Column(String(50, convert_unicode=True), nullable=False, default=None)
    address = Column(String(100, convert_unicode=True), nullable=False, default=None)
    mobile = Column(String(16), nullable=True, default=None)

    flats = relationship('Flat', secondary=FlatsLandlords, back_populates='landlords')
    login = relationship('User')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
