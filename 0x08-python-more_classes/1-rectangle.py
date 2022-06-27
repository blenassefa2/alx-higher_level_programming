#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a class for a rectangle """


class Rectangle:
    """This is a rectangle class """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for rectangle

        Parameters
        ----------
        width : int
            the width of rectangle object
        height: int
            the height of rectangle object
        """
        try:
            self.__height = height
            self.__width = width
            typerr = "must be an integer"
            valerr = "must be >= 0"
            if not isinstance(width, int):
                raise TypeError("width " + typerr)
            if width < 0:
                raise ValueError("width " + valerr)
            if not isinstance(height, int):
                raise TypeError("height " + typerr)
            if height < 0:
                raise ValueError("height " + valerr)
        except Exception as exception:
            raise exception

    @property
    def height(self):
        """
        gets the current rectangle's height

        Returns:
            The height of the current object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height

        Args:
            value : int
            the height of rectangle object
        """
        try:
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        except Exception as exception:
            raise exception

    @property
    def width(self):
        """
        gets the current width

        Returns:
            The width of the current object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width

        Args:
            value : int
            the new width of rectangle object
        """

        try:
            self.__width = value

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
        except Exception as exception:
            raise exception
