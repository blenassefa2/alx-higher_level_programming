#!/usr/bin/python3
"""module that defines BaseGeometry class"""


class BaseGeometry:
    """a class with unimplemented method"""

    def area(self):
        """a public instance method
        Raises:
            Exception - area() not implemented
        """
        raise Exception("area() not implemented")
