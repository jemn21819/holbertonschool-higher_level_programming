#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
class Node that defines a node of a
singly linked list
"""


class Node:
    """
    class Node that defines a node
    of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Attributes:
            __data (int): to add
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ just a property func"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ Just a property func"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ just a setter fuc"""
        if type(value) is not Node and value is not None:
            raise TypeError("ext_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class to store singly linked list of Node objects"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            head = self.__head
            if value < head.data:
                node.next_node = head
                self.__head = node
                return
            while head.next_node is not None:
                if value < head.next_node.data:
                    node.next_node = head.next_node
                    head.next_node = node
                    break
                head = head.next_node
            head.next_node = node

    def __str__(self):
        head = self.__head
        p_class = ""
        if head is None:
            return p_class
        while head.next_node is not None:
            p_class += format(head.data, 'd')
            p_class += '\n'
            head = head.next_node
        p_class += format(head.data, 'd')
        return p_class
