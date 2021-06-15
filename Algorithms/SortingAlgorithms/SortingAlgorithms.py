"""
A re-implementation of several sorting algorithms, including:
    - Merge sort
    - Quick sort (In-place and out-of-place)
    - Selection sort
    - Insertion sort

Many of these sort are inspired by their implementations in the CSC111
University of Toronto Course.

Implementation Notes:
    - Non-mutating algorithms are explicitely prefixed with no_mut_
    - Every top level sorting algorithm (the main function of that algorithm)
        has a default value for key, (lambda x: x) which does not modify it's input
"""
from typing import Any, Callable, Union
from structlinks.DoublyLinkedList import DoublyLinkedList
from structlinks.LinkedList import LinkedList


########################################
# Merge sort (In-place)
########################################
def mergesort(lst: Union[list, LinkedList, DoublyLinkedList],
              key: Callable[[Any], Any] = (lambda x: x)) -> None:
    """
    Return a sorted list of the items in lst
    using the merge sort algorithm.

    This algorithm is heavily based off 'Approach 2' by Krikti,
    https://www.geeksforgeeks.org/in-place-merge-sort/
    """
    _in_place_mergesort(lst, 0, len(lst), key)


def _in_place_mergesort(lst: Union[list, LinkedList, DoublyLinkedList],
                        b: int, e: int, key: Callable[[Any], Any]) -> None:
    if e - b < 2:  # When there is only one element left in the list
        return
    else:
        m = ((e - b) // 2) + b  # Split the list in half

        # Sort each half individual
        _in_place_mergesort(lst, b, m, key)
        _in_place_mergesort(lst, m, e, key)

        # Merge and return the sorted half
        return _in_place_merge(lst, b, e, key)


def _in_place_merge(lst: Union[list, LinkedList, DoublyLinkedList],
                    b: int, e: int, key: Callable[[Any], Any]) -> None:
    """Return a single sorted list from two merged input lists."""

    # The initial gap between swappable elements
    gap = ((e - b + 1) + 1) // 2

    while gap > 0:
        for i in range(b, e - gap):
            j = i + gap
            if key(lst[j]) < key(lst[i]):
                lst[j], lst[i] = lst[i], lst[j]

        if gap <= 1:
            gap = 0
        else:
            # The +1 forces the ceiling of (gap / 2)
            gap = (gap + 1) // 2


########################################
# Merge sort (Non-mutating)
########################################
def no_mut_mergesort(lst: Union[list, LinkedList, DoublyLinkedList],
                     key: Callable[[Any], Any] = (lambda x: x)) -> \
        Union[list, LinkedList, DoublyLinkedList]:
    """
    Return a sorted list of the items in lst
    using the merge sort algorithm.
    """
    if isinstance(lst, LinkedList):
        return LinkedList(no_mut_mergesort(lst.to_list(), key))

    elif isinstance(lst, DoublyLinkedList):
        return DoublyLinkedList(no_mut_mergesort(lst.to_list(), key))

    else:
        if len(lst) < 2:  # When there is only one element left in the list
            return lst.copy()
        else:
            m = len(lst) // 2  # Split the list in half

            # Sort each half individual
            left = no_mut_mergesort(lst[:m], key)
            right = no_mut_mergesort(lst[m:], key)

            # Merge and return the sorted half
            return _no_mut_mergesort_merge(left, right, key)


def _no_mut_mergesort_merge(left: list, right: list, key: Callable[[Any], Any]) -> list:
    """Return a single sorted list from two merged input lists."""

    # Keep track of the current item being inspected in each list
    left_idx = 0
    right_idx = 0

    # Accumulator for the new list
    sorted_so_far = []
    # Loop until we reach the end of one list
    while left_idx < len(left) and right_idx < len(right):
        # assert sorted_so_far == sorted(left[:left_idx] + right[:right_idx], key=key)

        if key(left[left_idx]) <= key(right[right_idx]):
            sorted_so_far.append(left[left_idx])
            left_idx -= - 1
        else:
            sorted_so_far.append(right[right_idx])
            right_idx -= - 1

    assert left_idx == len(left) or right_idx == len(right)

    # Add the remaining element in one of the lists to the sorted list
    if left_idx < len(left):
        return sorted_so_far + left[left_idx:]
    elif right_idx < len(right):
        return sorted_so_far + right[right_idx:]


########################################
# Quick sort (In Place)
########################################
def quicksort(lst: Union[list, LinkedList, DoublyLinkedList],
              key: Callable[[Any], Any] = (lambda x: x)) -> None:
    """An in-place implementation of the quick-sort algorithm.
    """

    _in_place_quicksort(lst, 0, len(lst), key)


def _in_place_quicksort(lst: Union[list, LinkedList, DoublyLinkedList],
                        b: int, e: int, key: Callable[[Any], Any]) -> None:
    """The main helper method of the in-place quicksort algorithm.
    """
    if e - b < 2:  # If there is only one element left in the list
        pass
    else:
        # Partition the list into entries smaller than the pivot
        # and entries larger than the pivot
        pivot = _in_place_partition(lst, b, e, key)

        # Sort both sides of the pivot
        _in_place_quicksort(lst, 0, pivot, key)
        _in_place_quicksort(lst, pivot + 1, e, key)


def _in_place_partition(lst: Union[list, LinkedList, DoublyLinkedList],
                        b: int, e: int, key: Callable[[Any], Any]) -> int:
    """Partition the input list between indexes b and e using the pivot
    at index b (the pivot is lst[b]).

    Return the index of the pivot after the inplace operations are complete.
    """

    pivot = key(lst[b])
    left_idx = b + 1
    right_idx = e

    # Close in on values from the smallest and largest sides
    while left_idx != right_idx:
        # If item at left index is smaller than the pivot, then move out index
        # up one, confirming that fact
        if key(lst[left_idx]) <= pivot:
            left_idx -= - 1
        else:
            # Otherwise, swap the entry to the end and extend the region that
            # is larger than the pivot by moving the boundry index closer to
            # the center of the list
            lst[right_idx - 1], lst[left_idx] = lst[left_idx], lst[right_idx - 1]
            right_idx += - 1

    # Swap the pivot to the middle of the smaller and larger groups
    lst[b], lst[left_idx - 1] = lst[left_idx - 1], lst[b]

    return left_idx - 1


########################################
# Quick sort (Non-mutating)
########################################
def no_mut_quicksort(lst: Union[list, LinkedList, DoublyLinkedList],
                     key: Callable[[Any], Any] = (lambda x: x)) -> \
        Union[list, LinkedList, DoublyLinkedList]:
    """Return a sorted list with the elements of lst using the quicksort
    algorithm without in-place optimizations: each recursive call creates a
    new list to be sorted.
    """
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left, right = _no_mut_partition(lst[1:], pivot, key)  # We remove the pivot

        middle = [lst[0]]

        if isinstance(lst, LinkedList):
            middle = LinkedList(middle)

        if isinstance(lst, DoublyLinkedList):
            middle = DoublyLinkedList(middle)

        return no_mut_quicksort(left, key) + middle + no_mut_quicksort(right, key)


def _no_mut_partition(lst: Union[list, LinkedList, DoublyLinkedList],
                      pivot: Any, key: Callable[[Any], Any]) -> \
        tuple[Union[list, LinkedList, DoublyLinkedList],
              Union[list, LinkedList, DoublyLinkedList]]:
    """Partition the list lst relative to the given pivot.

    The first index of the tuple is a list of all items smaller than the pivot,
    the second index is a list of all items greater than the pivot
    """

    smaller_lst = []
    larger_lst = []

    if isinstance(lst, LinkedList):
        smaller_lst = LinkedList()
        larger_lst = LinkedList()

    if isinstance(lst, DoublyLinkedList):
        smaller_lst = DoublyLinkedList()
        larger_lst = DoublyLinkedList()

    for item in lst:
        if key(item) <= key(pivot):
            smaller_lst.append(item)
        else:
            larger_lst.append(item)

    return (smaller_lst, larger_lst)


########################################
# Selection Sort
########################################
def selection_sort(lst: Union[list, LinkedList, DoublyLinkedList],
                   key: Callable[[Any], Any] = (lambda x: x)) -> None:
    """An in-place (mutating) implementation of the selection sort algorithm.
    """

    # Build a sorted list from the smallest elements in the unsorted portion of
    # the list
    for idx in range(len(lst)):
        min_index = _smallest_index(lst, idx, key)
        lst[idx], lst[min_index] = lst[min_index], lst[idx]


def _smallest_index(lst: Union[list, LinkedList, DoublyLinkedList],
                    i: int, key: Callable[[Any], Any]) -> int:
    """Return the index of the smallest item in the sublist lst[i:]
    """

    # Extract the smallest item
    smallest_so_far = i
    for idx in range(i + 1, len(lst)):
        if key(lst[smallest_so_far]) > key(lst[idx]):
            smallest_so_far = idx

    return smallest_so_far


########################################
# Selection Sort
########################################
def insertion_sort(lst: Union[list, LinkedList, DoublyLinkedList],
                   key: Callable[[Any], Any] = (lambda x: x)) -> None:
    """An in-place (mutating) implementation of the insertion sort algorithm.
    """
    for idx in range(0, len(lst)):
        _insert(lst, idx, key)


def _insert(lst: Union[list, LinkedList, DoublyLinkedList],
            i: int, key: Callable[[Any], Any]) -> None:
    """Move lst[i] so that lst[:i + 1] is sorted.
    """
    idx = i

    # "Shift" the item at index to the left until the item is greater than the item
    # in the index before it
    while idx > 0 and key(lst[idx]) < key(lst[idx - 1]):
        lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]

        idx -= 1
