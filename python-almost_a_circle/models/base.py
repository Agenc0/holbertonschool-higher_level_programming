#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes Base instances"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_objects = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(dict_objects))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)

            dummy.update(**dictionary)
            return dummy
