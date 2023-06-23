#!/usr/bin/python3
"""Defines a base class"""
import json
import csv


class Base:
    """A class that will be the “base” of all other classes in this project.

    Args:
        id(int): the id of the newly instantiated base.

    Attributes:
        __nb_objects(int): the number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries(list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs(list): list of instances which inherits from base.
        """
        dict_list = []
        if list_objs is not None:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w") as filename:
            filename.write(cls.to_json_string(dict_list))
