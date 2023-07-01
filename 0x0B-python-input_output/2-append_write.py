#!/usr/bin/python3
"""defines a file appending function"""


def append_write(filename="", text=""):
    """writes a str to a text file, returns the number of chars written."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
