#!/usr/bin/python3
"""module that defines Rectangle"""


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
                name of variable
            value : int
                integer to be validated

        Raises:
            TypeError - <name> must be an integer
            ValueError - <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """implementation of the method from inherited class"""

        return self.__width * self__height

    def __str__(self):
        """makes the class printable"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
