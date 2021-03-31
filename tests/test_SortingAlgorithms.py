"""This file contains tests for SortingAlgorithms.py.

Because it exists in a /tests/ folder, it adds the
current working directory to PYTHONPATH, in order to 'see'
the functions it is testing
"""

# Add the root directory to PYTHONPATH
import sys
sys.path.append('.')

from SortingAlgorithms import *


########################################
# Quick sort (In Place)
########################################
def test_mergesort_unsortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

    actual = mergesort(test_list)
    expected = sorted(test_list)

    assert actual == expected


def test_mergesort_sortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    actual = mergesort(test_list)
    expected = sorted(test_list)

    assert actual == expected


def test_mergesort_reversedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    actual = mergesort(test_list)
    expected = sorted(test_list)

    assert actual == expected


########################################
# Quick sort (In Place)
########################################
def test_quicksort_unsortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

    expected = sorted(test_list.copy())
    quicksort(test_list)
    actual = test_list.copy()

    assert actual == expected


def test_quicksort_sortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    expected = sorted(test_list.copy())
    quicksort(test_list)
    actual = test_list.copy()

    assert actual == expected


def test_quicksort_reversedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    expected = sorted(test_list.copy())
    quicksort(test_list)
    actual = test_list.copy()

    assert actual == expected


########################################
# Quick sort (Out of Place)
########################################
def test_out_quicksort_unsortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

    actual = out_place_quicksort(test_list)
    expected = sorted(test_list)

    assert actual == expected


def test_out_quicksort_sortedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    actual = out_place_quicksort(test_list)
    expected = sorted(test_list)

    assert actual == expected


def test_out_quicksort_reversedlist() -> None:
    """Test mergesort on an unsorted list"""
    test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    actual = out_place_quicksort(test_list)
    expected = sorted(test_list)

    assert actual == expected