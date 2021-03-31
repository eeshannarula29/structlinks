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
class TestMergeSort:
    def test_unsortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        actual = mergesort(test_list)
        expected = sorted(test_list)

        assert actual == expected


    def test_sortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        actual = mergesort(test_list)
        expected = sorted(test_list)

        assert actual == expected


    def test_reversedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        actual = mergesort(test_list)
        expected = sorted(test_list)

        assert actual == expected


########################################
# Quick sort (In Place)
########################################
class TestInPlaceQuickSort:
    def test_unsortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        expected = sorted(test_list.copy())
        quicksort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_sortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        expected = sorted(test_list.copy())
        quicksort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_reversedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        expected = sorted(test_list.copy())
        quicksort(test_list)
        actual = test_list.copy()

        assert actual == expected


########################################
# Quick sort (Out of Place)
########################################
class TestOutPlaceQuickSort:
    def test_unsortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        actual = out_place_quicksort(test_list)
        expected = sorted(test_list)

        assert actual == expected


    def test_sortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        actual = out_place_quicksort(test_list)
        expected = sorted(test_list)

        assert actual == expected


    def test_reversedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        actual = out_place_quicksort(test_list)
        expected = sorted(test_list)

        assert actual == expected


########################################
# Selection Sort
########################################
class TestSelectionSort:
    def test_unsortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        expected = sorted(test_list.copy())
        selection_sort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_sortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        expected = sorted(test_list.copy())
        selection_sort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_reversedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        expected = sorted(test_list.copy())
        selection_sort(test_list)
        actual = test_list.copy()

        assert actual == expected


########################################
# Insertion Sort
########################################
class TestInsertionSort:
    def test_unsortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        expected = sorted(test_list.copy())
        insertion_sort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_sortedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        expected = sorted(test_list.copy())
        insertion_sort(test_list)
        actual = test_list.copy()

        assert actual == expected


    def test_reversedlist(self) -> None:
        """Test mergesort on an unsorted list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        expected = sorted(test_list.copy())
        insertion_sort(test_list)
        actual = test_list.copy()

        assert actual == expected