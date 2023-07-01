#!/usr/bin/python3
"""defines a file writing function"""


def write_file(filename="", text=""):
    """writes a str to a text file, returns the number of chars written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
