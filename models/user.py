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
