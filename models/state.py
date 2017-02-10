#!/usr/bin/python3
"""
This is the State class module. This module creates a State class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Assign public attribute name to the object.
    """
    def name(self, name):
        self.name = name
