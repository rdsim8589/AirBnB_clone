#!/usr/bin/python3
"""
This is the BaseModel module. This module defines a BaseModule class.
The BaseModule class defines common attributes/methods for other classes.
"""
from . import storage
from datetime import datetime
import uuid


class BaseModel:
    """
    Initilaize the object and assign a unique ID and current time.
    """
    def __init__(self, *args, **kwargs):
        dict_found = 0
        for arg in args:
            if type(arg) == dict:
                dict_found = 1
                break
        if dict_found == 1:
            args[0]['created_at'] = datetime.strptime(
                args[0]['created_at'], '%Y-%m-%d %H:%M:%S.%f')
            args[0]['updated_at'] = datetime.strptime(
                args[0]['updated_at'],  '%Y-%m-%d %H:%M:%S.%f')
            self.__dict__ = args[0]
        else:
            # make a random UUID
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    """
    Update the public instance attribute updated_at with the current datetime
    """
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    """
    Return a dictionary with values converts to json format
    """
    def to_json(self):
        tmp_dict = self.__dict__.copy()
        tmp_dict["__class__"] = type(self).__name__
        tmp_dict["created_at"] = str(self.created_at)
        tmp_dict["updated_at"] = str(self.updated_at)
        return tmp_dict

    """
    Return object as a string.
    """
    def __str__(self):
        string = ""
        string += "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
        return string
