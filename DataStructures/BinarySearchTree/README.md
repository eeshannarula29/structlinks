# BinarySearchTrees

## Initialize a BST

BST can be initialized in two ways, first by a list, which makes a balanced binary search tree or
by constructing a tree from scratch.

### From list

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20, 30, 3])

print(bst)

# Output:
#   _4___
#  /     \
#  2    20_
# / \  /   \
# 1 3 10  30
```

### From Scratch

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree(7)

left = BinarySearchTree(3)
left.set_left_to(BinarySearchTree(2))
left.set_right_to(BinarySearchTree(5))

right = BinarySearchTree(11)
right.set_left_to(BinarySearchTree(9))
right.set_right_to(BinarySearchTree(13))

bst.set_left_to(left)
bst.set_right_to(right)

print(bst)

# Output:
#   _7__
#  /    \
#  3   11_
# / \ /   \
# 2 5 9  13
```

## Printing BST

### Branched Form

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20, 30, 3])

bst.display()

# Output:
#   _4___
#  /     \
#  2    20_
# / \  /   \
# 1 3 10  30

# or instead

print(bst)

# Output:
#   _4___
#  /     \
#  2    20_
# / \  /   \
# 1 3 10  30
```

### Indented Form

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20, 30, 3])

bst.display(indented = True)

 # Output:
 # |->4
 #   |->2
 #     |->1
 #     |->3
 #   |->20
 #     |->10
 #     |->30
```

## Properties

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20])

print(bst)

# Output:
#   4___
#  /    \
#  2   20
# /   /
# 1  10

print(bst.root) # root value
# Output:
# 4

print(bst.left) # copy of left child
# Output:
#   2
#  /
# 1

print(bst.right) # copy of right child
# Output:
#   20
#  /
# 10

print(bst.height) # height of the tree
# Output:
# 3

print(bst.is_balanced) # Weather tree is balanced
# Output:
# True
```

## Insert Item in BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20])

print(bst)

# Output:
#   4___
#  /    \
#  2   20
# /   /
# 1  10

bst.insert(3)

print(bst)

# Output:
#   _4___
#  /     \
#  2    20
# / \  /
# 1 3 10
```

## Remove Item from BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 3, 4, 5])

print(bst)

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

bst.remove(2)

print(bst)

# Output:
#  3_
# /  \
# 1  5
#   /
#   4
```

## Convert to List

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([2, 1, 3, 5, 4])

print(bst.to_list())

# Output:
# [1, 2, 3, 4, 5]
```

## Item in BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([2, 1, 3, 3, 5, 4])

print(3 in bst)
# Output:
# True

print(100 in bst)
# Output:
# False
```

## Invert the BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 3, 4, 5])

print(bst)

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

bst.invert()

print(bst)

# Output:
#  _3
# /  \
# 5  2
#  \  \
#  4  1
```

## Balance the BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree(5)
right = BinarySearchTree(6)
right.set_right_to(BinarySearchTree(7))
bst.set_right_to(right)

print(bst)

# Output:
# 5
#  \
#  6
#   \
#   7


bst.balance()

print(bst)

# Output:
#  6
# / \
# 5 7
```

## Mapping a BST

### Mutate existing tree

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 3, 4, 5])

print(bst)

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

bst.apply(lambda x: x ** 2) # <---- mapping x to x^2

print(bst)

# Output:
#   9___
#  /    \
#  4   25
# /   /
# 1  16
```

### Creating new Mapped BST

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 3, 4, 5])

print(bst)

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

mapped = bst.map(lambda x: x ** 2) # <---- mapping x to x^2

print(mapped)

# Output:
#   9___
#  /    \
#  4   25
# /   /
# 1  16

print(bst)  # bst did not change

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4
```

## Some other methods

```python
from structlinks.DataStructures import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 3, 4, 5])

print(bst)

# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

# Maximum item in the tree
print(bst.maximum())
# Output:
# 5

# Minimum item in the tree
print(bst.mimimum())
# Output:
# 1

# Copy BST
print(bst.copy())
# Output:
#   3_
#  /  \
#  2  5
# /  /
# 1  4

# abs, floor, and ceil
abs_bst = bst.abs()  # <- map abs to all element of bst
floor_bst = bst.floor()  # <- map floor to all element of bst
ceil_bst = bst.ceil()  # <- map ceil to all element of bst
```
