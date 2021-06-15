"""This file contains the Binary search tree class. SOme of the methods of the class are
taken from University of Toronto's CSC111 course

The printing of the branched binary search tree is taken from StackOverflow, the link
is the the readme.md file.
"""

from __future__ import annotations
from typing import Optional, Any, Callable
import math
import copy as cpy


class BinarySearchTree:
    """The class represents a Binary search tree

    Some of the methods are taken from the University of Toronto's CSC111 course
    """
    def __init__(self, root: Optional[Any]) -> None:

        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def set_left_to(self, tree: BinarySearchTree) -> None:
        if isinstance(tree, BinarySearchTree):
            self._left = tree
        else:
            raise TypeError

    def set_right_to(self, tree: BinarySearchTree) -> None:
        if isinstance(tree, BinarySearchTree):
            self._right = tree
        else:
            raise TypeError

    @property
    def root(self) -> Any:
        """Root of the BST"""
        return cpy.copy(self._root)

    @property
    def left(self) -> Any:
        """Return copy of left child of the BST"""
        return self._left.copy()

    @property
    def right(self) -> Any:
        """Return copy of right child of the BST"""
        return self._right.copy()

    @property
    def is_balanced(self) -> bool:

        if self.is_empty():
            return True

        if abs(self._left.height - self._right.height) <= 1 and \
                self._left.is_balanced and self._right.is_balanced:
            return True

        return False

    @property
    def height(self) -> int:
        """Return the height of the tree"""
        if self.is_empty():
            return 0
        else:
            return 1 + max(self._left.height, self._right.height)

    def is_empty(self) -> bool:
        """Return whether this BST is empty.
        """
        return self._root is None

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return self._left.__contains__(item)
        else:
            return self._right.__contains__(item)

    def __copy__(self) -> BinarySearchTree:
        """Return a copy of the BST"""
        tree = BinarySearchTree(self._root)
        tree.set_right_to(self._right)
        tree.set_left_to(self._left)
        return tree

    def copy(self) -> BinarySearchTree:
        """Return a copy of the BST"""
        if self.is_empty():
            return BinarySearchTree(self.root)
        else:
            tree = BinarySearchTree(self.root)
            tree.set_right_to(self._right.copy())
            tree.set_left_to(self._left.copy())
            return tree

    def __abs__(self) -> BinarySearchTree:
        """Return BST similar to self, but with abs values"""
        return self.map(lambda x: abs(x))

    def abs(self) -> BinarySearchTree:
        """Return BST similar to self, but with abs values"""
        return self.map(lambda x: abs(x))

    def __eq__(self, other: BinarySearchTree) -> bool:
        """Check weather two BST's ate same or not"""
        return self.to_list() == other.to_list()

    def floor(self) -> BinarySearchTree:
        """Return BST similar to self, but with floor values"""
        return self.map(lambda x: math.floor(x))

    def ceil(self) -> BinarySearchTree:
        """Return BST similar to self, but with ceil values"""
        return self.map(lambda x: math.ceil(x))

    def __floor__(self) -> BinarySearchTree:
        """Return BST similar to self, but with floor values"""
        return self.map(lambda x: math.floor(x))

    def __ceil__(self) -> BinarySearchTree:
        """Return BST similar to self, but with ceil values"""
        return self.map(lambda x: math.ceil(x))

    def map(self, key=Callable) -> BinarySearchTree:
        """Map the BST to key and return mapped BST"""
        copy = self.copy()

        if not copy.is_empty():
            copy._root = key(self._root)
            copy.set_left_to(copy._left.map(key))
            copy.set_right_to(self._right.map(key))

        return copy

    def apply(self, key=Callable) -> None:
        """Map the BST to key"""

        if not self.is_empty():
            self._root = key(self._root)
            self._left.apply(key)
            self._right.apply(key)

    def __str__(self) -> str:
        """Return a string representation of this BST.
        """
        return self.display_branched()

    def __repr__(self) -> str:
        return 'BinarySearchTree( \n' + self.display_branched() + ')'

    def display(self, indented: Optional[bool] = False):
        """Print a string representation of this BST"""
        if indented:
            print(self.display_indented())
        else:
            print(self.display_branched())

    def display_indented(self) -> str:
        """Return indented string representation of BST"""
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.
        """
        if self.is_empty():
            return ''
        else:
            return (
                    depth * '  ' + '|->' + f'{self._root}\n'
                    + self._left._str_indented(depth + 1)
                    + self._right._str_indented(depth + 1)
            )

    def display_branched(self) -> str:
        string_so_far = ''
        lines, *_ = self._display_aux()
        for line in lines:
            string_so_far += line + '\n'

        return string_so_far

    def _display_aux(self) -> Any:

        if self._right.is_empty() and self._left.is_empty():
            line = '%s' % self._root
            width = len(line)
            height = 1
            middle = width // 2

            return [line], width, height, middle

        if self._right.is_empty():
            lines, n, p, x = self._left._display_aux()

            s = '%s' % self._root
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self._left.is_empty():
            lines, n, p, x = self._right._display_aux()

            s = '%s' % self._root
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._left._display_aux()
        right, m, q, y = self._right._display_aux()

        s = '%s' % self._root
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]

        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def maximum(self) -> Optional[int]:
        """Return the maximum number in this BST, or None if this BST is empty.
        """
        if self.is_empty():
            return None
        else:
            curr_max = self._root

            if self._right._root and curr_max < self._right._root:
                curr_max = self._right.maximum()

            return curr_max

    def minimum(self) -> Optional[Any]:
        """Return the minimum number in this BST, or None if this BST is empty.
        """
        if self.is_empty():
            return None
        else:
            curr_min = self._root

            if self._right._root and curr_min > self._left._root:
                curr_min = self._left.maximum()

            return curr_min

    def items(self) -> list:
        """Return all of the items in the BST in sorted order.
        """
        if self.is_empty():
            return []
        else:
            return self._left.items() + [self._root] + self._right.items()

    def insert(self, item: Any) -> None:
        """Insert item into the list
        """
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        elif item > self._root:
            self._right.insert(item)
        elif item < self._root:
            self._left.insert(item)
        else:
            return

    def remove(self, item) -> bool:
        """Remove the item from the tree
        """
        if self.is_empty():
            return False
        elif self._root == item:
            self._delete_root()
        else:
            if item > self._root:
                return self._right.remove(item)
            else:
                return self._left.remove(item)

    def _delete_root(self) -> None:

        if self._left.is_empty() and self._right.is_empty():

            self._root = None
            self._right._root = None
            self._left._root = None

        elif self._left.is_empty():

            self._root, self._left, self._right = self._right._root, \
                                                  self._right._left, \
                                                  self._right._right

        elif self._right.is_empty():

            self._root, self._left, self._right = self._left._root, \
                                                  self._left._left, \
                                                  self._left._right
        else:
            self._root = self._extract_max()

    def _extract_max(self) -> Any:

        if self._right._root is None:  # if this is the case then _root is the largest number
            max_item = self._root
            self._root, self._right._root, self._left._root = None, None, None
            return max_item
        else:
            return self._right._extract_max()

    def invert(self) -> None:
        """Invert the BST"""
        if not self.is_empty():

            if not self._left.is_empty():
                self._left.invert()
            if not self._right.is_empty():
                self._right.invert()

            temp = self._left
            self._left = self._right
            self._right = temp

    @staticmethod
    def create_tree(lst: list) -> BinarySearchTree:
        """Return a balanced binary search tree"""
        lst = list(set(lst))

        if len(lst) == 1:
            return BinarySearchTree(lst[0])

        elif len(lst) > 1:

            lst = sorted(lst)

            middle = len(lst) // 2

            left = BinarySearchTree.create_tree(lst[:middle])

            right = None

            if middle + 1 < len(lst):
                right = BinarySearchTree.create_tree(lst[(middle + 1):])

            tree = BinarySearchTree(lst[middle])

            tree._left = left

            if right:
                tree._right = right

            return tree

    def to_list(self) -> list:
        """Return all of the items in the BST in sorted order.
        """
        if self.is_empty():
            return []
        else:
            return self._left.to_list() + [self._root] + self._right.to_list()

    def balance(self) -> None:
        """Convert the BST to a balanced BST"""
        tree = BinarySearchTree.create_tree(self.to_list())

        self._root = tree._root
        self._left = tree._left
        self._right = tree._right
