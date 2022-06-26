#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a module for node and slingly linked classes"""


class Node:
    """This is a Node class """

    def __init__(self, data, next_node=None):
        """
        Constructs all the necessary attributes for a Node

        Parameters
        ----------
        data : int
            data stored in the node
        next_node: Node
            the node next to current node
        """
        try:
            self.__data = data
            self.__next_node = next_node

            if not isinstance(data, int):
                raise TypeError("data must be an integer")

            if next_node:
                if not isinstance(next_node, Node):
                    raise TypeError("next_node must be a Node object")

        except Exception as exception:
            raise exception

    @property
    def data(self):
        """
        gets the current data

        Returns:
            The data of the current object
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter method for data

        Args:
            value : int
            the data of node object
        """
        try:
            self.__data = value
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
        except Exception as exception:
            raise exception

    @property
    def next_node(self):
        """
        gets the next Node object

        Returns:
            The next node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter method for next_node

        Args:
            value : Node
            the new node next to current node
        """

        try:
            self.__next_node = value

            if value:
                if not isinstance(value, Node):
                    raise TypeError("next_node must be a Node object")

        except Exception as exception:
            raise exception


class SinglyLinkedList:
    """A class that defines singly linked list object"""

    def __init__(self):
        """Defines all necessary elements for the object"""
        self.__head = Node(0)

    def sorted_insert(self, value):
        """
        inserts nodes to list object in increasing order

        Args:
            value : int
                the data of new node
        """
        temp = self.__head.next_node
        temp2 = self.__head
        while temp and value > temp.data:
            temp2 = temp2.next_node
            temp = temp.next_node
        temp2.next_node = Node(value, temp)

    def __str__(self):
        """Method that enables printing the object"""
        temp = self.__head.next_node
        s = ""

        while temp:
            s = s + str(temp.data) + "\n"
            temp = temp.next_node
        return s[:-1]
