"""
This file contains tests for the Stack Class
"""

from Stack import Stack, EmptyStackError

# Add the root directory to PYTHONPATH
import sys

sys.path.append('.')


def test_append() -> None:
    """
    Tests the append function of the stack datastructure
    """
    stack = Stack()

    stack.push(2)
    stack.push("2")
    assert stack.items == [2, "2"]


def test_pop() -> None:
    """
    Tests the pop function of the stack datastructure
    """
    stack = Stack()

    stack.push(2)
    stack.push(3)

    popped_item = stack.pop()
    assert (popped_item == 3) and (stack.items == [2])


def test_pop_error() -> None:
    """
    Tests whether pop raises an error correctly
    """
    stack = Stack()

    with pytest.raises(EmptyStackError):
        stack.pop()


if __name__ == '__main__':
    import pytest

    pytest.main(['test_Stack.py'])
