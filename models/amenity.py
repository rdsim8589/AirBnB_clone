#!/usr/bin/python3
"""
This is the Amenity class module. This module creates a Amenity class that
inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This is the Amenity Class, it inherts from BaseModel """
    name = ""
