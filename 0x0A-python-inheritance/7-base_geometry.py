#!/usr/bin/python3
"""module that defines BaseGeometry class"""


class BaseGeometry:
    """a class with unimplemented method"""

    def area(self):
        """a public instance method
        Raises:
            Exception - area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance method

        Args:
            name : string
                name of integer
            value : int
                integer to be checked

        Raises:
            TypeError - <name> must be an integer
            ValueError - <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
