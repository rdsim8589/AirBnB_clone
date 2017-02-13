#!/usr/bin/python3
"""
This is the Review class module. This module creates a Review class that
inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ This is the Review class and it inherts from BaseModel class """
    place_id = ""
    user_id = ""
    text = ""
