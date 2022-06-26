#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a class for a square with attribute size"""


class Square:
    """This is a square class """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for square

        Parameters
        ----------
        size : int
            the size of square object
        """
        try:
            self.__size = size
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except Exception as exception:
            raise exception

    @property
    def size(self):
        """
        gets the current sqare size

        Returns:
            The size of the current object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for size

        Args:
            value : int
            the size of square object
        """
        try:
            self.__size = value
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
        except Exception as exception:
            raise exception

    def area(self):
        """
        Calculates the current sqare area

        Returns:
            The area of the current object
        """
        return self.__size * self.__size

    def __lt__(self, other):
        """
        Overloads less than

        Args:
            other : Square
                square to be compared to
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Overloads greater than

        Args:
            other : Square
                square to be compared to
        """
        return self.area() > other.area()

    def __le__(self, other):
        """
        Overloads less than or equal to

        Args:
            other : Square
                square to be compared to
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Overloads greater than or equal to

        Args:
            other : Square
                square to be compared to
        """
        return self.area() >= other.area()

    def __eq__(self, other):
        """
        Overloads equal to

        Args:
            other : Square
                square to be compared to
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Overloads '!='

        Args:
            other : Square
                square to be compared to
        """
        return self.area() != other.area()
