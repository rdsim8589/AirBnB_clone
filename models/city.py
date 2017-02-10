#!/usr/bin/python3
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Assign public attribute state_id to the object.
    """
    def state_id(self, state_id):
        self.state_id = state_id

    """
    Assign public attribute name to the object.
    """
    def name(self, name):
        self.name = name
