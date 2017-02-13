#!/usr/bin/python3
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This is the City class and it inherts from BaseModel """
    state_id = ""
    name = ""
