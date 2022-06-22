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
