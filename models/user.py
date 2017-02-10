#!/usr/bin/python3
"""
This is the User module. This module defines a User class that inherits from
BaseModel.
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Assign public attribute email to the object.
    """
    def email(self, email=""):
        self.email = email

    """
    Assign public attribute pasword to the object.
    """
    def password(self, password=""):
        self.password = password

    """
    Assign public attribute first_name to the object.
    """
    def first_name(self, first_name=""):
        self.first_name = first_name

    """
    Assign public attribute last_name to the object.
    """
    def last_name(self, last_name):
        self.last_name = last_name
