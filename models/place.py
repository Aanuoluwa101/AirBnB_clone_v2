#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
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
    reviews = relationship("Review", backref='place', cascade="all, delete")
    amenity_ids = []

    @property
    def reviews(self):
        """Returns the list of Review instances"""
        from models import storage
        review_list = []
        extracted_reviews = models.storage.all(Review).values()
        for review in extracted_reviews:
            if review.place_id: == self.id
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Returns the list of Amenity instances"""
        from models import storage
        review_list = []
        extracted_amenities = models.storage.all('Amenity').values()
        for amenity in extracted_amenities:
            if amenity.amenity_ids: == self.id
                review_list.append(amenity)
        return review_list

    @amenities.setter
    def amenities(self, obj):
        """Append method"""
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
