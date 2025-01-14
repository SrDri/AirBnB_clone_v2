#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenity_ids = []
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    if environ['HBNB_TYPE_STORAGE'] != 'db':
        @property
        def amenities(self):
            """ Getter amenities """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, instance=None):
            """ Setter amenities """
            if isinstance(instance, Amenity):
                if instance.place_amenity.place_id == self.id:
                    self.amenity_ids.append(instance.id)
