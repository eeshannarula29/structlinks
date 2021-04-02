"""
This is an implementation of the stack data structure, with code pulled from the CSC110
course notes.
"""
from __future__ import annotations
from typing import Any


class Stack:
    """
    This class represents a stack data structure
    """

    def __init__(self) -> None:
        """
        Initialize a stack, empty at first
        """
        self.items = []

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

    def pop(self) -> Any:
        """
        Removes the element at the top of the stack and
        returns it. Raises IndexError if list is empty
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self.items.pop()


class EmptyStackError(Exception):
    def __str__(self) -> str:
        """String representation of the error"""
        return "Popping from an empty stack is not allowed"
