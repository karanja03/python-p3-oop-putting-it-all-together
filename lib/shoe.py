#!/usr/bin/env python3

class Shoe:
    '''Represents a shoe.'''
    
class Shoe:
    '''Represents a shoe.'''

    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private variable to store the size
        self.size = size  # Check if size is an integer when setting it
        self.condition = "New"  # Initialize condition attribute

    def size(self):
        return self._size

    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
 