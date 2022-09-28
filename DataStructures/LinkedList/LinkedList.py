from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Sequence, Union, Callable
import math


@dataclass
class _Node:
    """
    A node in a linked list.
    The class it take from University of Toronto CSC111 course
    """
    item: Any
    next: Optional[_Node] = None


class LinkedList:
    """
    The class represents a Linked lists
    Many of the methods in the class are taken from University of Toronto CSC111 course
    """
    def __init__(self,
                 items: Optional[Sequence] = None,
                 first: Optional[_Node] = None,
                 tail: Optional[_Node] = None) -> None:
        """
        Initialize a linked list.
        """

        self._first = first
        self._tail = tail
        self._length = 0

        if items:
            for item in items:
                self.append(item)

    def add_first(self, item: Any):
        new_node = _Node(item)
        new_node.next = self._first
        self._first = new_node

        if self._tail is None:
            self._tail = self._first
        self._length += 1

    def append(self, item: Any) -> None:
        """
        Append item to the end of this list.
        """
        if isinstance(item, list):
            self._append_list(item)
            return

        if self._tail is None:
            self.add_first(item)
            return

        new_node = _Node(item)
        self._tail.next = new_node
        self._tail = new_node
        self._length += 1

    def _append_list(self, item):
        for e in item:
            self.append(e)

    def insert(self, i: int, item: Any) -> None:
        if i < 0:
            i = self._length + i

        if i == self._length:
            self.append(item)
            return

        if i == 0:
            self.add_first(item)
        else:
            curr = self._first
            curr_index = 0

            while curr is not None and curr_index != i - 1:
                curr_index += 1
                curr = curr.next

            if curr is None:
                raise IndexError
            else:
                new_node = _Node(item, curr.next)
                curr.next = new_node
                self._length += 1

    def pop(self, i: int) -> Any:
        if i < 0:
            i = self._length + i

        if i == 0:
            if self._first:
                item = self._first.item
                self._first = self._first.next
                self._length -= 1
                return item
            else:
                raise IndexError
        else:

            if i > self._length:
                raise IndexError('Index out of bound')

            curr = self._first
            curr_index = 0

            while curr is not None and curr_index != i - 1:
                curr = curr.next
                curr_index += 1

            if curr.next is None:
                raise IndexError

            else:
                item = curr.next.item
                curr.next = curr.next.next
                self._length -= 1
                return item

    def remove(self, item: Any) -> None:

        curr = self._first

        if not curr:
            raise ValueError

        elif curr.item == item:
            self._first = self._first.next
            self._length -= 1

        else:
            while curr is not None:
                if curr.next and curr.next.item == item:
                    curr.next = curr.next.next
                    self._length -= 1
                    return
                curr = curr.next
            raise ValueError

    def count(self, item: Any) -> int:

        curr = self._first
        count = 0

        while curr is not None:
            if curr.item == item:
                count += 1
            curr = curr.next

        return count

    def index(self, item: Any) -> int:

        index_so_far = 0
        curr = self._first

        while curr is not None and index_so_far < self._length:
            if curr.item == item:
                return index_so_far
            index_so_far += 1
            curr = curr.next
        raise ValueError(f'{item} not in the Linked List')

    def __setitem__(self, i: int, item: Any) -> None:

        if i < 0:
            i = self._length + i

        curr = self._first
        index_so_far = 0

        while curr is not None:
            if index_so_far == i:
                curr.item = item
                break
            index_so_far += 1
            curr = curr.next
        if curr is None:
            raise IndexError

    def invert(self) -> None:

        curr = self._first
        previous = None

        while curr:
            curr_value = curr.next
            curr.next = previous

            previous = curr
            curr = curr_value

        self._first = previous

    def to_list(self) -> list:

        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def copy(self) -> LinkedList:
        copy = LinkedList()
        curr = self._first

        while curr is not None:
            copy.append(curr.item)
            curr = curr.next

        return copy

    def extend(self, other: LinkedList) -> None:
        curr = other._first

        while curr is not None:
            self.append(curr.item)
            curr = curr.next

    def __add__(self, other: LinkedList) -> LinkedList:
        copy = self.copy()
        curr = other._first

        while curr is not None:
            copy.append(curr.item)
            curr = curr.next

        return copy

    def sort(self, reverse: Optional[bool] = False):
        lst = self.to_list()
        lst.sort(reverse=reverse)
        copy = LinkedList(lst)
        self._first = copy._first

    def map(self, key=Callable) -> LinkedList:
        lst = LinkedList()

        curr = self._first

        while curr is not None:
            lst.append(key(curr.item))
            curr = curr.next

        return lst

    def __contains__(self, item: Any) -> bool:
        """
        Return whether item is in this linked list.
        """
        curr = self._first

        while curr is not None:
            if curr.item == item:
                return True

            curr = curr.next

        return False

    def __getitem__(self, i: Union[int, slice]) -> Union[Any, LinkedList]:
        if isinstance(i, int):

            if i < 0:
                i = self._length + i

            curr = self._first
            curr_index = 0

            while curr is not None and curr_index != i:
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                return curr.item
        else:
            start = i.start
            stop = i.stop

            if start is None:
                start = 0
            if stop is None:
                stop = self._length

            if not (0 <= start <= stop <= len(self)):
                raise IndexError
            else:
                new_linked_list = LinkedList([])
                index = 0

                for item in self:
                    if start <= index < stop:
                        new_linked_list.append(item)
                    elif index > stop:
                        break
                    index += 1

                return new_linked_list

    def __eq__(self, other: LinkedList) -> bool:

        curr1 = self._first
        curr2 = other._first
        are_equal = True

        while are_equal and curr1 is not None and curr2 is not None:
            if curr1.item != curr2.item:
                are_equal = False
            curr1 = curr1.next
            curr2 = curr2.next

        return are_equal

    def __str__(self) -> str:
        return '[' + ' -> '.join([str(element) for element in self]) + ']'

    def __repr__(self) -> str:
        return f'LinkedList({self.__str__()})'

    def __abs__(self) -> LinkedList:
        return self.map(lambda x: abs(x))

    def __floor__(self) -> LinkedList:
        return self.map(lambda x: math.floor(x))

    def __ceil__(self) -> LinkedList:
        return self.map(lambda x: math.ceil(x))

    def __len__(self) -> int:
        return self._length