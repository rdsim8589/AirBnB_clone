#!/usr/bin/python3
"""
This is the Review class module. This module creates a Review class that inherits
from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    """
    Initialize the object of Review class, calling __init__() of parent class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
