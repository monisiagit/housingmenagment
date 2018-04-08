from sqlalchemy import Column, Integer, ForeignKey
from main import db

FlatsLandlords = db.Table('flats_landlords', db.Model.metadata,
                       Column('flat_id', Integer, ForeignKey('flat.id'), primary_key=True),
                       Column('landlord_id', Integer, ForeignKey('landlord.id'), primary_key=True))
