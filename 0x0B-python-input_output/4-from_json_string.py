#!/usr/bin/python3
"""Defines a deserialization function."""
import json


def from_json_string(my_str):
    """deserializes a json string"""
    return json.loads(my_str)
