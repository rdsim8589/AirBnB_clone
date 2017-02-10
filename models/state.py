#!/usr/bin/python3
"""
This is the State class module. This module creates a State class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    """
    Initialize the object of State class, calling __init__() of parent class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
