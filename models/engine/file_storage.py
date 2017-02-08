#!/usr/bin/python3
"""
This module contains the File Storage class

This class serializes instances to JSON
and deserialize JSON file to an instance
"""
import os, json
class FileStorage:
    """
    Serializes instance to JSON and deserialize JSON file to an instance
    """
    def __init__(self):
        """ The init """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ returns __objects"""
        return self.__objects

    def new(self, obj):
        """ create """
        self.__objects[obj.id] = obj

    def save(self):
        """ serializes __objects"""
        with open(self.__file_path, mode='w', encoding='utf-8') as myFile:
            myFile.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes self.__objects """
        if os.path.isfile(self.__file_path) == True:
            with open(self.__file_path, mode='r', encoding='utf-8') as myFile:
                self.__objects = json.loads(myFile.read())
        else:
            open(self.__file_path, mode='a').close()
