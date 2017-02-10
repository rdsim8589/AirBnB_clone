#!/usr/bin/python3
"""
This is the Amenity class module. This module creates a Amenity class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    """
    Initialize object of Amenity class, calling the Parent calss __init__().
    """
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
