# NetLinks

NetLinks can be used to access different DataTypes, like Linked list, Doubly Linked lists, Trees, Binary trees,
and may more. You can even visualize them. It also can be used to sort and search items in these data types.

I should also mention that much of the Basic data class structure is take from the
University of Toronto's CSC111 course.

I and other collaborators are students at
University of Toronto, and currently taking CSC111.

Some code is also taken from other sources like Stackoverflow and Geeksforgeeks. All the
References are mentioned at the bottom of the file.

## Current DataTypes

- [Binary Search Trees](#BinarySearchTrees)
- [Linked Lists](#LinkedLists)
- [Doubly Linked Lists](#DoublyLinkedLists)
- [Stacks](#Stacks)

## Current Sorting Algorithms

- [Merge Sort (In Place)](#MergeSort-InPlace)
- [Merge Sort (Non-Mutating)](#MergeSort-NonMutating)
- [Quick Sort (In Place)](#QuickSort-InPlace)
- [Quick Sort (Non-Mutating)](#QuickSort-NonMutating)
- [Selection Sort](#SelectionSort)
- [Insertion Sort](#InsertionSort)

## Contribute to NetLinks
We are very glad 😃 that you want to contribute to our project. We welcome you to our communtiy. Please
check the [CONTRIBUTING.md](https://github.com/eeshannarula29/NetLinks/blob/main/CONTRIBUTING.md) file
for further information on how you can contribute.

## Learn Github
These are some resourses you can use to learn the basics of Github. You can always come to the [Discussion board](https://github.com/eeshannarula29/NetLinks/discussions) to discuss the concepts you lernt or have problems with.
- [Intro to Git and Github by Daniel Shiffman](https://youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV)
- [Guide to Contributing](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)

## Discussion Board
You can clarify all of your queries about github nand collborating on the [Discussion Board](https://github.com/eeshannarula29/NetLinks/discussions)

## BinarySearchTrees

### Initialize a BST

BST can be initialized in two ways, first by a list, which makes a balanced binary search tree or
by constructing a tree from scratch.

#### From list
```python
from NetLinks.BinaryTree import BinarySearchTree

bst = BinarySearchTree.create_tree([1, 2, 4, 10, 20, 30, 3])

print(bst)

# Output:
#   _4___
#  /     \
#  2    20_
# / \  /   \
# 1 3 10  30
```

#### From Scratch
```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Printing BST

#### Branched Form
```python
from NetLinks.BinaryTree import BinarySearchTree

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

#### Indented Form
```python
from NetLinks.BinaryTree import BinarySearchTree

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
### Properties
```python
from NetLinks.BinaryTree import BinarySearchTree

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
### Insert Item in BST

```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Remove Item from BST

```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Convert to List

```python
from NetLinks.BinaryTree import BinarySearchTree

bst = BinarySearchTree.create_tree([2, 1, 3, 5, 4])

print(bst.to_list())

# Output:
# [1, 2, 3, 4, 5]
```

### Item in BST

```python
from NetLinks.BinaryTree import BinarySearchTree

bst = BinarySearchTree.create_tree([2, 1, 3, 3, 5, 4])

print(3 in bst)
# Output:
# True

print(100 in bst)
# Output:
# False
```

### Invert the BST

```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Balance the BST

```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Mapping a BST

#### Mutate existing tree
```python
from NetLinks.BinaryTree import BinarySearchTree

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

#### Creating new Mapped BST
```python
from NetLinks.BinaryTree import BinarySearchTree

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

### Some other methods

```python
from NetLinks.BinaryTree import BinarySearchTree

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

## LinkedLists
### Initializing a Linked list
You can initialize a linked list by simply creating a linked list object
and optionally pass in a list object witch would contain the initial list
items.

```python
from NetLinks.LinkedList import LinkedList

# create an empty linked list
lst = LinkedList()
# create a linked list with initial values
lst = LinkedList([1, 10, -3, 5])
```

### Basic Operations

All of the basic operations are taken from the University of Toronto's CSC111 course.
```python
from NetLinks.LinkedList import LinkedList

lst = LinkedList([1, 10, 3, 5])

# print the list
print(lst)  # this will print : [1 -> 10 -> 3 -> 5]

# Length of the list
length = len(lst)  # length = 4

# Append items
lst.append(2)  # After the call, lst = [1 -> 10 -> 3 -> 5 -> 2]

# Insert items
lst.insert(0, 200)  # After the call, lst = [200 -> 1 -> 10 -> 3 -> 5 -> 2]

# Get & Set item by index
item = lst[1]  # here item = 10
lst[2] = 100  # set element at index 2 to be 100, so lst = [200 -> 1 -> 100 -> 3 -> 5 -> 2]

# Slicing the list
part = lst[2:]  # here part = [100 -> 3 -> 5 -> 2]

# Removing element
# 1) by index
popped = lst.pop(0)  # here popped = 200, and lst = [1 -> 100 -> 3 -> 5 -> 2]
# 2) by item value
lst.remove(1) # now list lst = [100 -> 3 -> 5 -> 2]

# Checking for Element
cond1 = 2 in lst  # here cond1 is True as 2 is in lst
cond2 = 1 in lst  # here cond2 is False as 1 is not in lst

# Adding to Linked Lists
lst1 = LinkedList([1, 10, 3, 5])
lst2 = LinkedList([2, 100, 4, 0])
lst3 = lst1 + lst2  # lst3 = [1 -> 10 -> 3 -> 5 -> 2 -> 100 -> 4 -> 0]

# Count of an item
count = lst.count(2)  # count = 1 as 2 appears only once

# Index of an item (return -1 if element not in lst)
index = lst.index(100)  # index = 0 as 100 is at index 0

# Equating to lists
cond3 = lst1 == lst2  # cond3 = False as lst1 and lst2 have different elements

# Sort the list
lst.sort()  # lst will be mutated to [2 -> 3 -> 5 -> 100]

# Extend the list
lst.extend(lst2)  # lst will be mutated to [2 -> 3 -> 5 -> 100 -> 2 -> 100 -> 4 -> 0]

# Copy the list
lst4 = lst.copy()  # lst4 is a copy of lst
```

### Additional Operations

#### Inverting a Linked List
```python
from NetLinks.LinkedList import LinkedList

lst = LinkedList([1, 10, 3, 5])

print(lst)
# Output:
# [1 -> 10 -> 3 -> 5]

lst.invert()  # mutate lst

print(lst)
# Output:
# [5 -> 3 -> 10 -> 1]
```

#### Mapping functions to a Linked List
```python
from NetLinks.LinkedList import LinkedList

lst = LinkedList([1, 10, 3, 5])

# Map function f(x) = x^2
new_lst = lst.map(lambda x: x ** 2)

print(new_lst)
# Output:
# [25 -> 9 -> 100 -> 1]
```

#### Inbuilt Mapping functions
```python
from NetLinks.LinkedList import LinkedList

lst = LinkedList([1.1, 10.5, -3.7, 5.2])

#abs
abs_lst = lst.abs()

print(abs_lst)
# Output:
# [1.1 -> 10.5 -> 3.7 -> 5.2]

# floor
floor_lst = lst.floor()

print(floor_lst)
# Output:
# [1.0 -> 10.0 -> 3.0 -> 5.0]

# ceil
ceil_lst = lst.ceil()

print(ceil_lst)
# Output:
# [2.0 -> 11.0 -> 4.0 -> 6.0]
```

## DoublyLinkedLists

### Initializing a Doubly Linked list
You can initialize a Doubly linked list by simply creating a Doubly linked list object
and optionally pass in a list object witch would contain the initial list
items.

```python
from NetLinks.LinkedList import DoublyLinkedList

# create an empty linked list
lst = DoublyLinkedList()
# create a linked list with initial values
lst = DoublyLinkedList([1, 10, -3, 5])
```

### Basic Operations
The idea for all of the basic operations is similar to that of Linked lists, which were taken
from the University of Toronto's CSC111 course.
```python
from NetLinks.LinkedList import DoublyLinkedList

lst = DoublyLinkedList([1, 10, 3, 5])

# print the list
print(lst)  # this will print : [1 <--> 10 <--> 3 <--> 5]

# Length of the list
length = len(lst)  # length = 4

# Append items
lst.append(2)  # After the call, lst = [1 <--> 10 <--> 3 <--> 5 <--> 2]

# Insert items
lst.insert(0, 200)  # After the call, lst = [200 <--> 1 <--> 10 <--> 3 <--> 5 <--> 2]

# Get & Set item by index
item = lst[1]  # here item = 10
lst[2] = 100  # set element at index 2 to be 100, so lst = [200 <--> 1 <--> 100 <--> 3 <--> 5 <--> 2]

# Slicing the list
part = lst[2:]  # here part = [100 <--> 3 <--> 5 <--> 2]

# Removing element
# 1) by index
popped = lst.pop(0)  # here popped = 200, and lst = [1 <--> 100 <--> 3 <--> 5 <--> 2]
# 2) by item value
lst.remove(1) # now list lst = [100 <--> 3 <--> 5 <--> 2]

# Checking for Element
cond1 = 2 in lst  # here cond1 is True as 2 is in lst
cond2 = 1 in lst  # here cond2 is False as 1 is not in lst

# Adding to Doubly Linked Lists
lst1 = DoublyLinkedList([1, 10, 3, 5])
lst2 = DoublyLinkedList([2, 100, 4, 0])
lst3 = lst1 + lst2  # lst3 = [1 <--> 10 <--> 3 <--> 5 <--> 2 <--> 100 <--> 4 <--> 0]

# Count of an item
count = lst.count(2)  # count = 1 as 2 appears only once

# Index of an item (return -1 if element not in lst)
index = lst.index(100)  # index = 0 as 100 is at index 0

# Equating to lists
cond3 = lst1 == lst2  # cond3 = False as lst1 and lst2 have different elements

# Sort the list
lst.sort()  # lst will be mutated to [2 <--> 3 <--> 5 <--> 100]

# Extend the list
lst.extend(lst2)  # lst will be mutated to [2 <--> 3 <--> 5 <--> 100 <--> 2 <--> 100 <--> 4 <--> 0]

# Copy the list
lst4 = lst.copy()  # lst4 is a copy of lst
```

### Additional Operations

#### Inverting a Doubly Linked List
```python
from NetLinks.DoublyLinkedList import DoublyLinkedList

lst = DoublyLinkedList([1, 10, 3, 5])

print(lst)
# Output:
# [1 <--> 10 <--> 3 <--> 5]

lst.invert()  # mutate lst

print(lst)
# Output:
# [5 <--> 3 <--> 10 <--> 1]
```

#### Mapping functions to a Doubly Linked List
```python
from NetLinks.DoublyLinkedList import DoublyLinkedList

lst = DoublyLinkedList([1, 10, 3, 5])

# Map function f(x) = x^2
new_lst = lst.map(lambda x: x ** 2)

print(new_lst)
# Output:
# [25 <--> 9 <--> 100 <--> 1]
```

#### Inbuilt Mapping functions
```python
from NetLinks.DoublyLinkedList import DoublyLinkedList

lst = DoublyLinkedList([1.1, 10.5, -3.7, 5.2])

#abs
abs_lst = lst.abs()

print(abs_lst)
# Output:
# [1.1 <--> 10.5 <--> 3.7 <--> 5.2]

# floor
floor_lst = lst.floor()

print(floor_lst)
# Output:
# [1.0 <--> 10.0 <--> 3.0 <--> 5.0]

# ceil
ceil_lst = lst.ceil()

print(ceil_lst)
# Output:
# [2.0 <--> 11.0 <--> 4.0 <--> 6.0]
```

## Stacks

### Initialize a stack
```python
from NetLinks.Stack import Stack

# initialize empty stack
stack = Stack()

# initialize stack with a list
stack_with_list = Stack([1, 2, 3, 4, 5])


print(stack_with_list)
# Output:

# |          5         | 
# |          4         | 
# |          3         | 
# |          2         | 
# |          1         | 
# |____________________|

```

### Push Elements 

```python
from NetLinks.Stack import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         | 
# |          1         | 
# |____________________|

stack.push(3)

print(stack)
# Output:

# |          3         | 
# |          2         | 
# |          1         | 
# |____________________|
```

### Push multiple Elements
```python
from NetLinks.Stack import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         | 
# |          1         | 
# |____________________|

stack.push_multiple([3, 4, 5])

print(stack)
# Output:

# |          5         | 
# |          4         | 
# |          3         | 
# |          2         | 
# |          1         | 
# |____________________|
```

### Pop Elements
```python
from NetLinks.Stack import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         | 
# |          1         | 
# |____________________|

stack.pop()

print(stack)
# Output:

# |          1         | 
# |____________________|
```

### Extend and Add Stacks
```python
from NetLinks.Stack import Stack

stack1 = Stack([1, 2])
stack2 = Stack([3, 4])

# adding two stacks
stack3 = stack1 + stack2

print(stack3)
# Output:

# |          4         | 
# |          3         | 
# |          2         | 
# |          1         | 
# |____________________|

# extend stack1
stack1.extend(stack2)

print(stack1)
# Output:

# |          4         | 
# |          3         | 
# |          2         | 
# |          1         | 
# |____________________|
```

### Map Stack to a function
```python
from NetLinks.Stack import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         | 
# |          1         | 
# |____________________|

# map to f(x) = x^2
mapped = stack.map(lambda x: x ** 2)

print(mapped)
# Output:

# |          4         | 
# |          1         | 
# |____________________|

print(stack)  # <---- stack did not get mutated
# Output:

# |          2         | 
# |          1         | 
# |____________________|
```

### Invert a Stack
```python
from NetLinks.Stack import Stack

stack = Stack([1, 2, 3])

print(stack)
# Output:

# |          3         |
# |          2         | 
# |          1         | 
# |____________________|

stack.invert()

print(stack)
# Output:

# |          1         | 
# |          2         | 
# |          3         |
# |____________________|
```

## MergeSort-InPlace
Use an inplace mergesort algorithm to return a sorted list.
This version is inferior (in terms of running time) to the non-mutating implementation of mergesort.
```python
from NetLinks.SortingAlgorithms import mergesort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
return_value = mergesort(lst)

print(lst)
# Output:
# [1, 4, 20, 50, 100]

print(return_value)
# Output:
# None
```

## MergeSort-NonMutating
Use mergesort algorithm to return a sorted list.
```python
from NetLinks.SortingAlgorithms import no_mut_mergesort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
sorted_lst = no_mut_mergesort(lst)

print(lst)
# Output:
# [1, 100, 50, 20, 4]

print(sorted_lst)
# Output:
# [1, 4, 20, 50, 100]
```


## QuickSort-InPlace
Use quicksort algorithm to return a sorted list. This is a *mutating* method: it modifies the input instead of returning an output.
```python
from NetLinks.SortingAlgorithms import quicksort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
return_value = quicksort(lst)

print(lst)
# Output:
# [1, 4, 20, 50, 100]

print(return_value)
# Output:
# None
```

## QuickSort-NonMutating
Use quicksort algorithm to return a sorted list. This is a *non-mutating* method: the input list will be preserved.
Note that the runtime of this version is technically inferior to the mutating version of quicksort, above.
```python
from NetLinks.SortingAlgorithms import no_mut_quicksort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
sorted_lst = no_mut_quicksort(lst)

print(lst)
# Output:
# [1, 100, 50, 20, 4]

print(sorted_lst)
# Output:
# [1, 4, 20, 50, 100]
```

## SelectionSort
Use the selection sort algorithm to return a sorted list. This is a mutating method that changes the input list.
```python
from NetLinks.SortingAlgorithms import selection_sort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
return_value = selection_sort(lst)

print(lst)
# Output:
# [1, 4, 20, 50, 100]

print(return_value)
# Output:
# None
```

## InsertionSort
Use the insertion sort algorithm to return a sorted list. Like selection sort, this is a mutating algorithm that modifies it's input
```python
from NetLinks.SortingAlgorithms import insertion_sort

# initialize a list
lst = [1, 100, 50, 20, 4]
# make a sorted list
return_value = insertion_sort(lst)

print(lst)
# Output:
# [1, 4, 20, 50, 100]

print(return_value)
# Output:
# None
```

## Sorting Algorithms: The Key Parameter
Each sorting algorithm accepts an optional `key` parameter: pass in a function to adjust the weighting scheme (or control the values of) of the elements in the list.

For example, if we wanted to sort the list from largest to smallest (rather than smallest to largest, as is default), we can:
```python
from NetLinks.SortingAlgorithms import insertion_sort

# Define a function that reverses the weighting of integers
def invert(x: int) -> int:
    return -x

# initialize a list
lst = [1, 100, 50, 20, 4]
# Sort the list, passing in the function as a key
return_value = insertion_sort(lst, key=invert)

print(lst)
# Output:
# [100, 50, 20, 4, 1]

print(sorted_lst)
# Output:
# None
```

## References

- [BST printitng](https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162)
- [University of Toronto](https://web.cs.toronto.edu/)
- [Stackoverflow](https://stackoverflow.com/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/)
