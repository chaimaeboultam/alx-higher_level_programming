#!/usr/bin/python3
"""
Module for adding two integers.
"""

def add_integer(a, b=98):
     """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
