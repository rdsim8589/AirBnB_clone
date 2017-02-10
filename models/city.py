#!/usr/bin/python3
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    """
    Initialize the object of City class, calling __init__() of Parent Class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
