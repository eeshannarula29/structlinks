"""This file contains the Matrix object."""

from __future__ import annotations
from typing import Union
import pprint
import copy


class Matrix:
    """A matrix

    Instance Attributes:
        - row_count: The number of rows
        - col_count: The number of columns 
    """
    # Private Instance Attributes:
    #       - _matrix: A 2-D list of integers or floats
    _matrix: list[list[Union[int, float]]]
    row_count: int
    col_count: int

    def __init__(self, m: int, n: int) -> None:
        """Initialize a new m x n matrix with all ones, where m is the number of rows
        and n is the number of columns

        Preconditions:
            - m >= 0 and n >= 0
        """
        if m == 0 or n == 0:
            self._matrix = []
            self.row_count = 0
            self.col_count = 0
        else:
            self._matrix = []
            for _ in range(m):
                self._matrix.append([1 for _ in range(n)])
            
            self.row_count = m
            self.col_count = n

    def multiply_scalar(self, k: Union[int, float]) -> Matrix:
        """Multiply the current matrix by the scalar k
        to produce a new matrix. This operation does not mutate
        the original matrix
        """
        new_matrix = Matrix(self.row_count, self.col_count)
        for i in range(self.row_count):
            for j in range(self.col_count):
                new_matrix._matrix[i][j] *= k
        return new_matrix
    
    def add_matrix(self, b: Matrix) -> Matrix:
        """Add the current matrix and matrix b to produce a
        new matrix. This operation does not mutate either matrix

        Preconditions:
            - self.row_count == b.row_count
            - self.col_count == b.col_count
        """
        sum_matrix = Matrix(self.row_count, self.col_count)
        for i in range(self.row_count):
            for j in range(self.col_count):
                # Add the corresponding entries for both matrices
                sum_matrix._matrix[i][j] = self._matrix[i][j] + b._matrix[i][j]
        return sum_matrix
    
    def is_square(self) -> bool:
        """Return whether the current matrix is square"""
        return self.row_count == self.col_count
    
    def print_matrix(self) -> None:
        """Print the current matrix to the console"""
        pprint.pprint(self._matrix)
    
    def minor(self, row: int, col: int) -> Matrix:
        """Return the minor of the matrix with the given row and
        col removed. This operation does not mutate the original matrix

        Preconditions:
            - 0 <= row < self.row_count
            - 0 <= col < self.col_count 
        """
        new_matrix = Matrix(self.row_count - 1, self.col_count - 1)
        for i in range(self.row_count):
            for j in range(self.col_count):
                if i < row and j < col:
                    new_matrix._matrix[i][j] = self._matrix[i][j]
                elif i < row and j > col:
                    new_matrix._matrix[i][j - 1] = self._matrix[i][j]
                elif i > row and j < col:
                    new_matrix._matrix[i - 1][j] = self._matrix[i][j]
                elif i > row and j > col:
                    new_matrix._matrix[i - 1][j - 1] = self._matrix[i][j]
        return new_matrix

    def determinant(self) -> Union[float, int]:
        """Return the determinant of the current matrix
        
        Preconditions:
            - self.row_count == self.col_count
        """
        if self.row_count == 0 and self.col_count == 0:
            return 1
        elif self.row_count == 1 and self.col_count == 1:
            return self._matrix[0][0]
        else:
            determinant = 0
            for j in range(self.col_count):
                determinant += self._matrix[0][j] * ((-1) ** j) * self.minor(0, j).determinant()
            return determinant
    
    def is_invertible(self) -> bool:
        """Return whether the current matrix is invertible"""
        return self.determinant() != 0
    
    def get_matrix(self) -> list[list[Union[int, float]]]:
        """Return a copy of the list of lists representing the matrix"""
        return copy.deepcopy(self._matrix)
    
    def set_matrix(self, input: list[list[Union[int, float]]]) -> None:
        """Set the current matrix to a copy of the given input
        
        Preconditions:
            - all(len(list_1) == len(list_2) for list_1 in input for list_2 in input)
        """
        self._matrix = copy.deepcopy(input)
        self.row_count = len(input)
        if len(input) == 0:
            self.col_count = 0
        else:
            self.col_count = len(input[0])
    
    def __getitem__(self, pos: tuple[int, int]) -> Union[int, float]:
        """Return the entry at the i-th row and j-th column"""
        i, j = pos
        # Subtract 1 since indexing starts at 0
        return self._matrix[i - 1][j - 1]

