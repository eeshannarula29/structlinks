"""
This file contains tests for the Stack Class
"""

from Stack import *

# Add the root directory to PYTHONPATH
import sys

sys.path.append('.')


class TestStack:

    def test_append(self) -> None:
        """Test the append function of the stack datastructures
        """
        stack = Stack()

        stack.push(2)
        stack.push("2")
        assert stack.to_list() == [2, "2"]

    def test_pop(self) -> None:
        """Test the pop function of the stack datastructures
        """
        stack = Stack()

        stack.push(2)
        stack.push(3)

        popped_item = stack.pop()
        assert (popped_item == 3) and (stack.to_list() == [2])

    def test_pop_error(self) -> None:
        """Test whether pop raises an error correctly
        """
        stack = Stack()

        try:
            stack.pop()
        except EmptyStackError:
            assert True
        except Exception as exp:
            if exp != EmptyStackError:
                assert False

    def test_multiple_push_empty_stack_empty_push(self) -> None:
        """Test push_multiple function for empty stack and empty push"""
        stack = Stack()
        stack.push_multiple([])

        assert stack.to_list() == []

    def test_multiple_push_empty_stack(self) -> None:
        """Test push_multiple function for empty stack"""
        stack = Stack()
        stack.push_multiple([1, 2, 3])

        assert stack.to_list() == [1, 2, 3]

    def test_multiple_push(self) -> None:
        """Test push_multiple function for empty stack"""
        stack = Stack([1, 2, 3, 4])
        stack.push_multiple([5, 6])

        assert stack.to_list() == [1, 2, 3, 4, 5, 6]

    def test_invert_empty(self) -> None:
        """Test invert function on empty stack"""
        stack = Stack()
        stack.invert()

        assert stack.to_list() == []

    def test_invert(self) -> None:
        """Test invert function"""
        stack = Stack([1, 2, 3, 4])
        stack.invert()

        assert stack.to_list() == [4, 3, 2, 1]

    def test_extend_both_empty(self) -> None:
        """Test extend function when both Stacks are empty"""
        s1 = Stack()
        s2 = Stack()

        s1.extend(s2)

        assert s1.to_list() == []

    def test_extend_mutating_empty(self) -> None:
        """Test extend function when the Stack being mutated is empty"""
        s1 = Stack()
        s2 = Stack([1, 2, 3, 4])

        s1.extend(s2)

        assert s1.to_list() == [1, 2, 3, 4]

    def test_extend_by_empty(self) -> None:
        """Test extend function when the Stack by which to extend is empty"""
        s1 = Stack([1, 2, 3, 4])
        s2 = Stack()

        s1.extend(s2)

        assert s1.to_list() == [1, 2, 3, 4]

    def test_extend(self) -> None:
        """Test extend function when both are non empty"""
        s1 = Stack([1, 2, 3, 4])
        s2 = Stack([5, 6, 7, 8])

        s1.extend(s2)

        assert s1.to_list() == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_add_both_empty(self) -> None:
        """Test __add__ function when both Stacks are empty"""
        s1 = Stack()
        s2 = Stack()

        s3 = s1 + s2

        assert s3.to_list() == []

    def test_add_by_empty(self) -> None:
        """Test __add__ function when one of the stack is empty"""
        s1 = Stack([1, 2, 3, 4])
        s2 = Stack()

        s3 = s1 + s2

        assert s3.to_list() == [1, 2, 3, 4]

    def test_add(self) -> None:
        """Test __add__ function when both are non empty"""
        s1 = Stack([1, 2, 3, 4])
        s2 = Stack([5, 6, 7, 8])

        s3 = s1 + s2

        assert s3.to_list() == [1, 2, 3, 4, 5, 6, 7, 8]
