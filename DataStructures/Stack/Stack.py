"""
This is an implementation of the stack data structure, with code pulled from the
University of Toronto's CSC110 course notes.
"""
from __future__ import annotations
from typing import Any, Optional, Callable, Sequence


class Stack:
    """
    This class represents a stack data structure
    """

    def __init__(self, items: Optional[list] = None) -> None:
        """
        Initialize a stack, empty at first
        """
        self.items = []

        if items:
            self.items = items

    def is_empty(self) -> bool:
        """
        Returns whether the stack is empty
        """
        return self.items == []

    def push(self, item: Any) -> None:
        """
        Adds a new element to the top of the stack
        """
        self.items.append(item)

    def push_multiple(self, items: Sequence) -> None:
        """Push multiple items in the stack"""
        for item in items:
            self.push(item)

    def pop(self) -> Any:
        """
        Removes the element at the top of the stack and
        returns it. Raises IndexError if list is empty
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self.items.pop()

    def __len__(self) -> int:
        """Return the length of the stack"""
        return len(self.items)

    def to_list(self) -> list:
        """Return list of the stack"""
        return self.items

    def __copy__(self) -> Stack:
        """Return a copy of the stack"""
        return Stack(items=self.items)

    def copy(self) -> Stack:
        """Return a copy of the stack"""
        return Stack(items=self.items)

    def map(self, key: Callable) -> Stack:
        """Map a function to the stack"""
        return Stack(items=[key(item) for item in self.items])

    def invert(self) -> None:
        """Invert the stack"""
        self.items.reverse()

    def extend(self, other: Stack):
        """extend the stack by putting other stack on top of self"""
        self.push_multiple(other.items)

    def __add__(self, other) -> Stack:
        """Return a stack with other stack on top of self"""
        return Stack(items=self.items + other.items)

    def __str__(self) -> str:
        """Return string representation of the stack"""
        string_so_far = ''

        gap = 10

        for index in range(len(self) - 1, -1, -1):
            item = self.items[index]

            string_rep = str(item)

            gap_left = gap - len(string_rep)

            string_so_far += '|' + ' ' * gap + string_rep + ' ' * gap_left + '| \n'

        string_so_far += '|' + '_' * (2 * gap) + '|'

        return string_so_far

    def __repr__(self) -> str:
        return f'Stack({self.items})'


class EmptyStackError(Exception):
    def __str__(self) -> str:
        """String representation of the error"""
        return "Popping from an empty stack is not allowed"
