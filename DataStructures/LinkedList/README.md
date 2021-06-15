# LinkedLists

## Initializing a Linked list

You can initialize a linked list by simply creating a linked list object
and optionally pass in a list object witch would contain the initial list
items.

```python
from structlinks.structures import LinkedList

# create an empty linked list
lst = LinkedList()
# create a linked list with initial values
lst = LinkedList([1, 10, -3, 5])
```

## Basic Operations

All of the basic operations are taken from the University of Toronto's CSC111 course.

```python
from structlinks.structures import LinkedList

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

## Additional Operations

### Inverting a Linked List

```python
from structlinks.structures import LinkedList

lst = LinkedList([1, 10, 3, 5])

print(lst)
# Output:
# [1 -> 10 -> 3 -> 5]

lst.invert()  # mutate lst

print(lst)
# Output:
# [5 -> 3 -> 10 -> 1]
```

### Mapping functions to a Linked List

```python
from structlinks.structures import LinkedList

lst = LinkedList([1, 10, 3, 5])

# Map function f(x) = x^2
new_lst = lst.map(lambda x: x ** 2)

print(new_lst)
# Output:
# [25 -> 9 -> 100 -> 1]
```

### Inbuilt Mapping functions

```python
from structlinks.structures import LinkedList

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
