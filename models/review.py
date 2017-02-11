#!/usr/bin/python3
"""
This is the Review class module. This module creates a Review class that inherits
from BaseModel.
"""
from models.base_model import BaseModel
import weakref


class Review(BaseModel):
    instance_list = []
    instance_count = 0
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.instance_list.append(weakref.proxy(self))
        self.__class__.instance_count += 1
