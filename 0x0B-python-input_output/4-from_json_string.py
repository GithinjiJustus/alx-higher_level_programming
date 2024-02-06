#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json

def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
