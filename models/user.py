#!/usr/bin/python3
"""
This is the User module. This module defines a User class that inherits from
BaseModel.
"""
from .base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """
    Initialize the User class object, calling __init__() of the Parent class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
