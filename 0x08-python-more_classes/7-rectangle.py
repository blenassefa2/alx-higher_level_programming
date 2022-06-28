#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a class for a rectangle """


class Rectangle:
    """This is a rectangle class """

    number_of_instances = 0
    print_symbol = "#"

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
            Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculates area

        Returns:
            area of current instance
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        calculates perimeter

        Returns:
            perimeter of current object
        """
        if not self.__height or not self.__width:
            return 0
        return (2 * self.__height) + (self.__width * 2)

    def __str__(self):
        """makes object printable"""
        s = ""
        if not self.__height or not self.__width:
            return s
        for i in range(self.__height):
            s += f"{self.print_symbol}"*self.__width + "\n"

        return s[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
