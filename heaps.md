---
title: Heaps
filename: heaps
---


# Heap

## Max and Min Heap

max and min heap classes work exactly the same way so, I would only work with max heap here

### Initalization

```python
from structlinks.DataStructures import MaxHeap, MinHeap

# Empty heap
max_heap = MaxHeap()

# With Inital Values
max_heap = MaxHeap([20, 25, 50, 10, 3])
```

### Printing the heap

```python
print(max_heap)
# Output:
#     _50_
#    /    \
#   25   20
#  /  \
# 10  3

print(max_heap.display())
# Output:
#     _50_
#    /    \
#   25   20
#  /  \
# 10  3

print(max_heap.display(listed = True))
# Output: [50, 25, 20, 10, 3]
```

### Push and Pop

```python
result = max_heap.pop()  # the popped element is saved in result variable

print(max_heap)
# Output:
#    25_
#   /   \
#  10  20
# /
# 3

max_heap.push(16)

print(max_heap)
# Output:
#    __25_
#   /     \
#  16_   20
# /   \
# 3  10
```

### Size and Height Properties

```python
print(max_heap.size)
# Output: 5

print(max_heap.height)
# Output: 3
```

## Create Custom Heaps

Custom heaps can be created which can contain all the python in-built and any other self declared objects. Follow
the steps below to create a custom heap.

-   first we define the comparison function which compares two elements of the Heap. The function is
    defined as an `PriorityFunction` object. The object takes a function which is used for comparion.
    The passed in function should contain two parameters `compare_to` and `compare_from`, and when it returns
    _True_, `compare_to` should be give priority to `compare_from`.

    Here we would create a `PriorityFunction` to comapre two strings and give priority to the string with
    greater length

```python
from structlinks.DataStructures import PriorityFunction

def comparing_function (compare_to, compare_from) :
    return len(compare_to) >= len(compare_from)

priority_function = PriorityFunction(comparing_function)
```

-   Now, we would use the `priority_function` to create a heap

```python
from structlinks.DataStructures import Heap

# Empty Heap
heap = Heap(prioritizer = priority_function)

# Heap with inital values
heap = Heap(prioritizer = priority_function, inital_heep = ['hi', 'hello', 'bye'])
```

**All the methods are same as Max and Min heap for the Custom heaps**
