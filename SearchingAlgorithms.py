"""
A re-implementation of several searching algorithms, including:
    - Binary Search

Many of these sort are inspired by their implementations in the CSC111
University of Toronto Course.
"""

from typing import Any


def linear_search(lst: list, item: Any) -> bool:
    """Return a boolean representing whether or not the given item
    exists in the list.
    """
    # Iterate through all items in the list
    for i in lst:
        if item == i:  # If the target item is found
            return True

    # If we reach this point, the item is not in the list
    return False


def binary_search(lst: list, item: Any) -> bool:
    """Return a boolean representing whether or not the given item
    exists in the list.

    Preconditions:
        - lst must be sorted
    """
    # Initialize our upper and lower bounds of the search area
    b = 0
    e = len(lst)

    # We will have verified the entire list when b >= e
    while b < e:
        # Get the middle index
        m = (e + b) // 2

        # Check if the middle item is the target
        if lst[m] == item:
            return True
        elif lst[m] < item:
            e = m
        else:
            b = m + 1

    # If we reach this point, the item is not in the list
    return False
