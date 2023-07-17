"""
Strategies module for the Nirvana project.

A strategy can be any function that takes a list as a parameter and returns an integer.
"""


def average(values: list) -> int:
    """Returns the `list` average."""
    return int(sum(values)/len(values))


def first(values: list) -> int:
    """Returns the `list` first element."""
    return values[0]


def last(values: list) -> int:
    """Returns the `list` last element."""
    return values[-1]
