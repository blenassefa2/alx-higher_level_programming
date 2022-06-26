#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a class for a square with attribute size"""


class Square:
    """This is a square class """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs all the necessary attributes for square

        Parameters
        ----------
        size : int
            the size of square object
        position: tuple
            positions of lines
        """
        try:
            self.__position = position
            self.__size = size
            errr = "position must be a tuple of 2 positive integers"
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            if len(position) != 2:
                raise TypeError(err)
            if not isinstance(position[0], int):
                raise TypeError(err)
            if not isinstance(position[1], int):
                raise TypeError(err)
            if position[0] < 0 or position[1] < 0:
                raise TypeError(err)
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

    @property
    def position(self):
        """
        gets the current square positions

        Returns:
            The positions of the current object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method for position

        Args:
            value : tuple
            the position of square object
        """
        try:
            self.__position = value

            err = "position must be a tuple of 2 positive integers"
            if len(position) != 2:
                raise TypeError(err)
            if not isinstance(position[0], int):
                raise TypeError(err)
            if not isinstance(position[1], int):
                raise TypeError(err)
            if position[0] < 0 or position[1] < 0:
                raise TypeError(error)
        except Exception as exception:
            raise exception

    def area(self):
        """
        Calculates the current sqare area

        Returns:
            The area of the current object
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the current sqare area """
        if self.__size == 0:
            print()
            return
        a, b = self.__position
        print("\n" * b)
        for i in range(self.__size):
            for y in range(a):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
