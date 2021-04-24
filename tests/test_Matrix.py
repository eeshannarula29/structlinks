"""This file contains tests for the Matrix library"""

from Matrix import Matrix


class TestMatrix:

    def test_multiply_scalar(self) -> None:
        """Test Matrix.multiply_scalar"""
        matrix = Matrix.ones((3, 3))
        new_matrix = matrix.multiply_scalar(3)

        assert all(new_matrix[i][j] == 3 for i in range(0, new_matrix.shape[0])
                   for j in range(0, new_matrix.shape[1]))

    def test_add_matrix(self) -> None:
        """Test Matrix.add_matrix"""
        matrix_a = Matrix.ones((3, 3))
        matrix_b = Matrix.ones((3, 3))

        sum_matrix = matrix_a.add_matrix(matrix_b)

        assert all(sum_matrix[i][j] == 2 for i in range(0, sum_matrix._row_count)
                   for j in range(0, sum_matrix._col_count))

    def test_is_square(self) -> None:
        """Test Matrix.is_square"""
        matrix_a = Matrix.ones((4, 4))
        matrix_b = Matrix.ones((1, 3))

        assert matrix_a.is_square and not matrix_b.is_square

    def test_minor(self) -> None:
        """Test Matrix.minor"""
        matrix_a = Matrix.ones((1, 2))
        minor_matrix_a = matrix_a.minor(0, 1)

        matrix_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        minor_matrix_b = matrix_b.minor(0, 0)
        minor_matrix_b2 = matrix_b.minor(1, 1)
        minor_matrix_b3 = matrix_b.minor(2, 2)
        minor_matrix_b4 = matrix_b.minor(2, 0)

        assert minor_matrix_a.to_list() == []
        assert minor_matrix_b.to_list() == [[5, 6], [8, 9]]
        assert minor_matrix_b2.to_list() == [[1, 3], [7, 9]]
        assert minor_matrix_b3.to_list() == [[1, 2], [4, 5]]
        assert minor_matrix_b4.to_list() == [[2, 3], [5, 6]]

    def test_determinant(self) -> None:
        """Test Matrix.determinant"""
        matrix_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        matrix_b = Matrix.ones((2, 2))

        matrix_c = Matrix.ones((4, 4))

        matrix_d = Matrix([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]])

        assert matrix_a.determinant() == 0
        assert matrix_b.determinant() == 0
        assert matrix_c.determinant() == 0
        assert matrix_d.determinant() == -376
