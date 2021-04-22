"""This file contains tests for the Matrix library"""

from structlinks.Matrix import Matrix


class TestMatrix:

    def test_multiply_scalar(self) -> None:
        """Test Matrix.multiply_scalar"""
        matrix = Matrix(3, 3)
        new_matrix = matrix.multiply_scalar(3)

        assert all(new_matrix[i, j] == 3 for i in range(1, new_matrix.row_count + 1)
                    for j in range(1, new_matrix.col_count + 1))
    
    def test_add_matrix(self) -> None:
        """Test Matrix.add_matrix"""
        matrix_a = Matrix(3, 3)
        matrix_b = Matrix(3, 3)

        sum_matrix = matrix_a.add_matrix(matrix_b)

        assert all(sum_matrix[i, j] == 2 for i in range(1, sum_matrix.row_count + 1)
                    for j in range(1, sum_matrix.col_count + 1))
    
    def test_is_square(self) -> None:
        """Test Matrix.is_square"""
        matrix_a = Matrix(4, 4)
        matrix_b = Matrix(1, 3)

        assert matrix_a.is_square() and not matrix_b.is_square()
    
    def test_minor(self) -> None:
        """Test Matrix.minor"""
        matrix_a = Matrix(1, 2)
        minor_matrix_a = matrix_a.minor(0, 1)

        matrix_b = Matrix(3, 3)
        matrix_b.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        minor_matrix_b = matrix_b.minor(0, 0)
        minor_matrix_b2 = matrix_b.minor(1, 1)
        minor_matrix_b3 = matrix_b.minor(2, 2)
        minor_matrix_b4 = matrix_b.minor(2, 0)

        assert minor_matrix_a.get_matrix() == []
        assert minor_matrix_b.get_matrix() == [[2, 3], [5, 6], [8, 9]]
        assert minor_matrix_b2.get_matrix() == [[1, 3], [4, 6], [7, 9]]
        assert minor_matrix_b3.get_matrix() == [[1, 2], [4, 5], [7, 8]]
        assert minor_matrix_b4.get_matrix() == [[2, 3], [5, 6]]
    
    def test_determinant(self) -> None:
        """Test Matrix.determinant"""
        matrix_a = Matrix(3, 3)
        matrix_a.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        matrix_b = Matrix(2, 2)

        matrix_c = Matrix(4, 4)

        matrix_d = Matrix(4, 4)
        matrix_d.set_matrix([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]])

        assert matrix_a.determinant() == 0
        assert matrix_b.determinant() == 0
        assert matrix_c.determinant() == 0
        assert matrix_d.determinant() == -376
