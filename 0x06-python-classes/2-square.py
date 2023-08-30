#!/usr/bin/python3
""" Defining a Class For task Two. """


class Square:
    """ Initializing main method """
    def __init__(self, size):
        """ creates instance private attribute
        with condition of type and value error
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
