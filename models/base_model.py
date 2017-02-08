#!/usr/bin/python3
"""
This is the BaseModel module. This module defines a BaseModule class.
The BaseModule class defines common attributes/methods for other classes.
"""

import datetime, uuid
class BaseModel:
    """
    Initilaize the object and assign a unique ID and current time.
    """
    def __init__(self):
        # make a random UUID
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()


    """
    Assign public attribute name to the object.
    """
    def name(self, name):
        self.name = name

    """
    Assign public attribute my_number to the object.
    """
    def my_number(self, my_number):
        self.my_number = my_number

    """
    Update the public instance attribute updated_at with the current datetime
    """
    def save(self):
        self.updated_at = str(datetime.datetime.now())

    """
    Return a dictionary containing all keys/values of __dict__ of the object.
    """
    def to_json(self):
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = str(self.created_at)
        self.__dict__["updated_at"] = str(self.updated_at)
        return self.__dict__

    """
    Return object as a string.
    """
    def __str__(self):
        strng = ""
        strng += "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return strng
