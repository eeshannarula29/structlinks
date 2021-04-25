"""This file contains the Matrix object."""

from __future__ import annotations
from typing import Union, Callable
import copy


class Matrix:
    """A matrix

    Instance Attributes:
    - shape: shape of the matrix

    Private Instance Attributes:
    - _row_count: The number of rows
    - _col_count: The number of columns
    - _matrix: A 2-D list of integers or floats
    """
    _matrix: list[list[Union[int, float]]]
    _row_count: int
    _col_count: int

    def __init__(self, array: list[list[Union[int, float]]]) -> None:
        """Initialize a new matrix
        """
        self._row_count = len(array)
        self._col_count = len(array[0]) if self._row_count > 0 else 0

        self.shape = (self._row_count, self._col_count)

        self._matrix = array

    def __getitem__(self, index: int) -> list:
        """ Return the row at index <index>"""
        if self._row_count <= index:
            raise IndexError
        return self._matrix[index]

    def __str__(self) -> str:
        return '[' + '\n '.join([str(row) for row in self._matrix]) + ']'

    def __repr__(self) -> str:
        return 'Matrix([' + '\n        '.join([str(row) for row in self._matrix]) + '])'

    def copy(self) -> Matrix:
        return Matrix(copy.deepcopy(self._matrix))

    def to_list(self) -> list[list[Union[int, float]]]:
        return copy.deepcopy(self._matrix)

    @property
    def is_square(self) -> bool:
        """Return whether the current matrix is square"""
        return self._row_count == self._col_count

    @property
    def is_invertible(self) -> bool:
        """Return whether the current matrix is invertible"""
        if self.is_square:
            return self.determinant() != 0
        return False

    @property
    def is_vector(self) -> bool:
        """Return whether self is a vector"""
        return self._row_count == 1 or self._col_count == 1

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        """Return a zero matrix of shape <shape>"""
        return Matrix([[0] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        """Return a matrix with all elements one of shape <shape>"""
        return Matrix([[1] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def identity(order: int) -> Matrix:
        """Return a identity matrix of shape order X order"""
        return Matrix([[1 if i == j else 0 for j in range(order) for i in range(order)]])

    def map(self, func: Callable) -> Matrix:
        """Return a new matrix mapped to function <func>"""
        copy_mat = self.copy()

        for i in range(self._row_count):
            for j in range(self._col_count):
                copy_mat[i][j] = func(copy_mat[i][j])

        return copy_mat

    def add_scalar(self, k: Union[int, float]) -> Matrix:
        """Add the current matrix by the scalar k
        to produce a new matrix. This operation does not mutate
        the original matrix
        """
        return self.map(lambda x: x + k)

    def multiply_scalar(self, k: Union[int, float]) -> Matrix:
        """Multiply the current matrix by the scalar k
        to produce a new matrix. This operation does not mutate
        the original matrix
        """
        return self.map(lambda x: x * k)
    
    def add_matrix(self, other: Matrix) -> Matrix:
        """Add the current matrix and matrix b to produce a
        new matrix. This operation does not mutate either matrix

        Preconditions:
            - self.row_count == b.row_count
            - self.col_count == b.col_count
        """
        if self.shape != other.shape:
            raise ShapeError

        sum_matrix = Matrix.zeros((self._row_count, self._col_count))
        for i in range(self._row_count):
            for j in range(self._col_count):
                # Add the corresponding entries for both matrices
                sum_matrix[i][j] = self[i][j] + other[i][j]
        return sum_matrix

    def multiply_matrix(self, other: Matrix) -> Matrix:
        """Matrix multiply self with other.
        This operation does not mutate the original matrix"""
        # check if self and other can be multiplied
        if self.shape[1] != other.shape[0]:
            raise TypeError(f'Can not multiply matrices of {self.shape} and {other.shape}')
        
        result = Matrix.zeros((self.shape[0], other.shape[1]))
        # iterate through rows of self
        for i in range(self._row_count):
            # iterate through columns of other
            for j in range(other.shape[1]):
                # iterate through rows of outer
                for k in range(other.shape[0]):
                    result[i][j] += self[i][k] * other[k][j]

        return result

    def transpose(self) -> Matrix:
        """Return transposed matrix of self"""
        new_matrix = Matrix.zeros((self.shape[1], self.shape[0]))

        for i in range(self._row_count):
            for j in range(self._col_count):
                new_matrix[j][i] = copy.deepcopy(self[i][j])

        return new_matrix

    def dot_multiply(self, other: Matrix) -> Matrix:
        """Return the dot product of two matrices

        Precondition:
        - self.shape == other.shape
        """
        if self.shape != other.shape:
            raise ShapeError

        return self.multiply_matrix(other.transpose())

    def minor(self, row: int, col: int) -> Matrix:
        """Return the minor of the matrix with the given row and
        col removed. This operation does not mutate the original matrix

        Preconditions:
            - 0 <= row < self.row_count
            - 0 <= col < self.col_count 
        """
        if not(0 <= row < self._row_count and 0 <= col < self._col_count):
            raise RowColOutOfBound

        # create a new array
        copy_mat = self.to_list()
        # remove the row
        copy_mat.pop(row)
        # remove the col from all the other rows
        for row in copy_mat:
            row.pop(col)
        # return the new matrix
        return Matrix(copy_mat)

    def determinant(self) -> Union[float, int]:
        """Return the determinant of the current matrix
        
        Preconditions:
            - self.row_count == self.col_count
        """
        if not self.is_square:
            raise NotSquareMatrix

        if self._row_count == 0 and self._col_count == 0:
            return 1
        elif self._row_count == 1 and self._col_count == 1:
            return self[0][0]
        else:
            determinant = 0
            for j in range(self._col_count):
                determinant += self[0][j] * ((-1) ** j) * self.minor(0, j).determinant()
            return determinant

    def cofactor(self) -> Matrix:
        """Return the cofactor matrix of self"""
        if not self.is_square:
            raise NotSquareMatrix

        new_matrix = Matrix.zeros(self.shape)

        for i in range(self._row_count):
            for j in range(self._col_count):
                new_matrix[i][j] = ((-1) ** (i + j)) * self.minor(i, j).determinant()

        return new_matrix

    def adjacent(self) -> Matrix:
        """Return the adj matrix of self"""
        if not self.is_square:
            raise NotSquareMatrix

        return self.cofactor().transpose()

    def inverse(self) -> Matrix:
        """Return inverse of self"""
        if not self.is_invertible:
            raise InverseDoesNotExists

        return self.adjacent().multiply_scalar(1 / self.determinant())


class NotSquareMatrix(Exception):
    """Error for when a non square matrix is passed"""
    def __str__(self) -> str:
        return "The matrix needs to be a square matrix"


class RowColOutOfBound(Exception):
    """Error for when the row or col index is out of bound"""
    def __str__(self) -> str:
        return "Either or Both the Row or Col index are out of bound"


class ShapeError(Exception):
    """Error for when the shape of the two matrices is different"""
    def __str__(self) -> str:
        return "The shape of the two matrices needs to be the same"


class InverseDoesNotExists(Exception):
    """Error for when inverse does not exists"""
    def __str__(self) -> str:
        return "The matrix is not invertible"
