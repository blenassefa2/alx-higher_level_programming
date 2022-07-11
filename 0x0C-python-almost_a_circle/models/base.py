#!/usr/bin/python3
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
