# Matrix

## Initialise Matrix

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix)
# Output:
#[[1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]]
```

## Shape of the Matrix

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix.shape)
# Output:
# (3, 3)
```

## Get/Set Items

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[1, 1] == 5)
# Output: True

print(matrix[1, :])
# Output: Matrix([[4, 5, 6]])

matrix[1, 1] = 100

matrix[2, 1:] = Matrix([[11, 12]])

print(matrix)
# Output:
#[[1, 2, 3]
# [4, 100, 6]
# [7, 11, 12]]
```

## Other Properties

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# check whether the matrix is a square matrix
print(matrix.is_square)
# Output: True

# check whether the matrix is a vector
print(matrix.is_vector)
# Output: False

# check whether the matrix is invertable
print(matrix.is_invertible)
# Output: False
```

## Add Constant

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_matrix = matrix.add_scalar(10)

print(new_matrix)
# Output:
#[[11, 12, 13]
# [14, 15, 16]
# [17, 18, 19]]
```

## Multiply Constant

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_matrix = matrix.multiply_scalar(10)

print(new_matrix)
# Output:
#[[10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]]
```

## Map Function

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_matrix = matrix.map(lambda x: x ** 2)

print(new_matrix)
# Output:
#[[1, 4, 9]
# [16, 25, 36]
# [49, 64, 81]]
```

## Create Zero, One, and Identity Matrix

```python
from structlinks.DataStructures import Matrix

zeros = Matrix.zeros(shape = (2, 1))

print(zeros)
# Output:
# [[0],
#  [0]]

ones = Matrix.ones(shape = (1, 2))

print(ones)
# Output:
# [[1, 1]]

indentity = Matrix.identity(order = 2)

print(indentity)
# Output:
# [[1, 0],
#  [0, 1]]
```

## Add Matrices

```python
from structlinks.DataStructures import Matrix

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

m3 = m1.add_matrix(m2)

print(m3)
# Output:
# [[11, 13, 15],
#  [17, 19, 21],
#  [23, 25, 27]]
```

## Matrix Multiplication (Cross Product)

```python
from structlinks.DataStructures import Matrix

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

m3 = m1.multiply_matrix(m2)

print(m3)
# Output:
# [[84, 90, 96]
#  [201, 216, 231]
#  [318, 342, 366]]
```

## Dot Product

```python
from structlinks.DataStructures import Matrix

m1 = Matrix([[1, 2, 3]])
m2 = Matrix([[4, 5, 6]])

m3 = m1.dot_multiply(m2)

print(m3)
# Output:
# [[32]]
```

## Stack Matrices

### Horizontal Stack

```python
from structlinks.DataStructures import Matrix

m1 = Matrix([[1, 2],[3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = Matrix([[9, 10], [11, 12]])

m4 = Matrix.hstack([m1, m2, m3])

print(m4)

#Output:
# [[1, 2, 5, 6, 9, 10]
#  [3, 4, 7, 8, 11, 12]]
```

### Vertical Stack

```python
from structlinks.DataStructures import Matrix

m1 = Matrix([[1, 2],[3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = Matrix([[9, 10], [11, 12]])

m4 = Matrix.vstack([m1, m2, m3])

print(m4)

#Output:
# [[1, 2]
#  [3, 4]
#  [5, 6]
#  [7, 8]
#  [9, 10]
#  [11, 12]]
```

## Transpose Matrix

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix)
# Output:
#[[1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]]

print(matrix.transpose)
# Output:
#[[1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]]
```

## Determinant

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix.determinant)
# Output: 0
```

## Inverse

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.inverse)
# Output:
#[[1.0, -0.5, -1.0]
# [1.0, -1.0, -1.0]
# [3.0, -2.5, -4.0]]
```

## Cofactor

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.cofactor)
# Output:
# [[2, 2, 6]
#  [-1, -2, -5]
#  [-2, -2, -8]]
```

## Adjacent

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.adjacent)
# Output:
# [[2, -1, -2]
#  [2, -2, -2]
#  [6, -5, -8]]
```

## Row Reduced Echolon Form (Rref)

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.rref)

# Output:
# [[1.0, 0.0, 0.0]
#  [-0.0, 1.0, 0.0]
#  [-0.0, -0.0, 1.0]]
```

## Rank and Nullity

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.rank)
# Output: 3
print(matrix.nullity)
# Output: 0
```

## Linear Indipendence and Dependence

```python
from structlinks.DataStructures import Matrix

matrix = Matrix([[3, 1, -1], [2, -2, 0], [1, 2, -1]])

print(matrix.linearly_independent)
# Output: True

print(matrix.linearly_dependent)
#Output: False

print(matrix.get_independent_vectors())
# Output:
# [Matrix([[3, 1, -1]]),
#  Matrix([[2, -2, 0]]),
#  Matrix([[1, 2, -1]])]

print(matrix.get_dependent_vectors())
# Output: []
```
