#!/usr/bin/python3
"""Defines a class that inherits from list."""


class Mylist(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Prints a list sorted in ascending order."""
        print(sorted(self))
