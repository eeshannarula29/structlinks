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

    def _get_indices(self, s: slice, stop_num: int) -> list:
        start = s.start if s.start else 0
        end = s.stop if s.stop else stop_num
        return list(range(start, end))
    
    def __getitem__(self, index) -> list:
        """ Return the row at index <index>"""
        if isinstance(index, int):
            raise ValueError("Please provide both Row and Col in the format [row (int/slice), col (int/slice)]")
        
        elif isinstance(index[0], int) and isinstance(index[1], int):
            if index[0] >= self._row_count or index[1]>= self._col_count:
                raise IndexError("either row or column is out of bound")
            return self._matrix[index[0]][index[1]]
        
        else:
            new_matrix = []
            rows = [index[0]] if isinstance(index[0], int) else self._get_indices(index[0], self._row_count)
            cols = [index[1]] if isinstance(index[1], int) else self._get_indices(index[1], self._col_count)
            
            if any(element < 0 or element >=self._row_count for element in rows):
                if any(element < 0 or element >=self._col_count for element in self._col_count):
                    raise IndexError("either row or column is out of bound")
                
            for row in rows:
                temp = []
                for col in cols:
                    temp.append(self._matrix[row][col])
                new_matrix.append(temp)

            return Matrix(new_matrix)

    def __setitem__(self, index, value) -> None:
        """Set the value <value> of item at index <index> in self"""
        if isinstance(index, int):
            raise ValueError("Please provide both Row and Col in the format [row (int/slice), col (int/slice)]")
        
        elif isinstance(index[0], int) and isinstance(index[1], int):
            if index[0] >= self._row_count or index[1]>= self._col_count:
                raise IndexError("either row or column is out of bound")
            self._matrix[index[0]][index[1]] = value
        
        elif isinstance(index[0], slice) or isinstance(index[1], slice):
            rows = [index[0]] if isinstance(index[0], int) else self._get_indices(index[0], self._row_count)
            cols = [index[1]] if isinstance(index[1], int) else self._get_indices(index[1], self._col_count)
            
            if any(element < 0 or element >=self._row_count for element in rows):
                if any(element < 0 or element >=self._col_count for element in self._col_count):
                    raise IndexError("either row or column is out of bound")
                
            for row_index, row in enumerate(rows):
                for col_index, col in enumerate(cols):
                    self._matrix[row][col] = value[row_index, col_index]
        else:
            raise ValueError("The row and the column should be of int or slice data type")    
        
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
            return self.determinant != 0
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
                copy_mat[i, j] = func(copy_mat[i, j])

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
                sum_matrix[i, j] = self[i, j] + other[i, j]
        return sum_matrix

    def multiply_matrix(self, other: Matrix) -> Matrix:
        """Matrix multiply self with other.
        This operation does not mutate the original matrix"""
        # check if self and other can be multiplied
        if self.shape[1] != other.shape[0]:
            raise TypeError(f'Can not multiply matrices of shape {self.shape} and {other.shape}')
        
        result = Matrix.zeros((self.shape[0], other.shape[1]))
        # iterate through rows of self
        for i in range(self._row_count):
            # iterate through columns of other
            for j in range(other.shape[1]):
                # iterate through rows of outer
                for k in range(other.shape[0]):
                    result[i, j] += self[i, k] * other[k, j]

        return result
    
    @property
    def transpose(self) -> Matrix:
        """Return transposed matrix of self"""
        new_matrix = Matrix.zeros((self.shape[1], self.shape[0]))

        for i in range(self._row_count):
            for j in range(self._col_count):
                new_matrix[j, i] = copy.deepcopy(self[i, j])

        return new_matrix

    def dot_multiply(self, other: Matrix) -> Matrix:
        """Return the dot product of two matrices

        Precondition:
        - self.shape == other.shape
        """
        if self.shape != other.shape:
            raise ShapeError

        return self.multiply_matrix(other.transpose)

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

    @property
    def determinant(self) -> Union[float, int]:
        """Return the determinant of the current matrix
        
        Preconditions:
            - self.row_count == self.col_count
        """
        if not self.is_square:
            return None

        if self._row_count == 0 and self._col_count == 0:
            return 1
        elif self._row_count == 1 and self._col_count == 1:
            return self[0, 0]
        else:
            determinant = 0
            for j in range(self._col_count):
                determinant += self[0, j] * ((-1) ** j) * self.minor(0, j).determinant
            return determinant

    @property
    def cofactor(self) -> Matrix:
        """Return the cofactor matrix of self"""
        if not self.is_square:
            return None

        new_matrix = Matrix.zeros(self.shape)

        for i in range(self._row_count):
            for j in range(self._col_count):
                new_matrix[i, j] = ((-1) ** (i + j)) * self.minor(i, j).determinant

        return new_matrix

    @property
    def adjacent(self) -> Matrix:
        """Return the adj matrix of self"""
        if not self.is_square:
            return None

        return self.cofactor.transpose

    @property
    def inverse(self) -> Matrix:
        """Return inverse of self"""
        if not self.is_invertible:
            return None

        return self.adjacent.multiply_scalar(1 / self.determinant)

    @staticmethod
    def vstack(matrices: list[Matrix]) -> Matrix:
        new_matrix = []
        def_shape = None
        
        if len(matrices) == 0:
            raise ValueError("the list of matrices can not be empty")
        
        for matrix in matrices:
            
            if not def_shape:
                def_shape = matrix.shape
                
            if not def_shape[1] == matrix.shape[1]:
                raise ColumnError
            
            for row in matrix.to_list():
                new_matrix.append(row)
                
        return Matrix(new_matrix)
    
    @staticmethod
    def hstack(matrices: list[Matrix]) -> Matrix:
        new_matrix = []
        def_shape = None
        
        if len(matrices) == 0:
            raise ValueError("the list of matrices can not be empty")
        
        for matrix in matrices:
            
            if not def_shape:
                def_shape = matrix.shape
                new_matrix = matrix.to_list()
            
            elif not def_shape[0] == matrix.shape[0]:
                raise RowError
            
            else:
                for row_index in range(def_shape[0]):
                    mat_row = matrix._matrix[row_index]
                    new_matrix[row_index].extend(mat_row) 
                                
        return Matrix(new_matrix)
    
    @staticmethod
    def _ToReducedRowEchelonForm( M):
        if not M: return
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        for r in range(rowCount):
            if lead >= columnCount:
                return
            i = r
            while M[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return
            M[i],M[r] = M[r],M[i]
            lv = M[r][lead]
            M[r] = [ mrx / float(lv) for mrx in M[r]]
            for i in range(rowCount):
                if i != r:
                    lv = M[i][lead]
                    M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
            lead += 1 
               
    @property
    def rref(self) -> Matrix:
        """Return the rref form of self
        
        source: https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
        """
        M = self.to_list()
        Matrix._ToReducedRowEchelonForm(M)
        return Matrix(M)
        
    @property
    def rank(self) -> int:
        rank = 0
        
        for row in self.rref._matrix:
            if any(element != 0 for element in row):
                rank += 1
        
        return rank   
    
    @property
    def nullity(self) -> int:
        return self._col_count - self.rank
    
    @property
    def lineary_independent(self) -> bool:
         return self.nullity == 0    
    
    @property
    def lineary_dependent(self) -> bool:
         return self.nullity != 0
    
    def get_indipendent_vectors(self) -> list[Matrix]:
            vectors = []
            
            for index, row in enumerate(self.rref._matrix):
                if any(element != 0 for element in row):
                    vectors.append(self[index, :])
            
            return vectors        
    
    def get_dependent_vectors(self) -> list[Matrix]:
            vectors = []
            
            for index, row in enumerate(self.rref._matrix):
                if all(element == 0 for element in row):
                    vectors.append(self[index, :])
            
            return vectors  
        
        
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
        return "The shape of the matrices needs to be the same"


class InverseDoesNotExists(Exception):
    """Error for when inverse does not exists"""
    def __str__(self) -> str:
        return "The matrix is not invertible"

class RowError(Exception):
    """Error for when the number of rows are not the same"""
    def __str__(self) -> str:
        return "The number of rows of the matrices need to be the same"

class ColumnError(Exception):
    """Error for when the number of columns are not the same"""
    def __str__(self) -> str:
        return "The number of columns of the matrices need to be the same"    
     