"""This file contains tests for SortingAlgorithms.py.
"""
from SortingAlgorithms import *
from LinkedList import *
from DoublyLinkedList import *

from typing import Optional, Callable


########################################
# Base tests for non-mutating sorts
########################################
class BaseNoMutatingSort:
    """The base class for a suit of tests that work with in place sorting algorithms.

    Inherit from this class and assign an algorithm to be used in the tests.
    """
    algorithm: Callable[[], None] = staticmethod(None)

    def test_unsortedlist(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        actual = self.algorithm(test_list)
        expected = sorted(test_list)

        assert actual == expected

    def test_sortedlist(self) -> None:
        """Test algorithm on a sorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        actual = self.algorithm(test_list)
        expected = sorted(test_list)

        assert actual == expected

    def test_reversedlist(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        actual = self.algorithm(test_list)
        expected = sorted(test_list)

        assert actual == expected

    def test_key_reverse(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        actual = self.algorithm(test_list, (lambda x: -x))
        expected = sorted(test_list, key=(lambda x: -x))

        assert actual == expected

    def test_unsorted_linked_list(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = LinkedList([9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_sorted_linked_list(self) -> None:
        """Test algorithm on a sorted list"""
        test_list = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_reversed_linked_list(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = LinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_key_reverse_linked_list(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = LinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        actual = self.algorithm(test_list, (lambda x: -x)).to_list()
        expected = sorted(test_list.to_list(), key=(lambda x: -x))

        assert actual == expected

    def test_unsorted_doubly_linked_list(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = DoublyLinkedList([9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_sorted_doubly_linked_list(self) -> None:
        """Test algorithm on a sorted list"""
        test_list = DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_reversed_doubly_linked_list(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        actual = self.algorithm(test_list).to_list()
        expected = sorted(test_list.to_list())

        assert actual == expected

    def test_key_reverse_doubly_linked_list(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        actual = self.algorithm(test_list, (lambda x: -x)).to_list()
        expected = sorted(test_list.to_list(), key=(lambda x: -x))

        assert actual == expected


########################################
# Base tests for mutating sorts
########################################
class BaseInPlaceSort:
    """The base class for a suit of tests that work with in place sorting algorithms.

    Inherit from this class and assign an algorithm to be used in the tests.
    """
    algorithm: Callable[[], None] = staticmethod(None)

    def test_unsortedlist(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = [9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200]

        expected = sorted(test_list.copy())
        self.algorithm(test_list)
        actual = test_list.copy()

        assert actual == expected

    def test_sortedlist(self) -> None:
        """Test algorithm on an sorted list"""
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        expected = sorted(test_list.copy())
        self.algorithm(test_list)
        actual = test_list.copy()

        assert actual == expected

    def test_reversedlist(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        expected = sorted(test_list.copy())
        self.algorithm(test_list)
        actual = test_list.copy()

        assert actual == expected

    def test_key_reverse(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        self.algorithm(test_list, (lambda x: -x))
        actual = test_list.copy()
        expected = sorted(test_list.copy(), key=(lambda x: -x))

        assert actual == expected

    def test_unsorted_linked_list(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = LinkedList([9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_sorted_linked_list(self) -> None:
        """Test algorithm on an sorted list"""
        test_list = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_reversed_linked_list(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = LinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_key_reverse_linked_list(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = LinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        self.algorithm(test_list, (lambda x: -x))
        actual = test_list.to_list()
        expected = sorted(test_list.to_list(), key=(lambda x: -x))

        assert actual == expected

    def test_unsorted_doubly_linked_list(self) -> None:
        """Test algorithm on an unsorted list"""
        test_list = DoublyLinkedList([9, 7, 5, 2, 4, 5, 3, 3, 2, 1, 10, 200])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_sorted_doubly_linked_list(self) -> None:
        """Test algorithm on an sorted list"""
        test_list = DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_reversed_doubly_linked_list(self) -> None:
        """Test algorithm on a reversed list"""
        test_list = DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        expected = sorted(test_list.to_list())
        self.algorithm(test_list)
        actual = test_list.to_list()

        assert actual == expected

    def test_key_reverse_doubly_linked_list(self) -> None:
        """Test algorithm on a list, sort with a reversing key."""
        test_list = DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        self.algorithm(test_list, (lambda x: -x))
        actual = test_list.to_list()
        expected = sorted(test_list.to_list(), key=(lambda x: -x))

        assert actual == expected


class TestNoMutatingMergesort(BaseNoMutatingSort):
    """Test the non-mutating mergesort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(no_mut_mergesort)


class TestInPlaceMergesort(BaseInPlaceSort):
    """Test the mutating mergesort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(mergesort)


class TestInPlaceQuicksort(BaseInPlaceSort):
    """Test the mutating quicksort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(quicksort)


class TestNoMutatingQuicksort(BaseNoMutatingSort):
    """Test the non-mutating quicksort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(no_mut_quicksort)


class TestInPlaceInsertionSort(BaseInPlaceSort):
    """Test the mutating insertionsort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(insertion_sort)


class TestInPlaceSelectionSort(BaseInPlaceSort):
    """Test the mutating selection sort algorithm"""
    algorithm: Optional[tuple[Callable[[list], None]]] = staticmethod(selection_sort)
