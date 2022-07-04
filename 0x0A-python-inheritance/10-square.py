#!/usr/bin/python3
""" this module creates a class that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class that inherits rectangle"""

    def __init__(self, size):
        """
        initializes the objects appropriatly

        Parameter
        ---------
            size : int
                size of square instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """implementation of method inherited from rectangle"""

        return self.__size * self.__size
