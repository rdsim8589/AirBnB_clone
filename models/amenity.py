#!/usr/bin/python3
"""
This is the Amenity class module. This module creates a Amenity class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Assign public attribute name to the object.
    """
    def name(self, name):
        self.name = name
