#!/usr/bin/python3
"""this module consists a function"""


def add_attribute(obj, name, value):
    """
    functions that adds new attribute to an object

    Parameters
    ----------
        obj : object
            object where we are adding new attr
        name : string
            name of new attribute
        value : object
            value of new attribute
    Raise
    -----
        TypeError - can't add new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
