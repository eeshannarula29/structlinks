"""This file contains tests for SortingAlgorithms.py.
"""
from typing import Optional, Callable, Any

from SearchingAlgorithms import *


########################################
# Base tests for searching algorithms
########################################
class BaseSearch:
    """The base class for the series of tests that
    evaluate the efficacy of searching functions.
    """
    algorithm: Callable[[list, Any], bool] = staticmethod(None)

    def test_sorted_list_first_true(self) -> None:
        """Test the searching algorithm on a sorted list
        for the item at the first index."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        assert self.algorithm(lst, 0)

    def test_sorted_list_middle_true(self) -> None:
        """Test the searching algorithm on a sorted list.
        for the item at the middle index."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        assert self.algorithm(lst, 5)

    def test_sorted_list_last_true(self) -> None:
        """Test the searching algorithm on a sorted list.
        for the item at the last index."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        assert self.algorithm(lst, 8)

    def test_sorted_list_false(self) -> None:
        """Test the searching algorithm on a sorted list
        for an item not in the list."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        assert not self.algorithm(lst, 4.5)

    def test_sorted_list_odd_length(self) -> None:
        """Test the searching algorithm on a sorted list of odd length."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        assert self.algorithm(lst, 7)

    def test_sorted_list_even_length(self) -> None:
        """Test the searching algorithm on a sorted list of even length."""
        lst = [0, 1, 2, 3, 4, 5, 6, 7]

        assert self.algorithm(lst, 7)

    def test_empty_list(self) -> None:
        """Test the searching algorithm on an empty list."""
        lst = []

        assert not self.algorithm(lst, 7)


class TestLinearSearch(BaseSearch):
    """Test the mutating selection sort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(linear_search)

    def test_unsorted_list_odd_length(self) -> None:
        """Test the searching algorithm on an unsorted list
        of odd length."""
        lst = [2, 3, 1, 2, 7, 3, 4]

        assert self.algorithm(lst, 7)

    def test_unsorted_list_even_length(self) -> None:
        """Test the searching algorithm on an unsorted list
        of even length."""
        lst = [2, 3, 1, 2, 7, 9, 8, 5, 3, 4]

        assert self.algorithm(lst, 7)

class TestBinarySearch(BaseSearch):
    """Test the mutating selection sort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(linear_search)