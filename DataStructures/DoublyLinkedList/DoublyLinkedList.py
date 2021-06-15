""" The file contains _DoubleNode and DoublyLinkedList class. Both of the classes have
ideas taken from University of Toronto's CSC111 course.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Sequence, Union, Callable
import math


@dataclass
class _DoubleNode:
    """A node in a doubly-linked list.

    The class is taken from University of Toronto's CSC111 course
    """
    item: Any
    prev: Optional[_DoubleNode] = None
    next: Optional[_DoubleNode] = None


class DoublyLinkedList:
    """The class represents a Doubly linked-list

    Idea for many of the methods is taken from the University of Toronto's CSC111 course
    """

    def __init__(self, items: Optional[Sequence] = None, first: Optional[_DoubleNode] = None,
                 last: Optional[_DoubleNode] = None) -> None:
        """Initialize a new doubly-linked list containing the given items.
        """

        if first and last:
            self._first = first
            self._last = last

            count = 0
            curr = self._first

            while curr is not None:
                count += 1
                curr = curr.next

            self._length = count
            return

        self._first = None
        self._last = None
        self._length = len(items) if items else 0

        if items:
            curr = None
            for item in items:
                if self._first is None:
                    self._first = _DoubleNode(item)
                    curr = self._first
                else:
                    new_node = _DoubleNode(item, curr)
                    curr.next = new_node
                    curr = curr.next
            self._last = curr

    def __len__(self) -> int:
        """Return the number of elements in this list.
        """
        return self._length

    def __getitem__(self, i: Union[int, slice]) -> Union[Any, DoublyLinkedList]:
        """Return the item stored at index i in this linked list.
        """
        if isinstance(i, int):
            if i < 0:
                i = len(self) + i

            if i >= len(self):
                raise IndexError

            elif i <= len(self) / 2:
                curr = self._first
                curr_index = 0
                while curr is not None:
                    if i == curr_index:
                        return curr.item
                    curr = curr.next
                    curr_index += 1

            elif i >= len(self) / 2:
                curr = self._last
                curr_index = len(self) - 1
                while curr is not None:
                    if i == curr_index:
                        return curr.item
                    curr = curr.prev
                    curr_index -= 1

        elif isinstance(i, slice):
            start = i.start
            stop = i.stop

            if start is None:
                start = 0
            if stop is None:
                stop = self._length

            if not (0 <= start <= stop <= len(self)):
                raise IndexError
            else:
                new_linked_list = DoublyLinkedList([])
                index = 0

                for item in self:
                    if start <= index < stop:
                        new_linked_list.append(item)
                    index += 1

                return new_linked_list

    def append(self, item: Any) -> None:
        """
        Append the item to the end of the list
        """
        new_node = _DoubleNode(item, self._last)

        if len(self) == 0:
            self._first = self._last = new_node
            self._length += 1
            return

        self._last.next = new_node
        self._last = new_node
        self._length += 1

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list."""
        if len(self) == 0:
            return False

        elif len(self) % 2 != 0:
            curr_from_start = self._first
            curr_from_end = self._last

            while curr_from_start != curr_from_end:
                if curr_from_end.item == item or curr_from_start.item == item:
                    return True
                curr_from_start = curr_from_start.next
                curr_from_end = curr_from_end.prev
            if curr_from_start and curr_from_start.item == item:
                return True
            return False
        else:
            if self._first.item == item:
                return True
            curr_from_start = self._first.next
            curr_from_end = self._last

            while curr_from_start != curr_from_end:
                if curr_from_end.item == item or curr_from_start.item == item:
                    return True
                curr_from_start = curr_from_start.next
                curr_from_end = curr_from_end.prev
            if curr_from_start and curr_from_start.item == item:
                return True
            return False

    def insert(self, i: int, item: Any) -> None:
        """
        Insert the item at index i in the list
        """
        if i < 0:
            i = len(self) + i

        if i > len(self):
            raise IndexError

        elif i <= len(self) / 2:
            curr = self._first
            curr_index = 0

            if i == 0:
                if self._first:
                    new_node = _DoubleNode(item, next=self._first)
                    self._first.prev = new_node
                    self._first = new_node
                else:
                    self._first = _DoubleNode(item)
                    self._last = self._first
                self._length += 1
                return

            while curr is not None:
                if curr_index == i - 1:
                    new_node = _DoubleNode(item, curr, curr.next)
                    if curr.next:
                        curr.next.prev = new_node
                    curr.next = new_node
                    self._length += 1
                    return
                curr = curr.next
                curr_index += 1

        elif i > len(self) / 2:
            curr = self._last
            curr_index = len(self) - 1

            while curr is not None:
                if curr_index == i - 1:
                    new_node = _DoubleNode(item, curr, curr.next)
                    if curr.next:
                        curr.next.prev = new_node
                    curr.next = new_node
                    self._length -= 1
                    return
                curr = curr.prev
                curr_index -= 1

    def pop(self, i: int) -> Any:
        if i < 0:
            i = len(self) + i

        if i >= len(self):
            raise IndexError

        elif i <= len(self) / 2:
            curr = self._first
            curr_index = 0

            if i == 0:
                item = self._first.item
                self._first = self._first.next

                if self._first:
                    self._first.prev = None

                self._length -= 1
                return item

            while curr is not None:
                if curr_index == i:
                    if curr.next:
                        curr.next.prev = curr.prev
                        if curr.prev:
                            curr.prev.next = curr.next
                    else:
                        if curr.prev:
                            curr.prev.next = None

                    self._length -= 1
                    return curr.item

                curr = curr.next
                curr_index += 1

        elif i > len(self) / 2:
            curr = self._last
            curr_index = len(self) - 1

            if i == curr_index:
                item = self._last.item

                if self._last.prev:
                    self._last.prev.next = None
                    self._last = self._last.prev

                self._length -= 1
                return item

            while curr is not None:
                if curr_index == i:
                    if curr.next:
                        curr.next.prev = curr.prev
                        curr.prev.next = curr.next
                    else:
                        curr.prev.next = None
                    self._length -= 1
                    return curr.item

                curr = curr.prev
                curr_index -= 1

    def __setitem__(self, i: int, item: Any) -> None:
        """Store item at index i in this list.
        """
        if i < 0:
            i = self._length + i

        if i < (self._length / 2):
            current_index = 0
            curr = self._first

            while curr is not None:
                if current_index == i:
                    curr.item = item

                curr = curr.next
                current_index += 1

        elif i < self._length:
            current_index = self._length - 1
            curr = self._last

            while curr is not None:
                if current_index == i:
                    curr.item = item

                curr = curr.prev
                current_index -= 1
        else:
            raise IndexError

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of the given item in this list.
        """

        index_so_far = 0
        curr = self._first

        while curr is not None:
            if curr.item == item:
                return index_so_far
            index_so_far += 1
            curr = curr.next
        raise ValueError

    def __str__(self) -> str:
        """Return a string representation of this list.
        """
        return '[' + ' <--> '.join([str(element) for element in self]) + ']'

    def __repr__(self) -> str:
        return f'DoubleLinkedList({self.__str__()})'

    def count(self, item: Any) -> int:
        """Return the number of times the given item occurs in this list.
        """
        count = 0

        if len(self) == 0:
            return count

        curr_from_start = self._first
        curr_from_end = self._last

        starting_index = 0

        if len(self) % 2 == 0:
            starting_index = 1
            curr_from_start = curr_from_start.next

            if self._first.item == item:
                count += 1

        ending_index = len(self) - 1

        while starting_index != ending_index:
            if curr_from_start.item == item:
                count += 1
            elif curr_from_end.item == item:
                count += 1

            starting_index += 1
            ending_index -= 1

            curr_from_start = curr_from_start.next
            curr_from_end = curr_from_end.prev

        if curr_from_start.item == curr_from_end.item == item:
            count += 1

        return count

    def copy(self) -> DoublyLinkedList:
        return DoublyLinkedList(first=self._first, last=self._last)

    def __add__(self, other: DoublyLinkedList) -> DoublyLinkedList:
        copy = self.copy()

        curr = other._first

        while curr is not None:
            copy.append(curr.item)
            curr = curr.next

        return copy

    def sort(self, reverse: Optional[bool] = False):
        lst = self.to_list()
        lst.sort(reverse=reverse)
        copy = DoublyLinkedList(lst)
        self._first = copy._first
        self._last = copy._last

    def remove(self, item: Any) -> None:
        """Remove the first occurrence
        """
        curr = self._first

        if not curr:
            raise ValueError

        elif curr.item == item:
            self._first = self._first.next

            if self._first:
                self._first.prev = None

            self._length -= 1

        else:
            while curr is not None:
                if curr.next and curr.next.item == item:
                    if curr.next.next:
                        curr.next.next.prev = curr.next
                    curr.next = curr.next.next

                    self._length -= 1
                    return
                curr = curr.next
            raise ValueError

    def __eq__(self, other: DoublyLinkedList) -> bool:
        """Return whether this list and the other list are equal.
        """
        curr1 = self._first
        curr2 = other._first
        are_equal = True

        while are_equal and curr1 is not None and curr2 is not None:
            if curr1.item != curr2.item:
                are_equal = False
            curr1 = curr1.next
            curr2 = curr2.next

        return are_equal

    def invert(self) -> None:
        """Invert the linked list
        """

        curr = self._first
        previous = None

        while curr:
            curr_value = curr.next
            curr.next = curr.prev
            curr.prev = curr_value
            
            previous = curr
            curr = curr_value

        self._last = self._first
        self._first = previous

    def extend(self, other: DoublyLinkedList) -> None:
        """Extend self by other linked list"""
        copy = self.copy()

        curr = other._first

        while curr is not None:
            copy.append(curr.item)
            curr = curr.next

        self._first = copy._first
        self._last = copy._last
        self._length = copy._length

    def map(self, key=Callable) -> DoublyLinkedList:
        """Return a mapped list to key"""
        lst = DoublyLinkedList()

        curr = self._first

        while curr is not None:
            lst.append(key(curr.item))
            curr = curr.next

        return lst

    def __abs__(self) -> DoublyLinkedList:
        return self.map(lambda x: abs(x))

    def abs(self) -> DoublyLinkedList:
        return self.map(lambda x: abs(x))

    def __floor__(self) -> DoublyLinkedList:
        return self.map(lambda x: math.floor(x))

    def floor(self) -> DoublyLinkedList:
        return self.map(lambda x: math.floor(x))

    def __ceil__(self) -> DoublyLinkedList:
        return self.map(lambda x: math.ceil(x))

    def ceil(self) -> DoublyLinkedList:
        return self.map(lambda x: math.ceil(x))
