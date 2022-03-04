#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
import global_usage

class FileStorage:

    """Class for converting JSON to base class and vice versa."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Convert objects to JSON file."""
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as filest:
            dictio = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dictio, filest)


    def reload(self):
        """Transform the JSON file into objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r+", encoding="utf-8") as filest:
            obj_dict = json.load(filest)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
    def classes(self):
        """Retourn le  dictionaires des classes de référence"""

        return global_usage.classe
