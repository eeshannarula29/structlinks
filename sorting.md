---
title: SortingAlgorithms
filename: sorting
--- 

# Sorting Algorithms

All the sorting algorithms in this module work with `lists`, `LinkedLists` and `DoublyLinkedLists`

## MergeSort-InPlace

Use an inplace mergesort algorithm to return a sorted list.
This version is inferior (in terms of running time) to the non-mutating implementation of mergesort.

```python
from structlinks.algorithms.sorting_algorithms import mergesort

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
from structlinks.algorithms.sorting_algorithms import no_mut_mergesort

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

Use quicksort algorithm to return a sorted list. This is a _mutating_ method: it modifies the input instead of returning an output.

```python
from structlinks.algorithms.sorting_algorithms import quicksort

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

Use quicksort algorithm to return a sorted list. This is a _non-mutating_ method: the input list will be preserved.
Note that the runtime of this version is technically inferior to the mutating version of quicksort, above.

```python
from structlinks.algorithms.sorting_algorithms import no_mut_quicksort

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
from structlinks.algorithms.sorting_algorithms import selection_sort

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
from structlinks.algorithms.sorting_algorithms import insertion_sort

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

# Sorting Algorithms: The Key Parameter

Each sorting algorithm accepts an optional `key` parameter: pass in a function to adjust the weighting scheme (or control the values of) of the elements in the list.

For example, if we wanted to sort the list from largest to smallest (rather than smallest to largest, as is default), we can:

```python
from structlinks.algorithms.sorting_algorithms import insertion_sort

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
