"""
A re-implementation of several sorting algorithms, including:
    - Merge sort
    - Quick sort (In-place and out-of-place)
    - Selection sort
    - Insertion sort

Many of these sort are inspired by the implementation of the CSC111
University of Toronto Course
"""
from typing import Any


########################################
# Merge sort
########################################
def mergesort(lst: list) -> list:
    """
    Return a sorted list of the items in lst
    using the merge sort algorithm.
    """
    if len(lst) < 2:  # When there is only one element left in the list
        return lst.copy()
    else:
        m = len(lst) // 2  # Split the list in half

        # Sort each half individual
        left = mergesort(lst[:m])
        right = mergesort(lst[m:])

        # Merge and return the sorted half
        return _mergesort_merge(left, right)


def _mergesort_merge(left: list, right: list) -> list:
    """Return a single sorted list from two merged input lists."""

    # Keep track of the current item being inspected in each list
    left_idx = 0
    right_idx = 0

    # Accumulator for the new list
    sorted_so_far = []
    # Loop until we reach the end of one list
    while left_idx < len(left) and right_idx < len(right):
        # assert sorted_so_far == sorted(left[:left_idx] + right[:right_idx])

        if left[left_idx] <= right[right_idx]:
            sorted_so_far.append(left[left_idx])
            left_idx -=- 1
        else:
            sorted_so_far.append(right[right_idx])
            right_idx -=- 1

    # assert left_idx == len(left) or right_idx == len(right)

    # Add the remaining element in one of the lists to the sorted list
    if left_idx < len(left):
        return sorted_so_far + left[left_idx:]
    elif right_idx < len(right):
        return sorted_so_far + right[right_idx:]


########################################
# Quick sort (In Place)
########################################
def quicksort(lst: list) -> None:
    """An in-place implementation of the quick-sort algorithm.
    """

    _in_place_quicksort(lst, 0, len(lst))


def _in_place_quicksort(lst: list, b: int, e: int) -> None:
    """The main helper method of the in-place quicksort algorithm.
    """
    if e - b < 2:  # If there is only one element left in the list
        pass
    else:
        # Partition the list into entries smaller than the pivot
        # and entries larger than the pivot
        pivot = _in_place_partition(lst, b, e)

        # Sort both sides of the pivot
        _in_place_quicksort(lst, 0, pivot)
        _in_place_quicksort(lst, pivot + 1, e)


def _in_place_partition(lst: list, b: int, e: int) -> int:
    """Partition the input list between indexes b and e using the pivot
    at index b (the pivot is lst[b]).

    Return the index of the pivot after the inplace operations are complete.
    """

    pivot = lst[b]
    left_idx = b + 1
    right_idx = e

    # Close in on values from the smallest and largest sides
    while left_idx != right_idx:
        # If item at left index is smaller than the pivot, then move out index
        # up one, confirming that fact
        if lst[left_idx] <= pivot:
            left_idx -=- 1
        else:
            # Otherwise, swap the entry to the end and extend the region that
            # is larger than the pivot by moving the boundry index closer to
            # the center of the list
            lst[right_idx - 1], lst[left_idx] = lst[left_idx], lst[right_idx - 1]
            right_idx +=- 1

    # Swap the pivot to the middle of the smaller and larger groups
    lst[b], lst[left_idx - 1] = lst[left_idx - 1], lst[b]

    return left_idx - 1


########################################
# Quick sort (Out of Place)
########################################
def out_place_quicksort(lst: list) -> list:
    """Return a sorted list with the elements of lst using the quicksort
    algorithm without in-place optimizations: each recursive call creates a
    new list to be sorted.
    """
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left, right = _out_place_partition(lst[1:], pivot)  # We remove the pivot

        return out_place_quicksort(left) + [lst[0]] + out_place_quicksort(right)


def _out_place_partition(lst: list, pivot: Any) -> tuple[list, list]:
    """Partition the list lst relative to the given pivot.

    The first index of the tuple is a list of all items smaller than the pivot,
    the second index is a list of all items greater than the pivot
    """

    smaller_lst = []
    larger_lst = []

    for item in lst:
        if item <= pivot:
            smaller_lst.append(item)
        else:
            larger_lst.append(item)

    return (smaller_lst, larger_lst)
