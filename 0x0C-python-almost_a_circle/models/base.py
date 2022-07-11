#!/usr/bin/python3
import json
"""a module that defines a class called base"""


class Base:
    """A class called base"""

    __nb_objects = 0  # Private class attr

    def __init__(self, id=None):
        """initializes a Base object appropriately

        Parameter
        ---------
            id : int
                integer value used later
        """
        self.id = None  # Public instance attr
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of list_dictionaries """
        if not list_dictionaries or list_dictionaries == []:
            return '[]'
        if (type(list_dictionaries) != list or
                not all(type(item) == dict for item in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
