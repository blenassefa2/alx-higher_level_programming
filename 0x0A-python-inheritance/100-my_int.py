#!/usr/bin/python3
"""creates a rebelious class MyInt"""


class MyInt(int):
    """rebelous class that inherits from int"""

    def __eq__(self, other):
        """
        Overloads == sign

        Args:
            other : int
                integer to be compared
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Overloads != sign

        Args:
            other : int
                integer to be compared
        """
        return int(self) == int(other)
