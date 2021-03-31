"""
A re-implementation of several sorting algorithms, includeing:
    - Merge sort
    - Quick sort
    - Selection sort
    - Insertion sort

Many of these sort are inspired by the implementation of the CSC111
University of Toronto Course
"""


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
