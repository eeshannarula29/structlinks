---
title: Graphs
filename: graphs
--- 

# Graphs

## Initialize a Graph
```python
from structlinks import Graph

graph = Graph()
```

## Adding Vertices

### Adding a Single Vertex
A vertex can we added simply by calling `graph.add_vertex`. The function takes in the value of the vertex. 
Additional `Attributes` of the vertex can be passed in as a dictionary. 
```python
from structlinks import Graph

graph = Graph()

# Adding a vertex
graph.add_vertex(2)

# Add vertex with attributes 
graph.add_vertex(3, attributes={'type': int, 'is active': True})
```

A error would **not** be raised if a vertex value is added again, instead the attributes 
of the vertex would be updated by the attributes of the new call. 

### Adding Multiple Vertices
Multiple vertices could be added using the `graph.add_vertices` function, which takes in a list of elements. To
add vertices with attributes the format of the tuple should be `[ ... (value, attribute dictionary) ... ]`. A list
contain both elements with no attributes and elements with attributes. 

```python
from structlinks import Graph

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

## Adding Edges

### Adding a Single Edge
An edge can be added using the `add_edge` function. Similar to vertices, edges can have attributes which we can pass in as 
an attribute. Note that if a vertex does not exists then the function does **not** raise an error, instead it creates
a new vertex with that value, and adds an edge. Note That if an edge already exists, then similar to vertices, the `attributes`
of the edge would be update if `add_edge` is called.

```python
from structlinks import Graph

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

### Adding multiple Edges
Multiple edges can be added using `add_edges` function. The function takes in a list of tuples, where each tuple represents 
an edge. The format of the tuple could `[... (item1, item2) ...]` , and we can additionally add attributes to the edge 
which would look like `[... (item1, item2, attributes dict) ...]`. Note that similar to `add edge`,  if a vertex does not exists then the function does **not** raise an error, instead it creates
a new vertex with that value, and adds an edge. 

```python
from structlinks import Graph

graph = Graph()

# Add vertices
graph.add_vertices([2, 1, 3, 5])

# Add edges
graph.add_edges([(2, 1), (1, 3, {'weight': 100}), (5, 25)])

print(graph.edges)
# Output:
# {(2, 1), (1, 3), (5, 25)}
```

## Clear the Graph
A graph can be cleared using the `clear` function. This would remove all the vertices and edges of the graph.
```python
graph.clear()
```

## Examining elements of a graph

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

## Path Finding
All the algorithms for finding the shortest path are located in the [`searching_algorithms` module](https://eeshannarula29.github.io/structlinks/searching),
however one can find all the paths from a vertex to another vertex with `get_all_paths_to` function. 
```python
from structlinks import Graph

graph = Graph()

graph.add_edges([(1, 2), (2, 3), (4, 5), (5, 6), (6, 1), (1, 3)])

paths = g[2].get_all_paths_to(3)  # <--- Get all the paths between 2 and 3

print(paths)
# Output: {(2, 3), (2, 1, 3)}
```

## Remove Vertices and Edges

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

## Get/Set the Attributes

```python
from structlinks import Graph

graph = Graph()

# Add vertices
graph.add_vertices([1, (2, {'type': int}), 3, ('string', {'type': str})])

# Add edges 
graph.add_edges([(1, 3, {'weight': 10}), (2, 1)])
```

### Vertex Attributes
```python
print(graph[2].attr)
# Output: {'type': int}

print(graph['string'].attr['type'])
# Output: str

graph[1].attr.update({'type': int})  # Same as graph[1].attr['type'] = int
```

### Edge Attributes
```python
print(graph[3][1])  # Represents an edge between 1 and 3 
# Output: {'weight': 10}

print(graph[1][2]) # Represents an edge between 1 and 2
# Output: {}

print(graph[1][3]['weight'])  # Return the weight attribute of the edge
# Output: 10

graph[1][2]['type'] = 'numbers'  # Same as graph[1][2].update({'type': 'numbers'})
```

### Add Global Attributes to All the Vertices of the Graph
```python
graph.add_global_attributes({'weight': 1})  # add this attribute to all the vertices
```

## Graph Generator Functions
```python
from structlinks import Graph

graph = Graph()

# Add vertices
graph.add_vertices([1, (2, {'type': int}), 3, ('string', {'type': str})])

# Add edges 
graph.add_edges([(1, 3, {'weight': 10}), ('string', 1, {'weight': 1})])
```
### Sub-Graph: Filter by Vertex Values
```python
filtered = graph.sub_graph_by_value(lambda x: isinstance(x, int))  # <-- only keep int vertices

print(filtered.vertices)
# Output: {1, 2, 3}

print(filtered.edges)
# Output: {(1, 3)}
```

### Sub-Graph: Filter by Attribute Values
```python
filtered = graph.sub_graph_by_attribute(attribute='type')  # only keep vertices with attribute 'type'

print(filtered.vertices)
# Output: {2}

print(filtered.edges)
# Output: {}
```

### Union

```python
other_graph = Graph()

other_graph.add_edges([(1, 7), (9, 0), (3, 10)])

union = graph.union(other_graph)

print(union.vertices)
# Output: {1, 2, 3, 'string', 7, 9, 0, 10}

print(union.edges)
# Output: {(1, 3), (1, 'string'), (1, 7), (9, 0), (3, 10)}
```

## Printing Graphs
```python
from structlinks import Graph

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
