#!/usr/bin/python3
"""
This is the State class module. This module creates a State class that inherits
from BaseModel.
"""
from models.base_model import BaseModel
import weakref

class State(BaseModel):
    instance_list = []
    instance_count = 0
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.instance_list.append(weakref.proxy(self))
        self.__class__.instance_count += 1
