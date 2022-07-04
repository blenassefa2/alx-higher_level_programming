#!/usr/bin/python3
"""this module defines a function"""

def inherits_from(obj, a_class):
    """checks if object is an instance of class inherited"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
    
