#!/usr/bin/python3
"""
This is the User module. This module defines a User class that inherits from
BaseModel.
"""
from .base_model import BaseModel
import weakref

class User(BaseModel):
    instance_list = []
    instance_count = 0
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.instance_list.append(weakref.proxy(self))
        self.__class__.instance_count += 1
