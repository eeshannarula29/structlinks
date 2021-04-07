---
title: searching
filename: searching
--- 

# Searching and Path Finding Algorithms 


## Searching Lists

The list seaching algorithms can be used with `Lists`, `LinkedLists`, and `DoublyLinkedLists`

### Linear Search
 
```python
from NetLinks.SearchingAlgorithms import linear_search

# initalize a list
lst = [1, 100, 4, -1, 5]

print(linear_search(lst, -1))
# Output: True

print(linear_search(lst, 0))
# Output: False
```

### Binary Search

Note that for binary search the list to be searched , should be `sorted`

```python
from NetLinks.SearchingAlgorithms import binary_search

# initalize a sorted list
lst = [-1, 1, 4, 5, 100]

print(binary_search(lst, -1))
# Output: True

print(binary_search(lst, 0))
# Output: False
```

## Path Finding in Graphs

### Algorithms For Un-Weighted Graphs

#### Breadth First Search
```python
from NetLinks.Graphs import Graphs
from NetLinks.SearchingAlgorithms import breadth_first_search

graph = Graph()

graph.add_vertices([1, 2, 3, 5, 7])
graph.add_edges([(1, 2), (2, 3), (3, 1), (3, 5)])

path = breadth_first_search(graph, origin = 1, target = 5)

print(path)
# Output: [(1, 3), (3, 5)]  # <---- Return the edges of the path (1 -> 3 -> 5)

non_existing_path = breadth_first_search(graph, origin = 1, target = 7)  # <-- 1 and 7 are not connected

print(non_existing_path)
# Output: None  
```

#### Depth First Search
```python
from NetLinks.Graphs import Graphs
from NetLinks.SearchingAlgorithms import depth_first_search

graph = Graph()

graph.add_vertices([1, 2, 3, 5])
graph.add_edges([(1, 2), (2, 3), (3, 1), (3, 5)])

path = depth_first_search(graph, origin = 1, target = 5)

print(path)
# Output: [(1, 3), (3, 5)]  # <---- Return the edges of the path (1 -> 3 -> 5)

non_existing_path = depth_first_search(graph, origin = 1, target = 7)  # <-- 1 and 7 are not connected

print(non_existing_path)
# Output: None  
```

### Algorithms For Weighted Graphs

```python
from NetLinks.Graphs import Graphs

graph = Graph()

graph.add_vertices([1, 2, 3, 5, 6, 7])

graph.add_edges([(0, 1, {'weight': 4}),
                 (2, 1, {'weight': 8}),
                 (2, 3, {'weight': 7}),
                 (3, 4, {'weight': 9}),
                 (4, 5, {'weight': 10}),
                 (5, 6, {'weight': 2}),
                 (6, 7, {'weight': 1}),
                 (7, 0, {'weight': 8}),
                 (7, 1, {'weight': 11}),
                 (7, 8, {'weight': 7}),
                 (6, 8, {'weight': 6}),
                 (8, 2, {'weight': 2}),
                 (2, 5, {'weight': 4}),
                 (3, 5, {'weight': 14})])
  
```
##### This is how the graph looks:

<img src="Fig-11.jpg" class="img-responsive" alt="">

#### Dijkstra's Search Algorithm For Single Path
This is Dijkstra's Search Algorithm for getting a path from an `origin` to a specific `target`

```python 
from NetLinks.SearchingAlgorithms import dijkstra_search_target

path = dijkstra_search_target(graph, origin = 0, target: 4, metric: 'weight')

print(path)
# Output: [(0, 7), (7, 6), (6, 5), (5, 4)]  # 0 -> 7 -> 6 -> 5 -> 4
```

#### Dijkstra's Search Algorithm 
This is Dijkstra's Search Algorithm for getting a path from an `origin` to all the other vertices.

```python 
from NetLinks.SearchingAlgorithms import dijkstra_search_target

paths = dijkstra_search_all(graph, origin = 0, metric: 'weight') 

print(paths)
# Output: 
{
  1: [(0, 1)],
  2: [(0, 1), (1, 2)],
  3: [(0, 1), (1, 2), (2, 3)],
  4: [(0, 7), (7, 6), (6, 5), (5, 4)],
  5: [(0, 7), (7, 6), (6, 5)],
  6: [(0, 7), (7, 6)],
  7: [(0, 7)],
  8: [(0, 1), (1, 2), (2, 8)]
}

```
