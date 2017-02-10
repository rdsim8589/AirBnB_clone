#!/usr/bin/python3
"""
This is the Place class module. This module creates a Place class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Assign public attribute state_id to the object.
    """
    def city_id(self):
        self.city_id = City.id

    def user_id(self):
        self.user_id = User.id

    """
    Assign public attribute name to the object.
    """
    def name(self, name=""):
        self.name = name

    """
    Assign public attribute description to the object.
    """
    def description(self, description=""):
        self.description = description

    def number_rooms(self, number_rooms=0):
        self.number_rooms = number_rooms

    def number_bathrooms(self, number_bathrooms=0):
        self.number_bathrooms = number_bathrooms

    def max_guest(self, max_guest=0):
        self.max_guest = max_guest

    def price_by_night(self, price_by_night=0):
        self.price_by_night = price_by_night

    def latitude(slef, latitude=0.0):
        self.latitude = latitude

    def longitude(self, longitude=0.0):
        self.longitude = longitude

    def amenities(self):
        self.amenities = []
        self.amenities.append(amenities)
