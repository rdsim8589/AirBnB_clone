#!/usr/bin/python3
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""
from models.base_model import BaseModel
import weakref

class City(BaseModel):
    instance_list = []
    instance_count = 0
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.instance_list.append(weakref.proxy(self))
        self.__class__.instance_count += 1
