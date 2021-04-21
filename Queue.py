"""The file contains Queue class. The basic structure of the class id taken from the
University of Toronto's CSC110 course

This implementation of Queue is done on doubly linked lists.
"""
from __future__ import annotations

from structlinks.DoublyLinkedList import *
from structlinks.SortingAlgorithms import quicksort

from typing import *


class Queue:
    """Represents a queue datatype"""
    def __init__(self, items: Optional[list] = None,
                 metric: Optional[Callable] = None,
                 limit: Optional[int] = None) -> None:

        self._items = DoublyLinkedList(items if items else [])
        self._metric = metric
        self._limit = limit

        if self._limit:
            while len(self._items) > self._limit:
                self._items.pop(0)

        if self._metric:
            quicksort(self._items, self._metric)

    @property
    def is_empty(self) -> bool:
        """Return whether this queue contains no items.
        """
        return len(self._items) == 0

    @property
    def is_filled(self) -> bool:
        """Return weather the queue us filled or not"""
        return self._limit and len(self._items) >= self._limit

    def copy(self) -> Queue:
        return Queue(items=self._items.to_list(), metric=self._metric, limit=self._limit)

    def __copy__(self) -> Queue:
        return Queue(items=self._items.to_list(), metric=self._metric, limit=self._limit)

    def to_list(self) -> list:
        """Return list representation of queue"""
        return self._items.to_list()

    def change_limit(self, limit: int) -> None:
        """Change the limit of the queue"""
        self._limit = limit

        if self._limit:
            while len(self._items) > self._limit:
                self._items.pop(0)

    def change_metric(self, metric: Callable) -> None:
        """Change the metric of the queue to <metric>"""
        self._metric = metric

        if self._metric:
            quicksort(self._items, self._metric)

    def enqueue(self, item) -> None:
        """put the item in the queue

        Raise an QueueLimitReachedError if this queue is full.
        """
        if not self._limit or self._limit > len(self._items):
            self._items.insert(0, item)

            if self._metric:
                quicksort(self._items, self._metric)
        else:
            raise QueueLimitReachedError

    def dequeue(self) -> Any:
        """Remove and return the item at the front of this queue.

        Raise an EmptyQueueError if this queue is empty."""
        if self.is_empty:
            raise EmptyQueueError
        else:
            return self._items.pop(len(self._items) - 1)

    def extend(self, other: Queue) -> None:
        """Extend self by other queue"""
        other_elements = other.to_list()

        while not self.is_filled and not other_elements == []:
            self.enqueue(other_elements.pop())

    def __len__(self) -> int:
        return len(self._items)

    def map(self, key: Callable) -> None:
        self._items = self._items.map(key)

    def update(self) -> None:
        """Update the order of the queue"""
        if self._metric:
            quicksort(self._items, self._metric)

    def display(self, key: Optional[Callable] = lambda x: x) -> None:
        string_so_far = ''

        temp = ''

        items = self._items.to_list()

        for index, item in enumerate(items):
            if index < len(items) - 1:
                temp += f' {key(item)} ->'
            else:
                temp += f' {key(item)}'

        string_so_far += 'Entry ' + '-' * len(temp) + '> Exit \n'

        string_so_far += '     ' + temp + '\n'

        string_so_far += '------' + '-' * len(temp) + '------'

        print(string_so_far)

    def __str__(self) -> str:
        return '[' + ' -> '.join([str(element) for element in self._items]) + ']'

    def __repr__(self) -> str:
        return f'Queue({self.__str__()})'


class EmptyQueueError(Exception):
    """Exception raised when calling dequeue on an empty queue.

    the exception is taken from University of Toronto's CSC110 course notes.
    """

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'dequeue may not be called on an empty queue'


class QueueLimitReachedError(Exception):
    """Exception raised when calling dequeue on an filled queue.
    """

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'dequeue may not be called on an filled queue'
