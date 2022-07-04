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
        """a public instance method
        Raises:
            TypeError - <name> must be an integer
            ValueError - <name> must be greater than 0
        """
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
