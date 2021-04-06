## Welcome to NetLinks

Easily Access and visualize different Data structures including Linked lists, Doubly Linked lists, Trees, Binary trees, Graphs, Stacks, and Queues.

I should also mention that much of the Basic data class structure is take from the
University of Toronto's CSC111 course. I and other collaborators are students at
University of Toronto, and currently taking CSC111.

## Current DataTypes

- [Binary Search Trees](https://eeshannarula29.github.io/NetLinks/binary_trees)
- [Graphs](https://eeshannarula29.github.io/NetLinks/graphs)  
- [Linked Lists](#LinkedLists)
- [Doubly Linked Lists](#DoublyLinkedLists)
- [Stacks](https://eeshannarula29.github.io/NetLinks/stacks)
- [Queues](#Queues)

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

## Graphs

### Initialize a Graph
```python
from NetLinks.Graph import Graph

graph = Graph()
```

### Adding Vertices

#### Adding a Single Vertex
A vertex can we added simply by calling `graph.add_vertex`. The function takes in the value of the vertex. 
Additional `Attributes` of the vertex can be passed in as a dictionary. 
```python
from NetLinks.Graph import Graph

graph = Graph()

# Adding a vertex
graph.add_vertex(2)

# Add vertex with attributes 
graph.add_vertex(3, attributes={'type': int, 'is active': True})
```

A error would **not** be raised if a vertex value is added again, instead the attributes 
of the vertex would be updated by the attributes of the new call. 

#### Adding Multiple Vertices
Multiple vertices could be added using the `graph.add_vertices` function, which takes in a list of elements. To
add vertices with attributes the format of the tuple should be `[ ... (value, attribute dictionary) ... ]`. A list
contain both elements with no attributes and elements with attributes. 

```python
from NetLinks.Graph import Graph

graph = Graph()

graph.add_vertices([2, (3, {'type': int, 'is active': True}), 5, ('string', {'type': str})])

print(graph.vertices)
# Output:
# {2, 3, 5, 'string'}
```

Similar to `add_vertex` if a vertex is added with existing value, the attributes of the vertex would be updated and 
no error would be raised.

Note that a vertex can be anything, as shown in the above example. It could be a number, string, dictionary or even
a graph object itself.

### Adding Edges

#### Adding a Single Edge
An edge can be added using the `add_edge` function. Similar to vertices, edges can have attributes which we can pass in as 
an attribute. Note that if a vertex does not exists then the function does **not** raise an error, instead it creates
a new vertex with that value, and adds an edge. Note That if an edge already exists, then similar to vertices, the `attributes`
of the edge would be update if `add_edge` is called.

```python
from NetLinks.Graph import Graph

graph = Graph()

# Add vertices
graph.add_vertices([2, 1, 3, 5])

# Add edge 
graph.add_edge(2, 1)

# Add edge with attributes
graph.add_edge(1, 3, attributes={'weight': 100})

# Add edge between non existing vertex
graph.add_edge(3, 100)

print(graph.edges)
# Output:
# {(2, 1), (1, 3), (3, 100)}
```
Note that `100` was not a vertex, but the function created a new vertex with value `100`, and add an edge between `3` and `100`.

#### Adding multiple Edges
Multiple edges can be added using `add_edges` function. The function takes in a list of tuples, where each tuple represents 
an edge. The format of the tuple could `[... (item1, item2) ...]` , and we can additionally add attributes to the edge 
which would look like `[... (item1, item2, attributes dict) ...]`. Note that similar to `add edge`,  if a vertex does not exists then the function does **not** raise an error, instead it creates
a new vertex with that value, and adds an edge. 

```python
from NetLinks.Graph import Graph

graph = Graph()

# Add vertices
graph.add_vertices([2, 1, 3, 5])

# Add edges
graph.add_edges([(2, 1), (1, 3, {'weight': 100}), (5, 25)])

print(graph.edges)
# Output:
# {(2, 1), (1, 3), (5, 25)}
```

### Clear the Graph
A graph can be cleared using the `clear` function. This would remove all the vertices and edges of the graph.
```python
graph.clear()
```

### Examining elements of a graph

We can read and examine the graph with some helpful function. As you have seen in a few examples above 
`graph.vertices` and `graph.edges` are two properties used to get the unique set of vertices and edges. 

To get the number of vertices and edges you can call `graph.vertices_count()` and `graph.edges_count()`. 

Other functions are `graph.get_neighbours`, `graph.adjacent`, `graph.get_degree`

```python
print(graph.vertices)
# Output: {2, 1, 3, 5}

print(graph.edges)
# Output: {(2, 1), (1, 3)}

print(graph[1].get_neighbours())  # Same as graph.get_neighbours(1)
# Output: {2, 3}

print(graph[2].adjacent(1))  # Same as graph.adjacent(2, 1) or graph.adjacent(1, 2)
# Output: True

print(graph[5].degree)  # Same as graph.get_degree(5)
# Output: 0

# print degree for multiple elements
print(graph.get_degree({1, 3}))
# Output: {1: 2, 3: 1}
```

There are some other functions specific to only vertices like `check_connected`, `get_connected`, and `in_cycle`.

```python
graph[1].check_connected(5)  # check if 1 and 5 are connected
# Output: False

graph[1].get_connected()  # Return all the vertices connected to graph
# Output: {1, 2, 3}

graph[1].in_cycle()  # check if vertex is in a cycle
# Output: False 

# You can also check if the graph is connected or not
print(graph.is_connected)  # check if all vertices in the graph are connected to each other
# Output: False
```

### Remove Vertices and Edges

Removing vertices and edges is similar to adding them. The functions used are `graph.remove_vertex`, `graph.remove_vertices`,
`graph.remove_edge` and `graph.remove_edges`

```python
print(graph.vertices)
# Output: {2, 1, 3, 5, 6, 7}

print(graph.edges)
# Output: {(2, 1), (1, 3), (3, 5), (1, 7), (7, 6), (6, 1)}

# Remove a vertex
graph.remove_vertex(2)  # <--------------- Removing single vertex

# After removing:
print(graph.vertices)
# Output: {1, 3, 5, 6, 7}

print(graph.edges)
# Output: {(1, 3), (3, 5), (1, 7), (7, 6), (6, 1)}

graph.remove_vertices([5, 3])  # <-------- Remove multiple vertices

# After removing:
print(graph.vertices)
# Output: {1, 6, 7}

print(graph.edges)
# Output: {(1, 7), (7, 6), (6, 1)}

graph.remove_edge(1, 7)  # <-------------- Remove a single edge

# After removing:
print(graph.vertices)
# Output: {1, 6, 7}

print(graph.edges)
# Output: {(7, 6), (6, 1)}

graph.remove_edges([(7, 6), (6, 1)]) # <-- Remove multiple edges

# After removing:
print(graph.vertices)
# Output: {1, 6, 7}

print(graph.edges)
# Output: {}
```

### Get/Set the Attributes

```python
from NetLinks.Graph import Graph

graph = Graph()

# Add vertices
graph.add_vertices([1, (2, {'type': int}), 3, ('string', {'type': str})])

# Add edges 
graph.add_edges([(1, 3, {'weight': 10}), (2, 1)])
```

#### Vertex Attributes
```python
print(graph[2].attr)
# Output: {'type': int}

print(graph['string'].attr['type'])
# Output: str

graph[1].attr.update({'type': int})  # Same as graph[1].attr['type'] = int
```

#### Edge Attributes
```python
print(graph[3][1])  # Represents an edge between 1 and 3 
# Output: {'weight': 10}

print(graph[1][2]) # Represents an edge between 1 and 2
# Output: {}

print(graph[1][3]['weight'])  # Return the weight attribute of the edge
# Output: 10

graph[1][2]['type'] = 'numbers'  # Same as graph[1][2].update({'type': 'numbers'})
```

#### Add Global Attributes to All the Vertices of the Graph
```python
graph.add_global_attributes({'weight': 1})  # add this attribute to all the vertices
```

### Graph Generator Functions
```python
from NetLinks.Graph import Graph

graph = Graph()

# Add vertices
graph.add_vertices([1, (2, {'type': int}), 3, ('string', {'type': str})])

# Add edges 
graph.add_edges([(1, 3, {'weight': 10}), ('string', 1, {'weight': 1})])
```
#### Sub-Graph: Filter by Vertex Values
```python
filtered = graph.sub_graph_by_value(lambda x: isinstance(x, int))  # <-- only keep int vertices

print(filtered.vertices)
# Output: {1, 2, 3}

print(filtered.edges)
# Output: {(1, 3)}
```

#### Sub-Graph: Filter by Attribute Values
```python
filtered = graph.sub_graph_by_attribute(attribute='type')  # only keep vertices with attribute 'type'

print(filtered.vertices)
# Output: {2}

print(filtered.edges)
# Output: {}
```

#### Union

```python
other_graph = Graph()

other_graph.add_edges([(1, 7), (9, 0), (3, 10)])

union = graph.union(other_graph)

print(union.vertices)
# Output: {1, 2, 3, 'string', 7, 9, 0, 10}

print(union.edges)
# Output: {(1, 3), (1, 'string'), (1, 7), (9, 0), (3, 10)}
```

### Printing Graphs
```python
from NetLinks.Graph import Graph

graph = Graph()

graph.add_edges([(1, 2), (2, 3), (4, 5), (5, 6), (6, 1)])

print(graph)
# Output:
# { 
# 1: {2, 6} 
# 2: {1, 3} 
# 3: {2} 
# 4: {5} 
# 5: {4, 6} 
# 6: {1, 5} 
# }
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

## Queues

### Initialize a Normal Queue

```python
from NetLinks.Queue import Queue

# initialize empty queue
queue = Queue()

# initialize queue with list
queue_with_list = Queue([1, 2, 3])

print(queue)
# Output:
# Entry ------------> Exit 
#       1 -> 2 -> 3
# ------------------------
```

### Initialize a Priority Queue
```python
from NetLinks.Queue import Queue

priority_func = lambda x: len(x)

queue = Queue(['hi', 'hello', 'hey'], metric = priority_func)

print(queue)
# Output:
# Entry -------------------> Exit 
#       hi -> hey -> hello
# -------------------------------
```

### Initialize Queue / Priority Queue with Limit
Add a limit to the queue to limit the number of elements in a queue, This can be done by adding limit
attribute while initializing a queue.
```python
from NetLinks.Queue import Queue

queue = Queue(['hi', 'hello', 'hey'], limit = 5)
```

### Interchange between Queue and Priority Queue
Queue and Priority Queue are interchangeable and can be converted from one to another
#### Queue --> Priority Queue
```python
from NetLinks.Queue import Queue

# Initialize a queue
queue = Queue(['hi', 'hello', 'hey'])

# define a priority function
priority_func = lambda x: len(x)

# convert Queue to Priority Queue
queue.change_metric(priority_func)
```
#### Priority Queue --> Queue
```python
from NetLinks.Queue import Queue

# define a priority function
priority_func = lambda x: len(x)

# Initialize a Priority Queue
queue = Queue(['hi', 'hello', 'hey'], metric = priority_func)

# convert Priority Queue to Queue
queue.change_metric(None)
```

### Change Limit 
```python
from NetLinks.Queue import Queue

# Initialize a queue with limit 
queue = Queue(['hi', 'hello', 'hey'], limit = 3)

queue.change_limit(4)  # <---- changes the limit to 4

queue.change_limit(None)  # <---- removes the limit
```

### Check for Empty / Filled Queue
```python
from NetLinks.Queue import Queue

# Initialize a queue with limit 
queue = Queue(['hi', 'hello', 'hey'], limit = 3)

print(queue.is_filled)
# Output:
# True

print(queue.is_empty)
# Output:
# False
```

### Enqueue / Push Elements
The function used to enqueue/push element from queue, takes constant time. If the limit of the queue has been obtained 
the `QueueLimitReachedError` will be raised.
```python
from NetLinks.Queue import Queue

# Initialize a queue
queue = Queue([100, 200, 300])

print(queue)
# Output:
# Entry ------------------> Exit 
#       100 -> 200 -> 300
# ------------------------------

queue.enqueue(50)  # <--- push 50 into the queue

print(queue)
# Output:
# Entry ------------------------> Exit 
#       50 -> 100 -> 200 -> 300
# ------------------------------------
```

### Dequeue / Pop Elements
The function used to Dequeue/Pop element, takes constant time. If the queue is empty then
the `EmptyQueueError` will be raised.
```python
from NetLinks.Queue import Queue

# Initialize a queue
queue = Queue([100, 200, 300])

print(queue)
# Output:
# Entry ------------------> Exit 
#       100 -> 200 -> 300
# ------------------------------

element = queue.dequeue()  # <--- pop element

print(element)
# Output:
# 300

print(queue)
# Output:
# Entry -----------> Exit 
#       100 -> 200
# -----------------------
```

### Extend Queue
```python
from NetLinks.Queue import Queue

q1 = Queue([100, 200, 300])
q2 = Queue([400, 500, 600])

q2.extend(q1)  # <--- Extend q2 by q1

print(q2)
# Output:
# Entry ---------------------------------------> Exit 
#       100 -> 200 -> 300 -> 400 -> 500 -> 600
# ---------------------------------------------------
```

### Map a Queue
```python
from NetLinks.Queue import Queue

# Initialize a queue
queue = Queue([1, 2, 3])

# create a mapping function
mapping_function = lambda x: x ** 2

# map the function to queue
queue.map(mapping_function)

print(queue)
# Output:
# Entry ------------> Exit 
#       1 -> 4 -> 9
# ------------------------
```

### Printing Custom Queues
Queues can be printed to get specific properties of a elements in the queue. 
```python
from NetLinks.Queue import Queue
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    
david = Person('David')
mario = Person('Mario')

people_queue = Queue([david, mario])

people_queue.display(lambda person: person.name)
# Output:
# Entry ---------------> Exit 
#       David -> Mario
# ---------------------------
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
