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
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns FileStorage.__objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ create """
        FileStorage.__objects.update({obj.id:obj})

    def save(self):
        """ serializes FileStorage.__objects"""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as jsonFile:
            tmp_dict = {}
            for key in FileStorage.__objects.keys():
                tmp_dict[key] = FileStorage.__objects[key].to_json()
            jsonFile.write(json.dumps(tmp_dict))

    def reload(self):
        """deserializes FileStorage.__objects """
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, mode='r', encoding='utf-8') as jFile:
                    obj = json.load(jFile)
                    for key in obj.keys():
                        new_obj = BaseModel(obj[key])
                        FileStorage.__objects[key] = new_obj
            except Exception as e:
                print(e)
