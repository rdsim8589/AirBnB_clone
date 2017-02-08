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
    __path = "file.json"
    __objects = {}

    def all(self):
        """ returns FileStorage.__.objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ create """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """ serializes FileStorage.__.objects"""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as jsonFile:
            jsonFile.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """deserializes FileStorage.__.objects """
        if os.path.isfile(FileStorage.__file_path) == True:
            try:
                with open(FileStorage.__file_path, mode='r', encoding='utf-8') as jsonFile:
                    
                    FileStorage.__objects = json.loads(jsonFile.read())
            except Exception as e:
                pass
