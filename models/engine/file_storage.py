#!/usr/bin/python3
"""
This module contains the File Storage class

This class serializes instances to JSON
and deserialize JSON file to an instance
"""
import os
import json


class FileStorage:
    """
    Serializes instance to JSON and deserialize JSON file to an instance
    """
    __file_path = "file.json"
    __objects = {}

    """
    Create a dictionary with key as class name and value as class itself.
    Return the class based on given class name
    """
    @staticmethod
    def selectClass(class_name):
        """
        input: class_name as a string
        return: the instance of the desired class
        """

        from .. import base_model, user, state, city, amenity, place, review
        class_dict = {'BaseModel': base_model.BaseModel, 'User': user.User,
                      'State': state.State, 'City': city.City,
                      'Amenity': amenity.Amenity, 'Place': place.Place,
                      'Review': review.Review}
        return class_dict[class_name]

    def all(self):
        """ returns FileStorage.__objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ create """
        FileStorage.__objects.update({obj.id: obj})

    def save(self):
        """ serializes FileStorage.__objects"""
        with open(FileStorage.__file_path, mode='w') as jsonFile:
            tmp_dict = {}
            for key in FileStorage.__objects.keys():
                tmp_dict[key] = FileStorage.__objects[key].to_json()
            jsonFile.write(json.dumps(tmp_dict))

    def reload(self):
        """deserializes FileStorage.__objects """
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, mode='r') as jFile:
                    obj = json.load(jFile)
                    for key in obj.keys():
                        class_name = obj[key]["__class__"]
                        new_obj = self.selectClass(class_name)(obj[key])
                        FileStorage.__objects[key] = new_obj
            except Exception as e:
                print("Exception in FileStorage reload", e)
