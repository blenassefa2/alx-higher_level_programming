#!/usr/bin/python3
"""module that defines Rectangle"""


BaseGeometry = __import__('7-base_geometry').__BaseGeometry

class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry class"""

    def __init__(self, width, height):
        """
        Initializes the class

        Parameters
        ---------
            width : int
                width of rectangle
            height : int
                height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
