#!/usr/bin/python3
"""module that defines a class called mylist"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        """prints sorted version of the object"""
        ans = sorted(self)
        print(ans)
