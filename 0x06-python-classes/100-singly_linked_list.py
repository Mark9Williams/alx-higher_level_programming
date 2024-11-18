#!/usr/bin/python3
""" a class Node that defines a node of a singly linked list by """


class Node:
    """ defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ Called at instantiation of a class object """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets or modifies the value of data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrives the value of next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next_node of the instance node """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class that defines a singly linked list """

    def __init__(self):
        """ Instantiates a singly linked list """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node into the correct sorted position in the list """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """ Prints the representation of the singly linked list """
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
