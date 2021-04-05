"""The file contains Graph object. The base code for the vertex and the graph object
is taken from University of Toronto's CSC111 course."""

from __future__ import annotations
from typing import Any, Optional, Union, Callable


class _Vertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - attributes: attributes of the vertex
        - neighbours: The vertices that are adjacent to this vertex.
    """
    item: Any
    attributes: dict
    neighbours: dict

    def __init__(self, item: Any,
                 neighbours: Optional[dict] = None,
                 attributes: Optional[dict] = None) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.attributes = attributes if attributes else {}
        self.neighbours = neighbours if neighbours else {}
        self.view = _VertexView(self)

    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            # Our base case: the target_item is the current vertex
            return True
        else:
            visited.add(self)  # Add self to the set of visited vertices
            for u in self.neighbours:
                u_vertex = self.neighbours[u]['item']
                if u_vertex not in visited:  # Only recurse on vertices that haven't been visited
                    if u_vertex.check_connected(target_item, visited):
                        return True

            return False


class _VertexView:
    """Used to get/view a vertex"""

    def __init__(self, _vertex: _Vertex) -> None:
        self._vertex = _vertex

    def __repr__(self) -> str:
        """Return string representation of vertex"""

        string_so_far = '{ \n'

        for neighbour in self._vertex.neighbours:
            string_so_far += \
                '  {' + f'{neighbour}: {self._vertex.neighbours[neighbour]["attributes"]}' + '}, \n'

        return string_so_far + '}'

    def __setitem__(self, other: Any, properties: dict) -> None:
        """Set a property of the edge between self and other

        properties is of the form:
        - {'property 1': value 1, 'property 2': value 2, ... 'property n': value n}
        """
        if other not in self._vertex.neighbours:
            raise ValueError('The vertex value is not a neighbour to self, or does not exists')

        if not isinstance(properties, dict):
            raise TypeError('attribute properties should be a dictionary')

        self._vertex.neighbours[other]['attributes'] = properties

    def __getitem__(self, other: Any) -> dict:
        """Return all the attributes of edge between self and other"""
        if other not in self._vertex.neighbours:
            return {}

        return self._vertex.neighbours[other]['attributes']

    @property
    def attr(self) -> dict:
        """Return the attribute dict of the vertex"""
        return self._vertex.attributes

    def check_connected(self, item: Any) -> bool:
        """Check if vertex is connected to the item"""
        return self._vertex.check_connected(item, set())

    def adjacent(self, item: Any) -> bool:
        """Return whether item is adjacent to self.
        """
        return item in self._vertex.neighbours

    def get_neighbours(self) -> set:
        """Return a set of the neighbours of vertex
        """
        return set(self._vertex.neighbours.keys())

    @property
    def degree(self) -> int:
        """Return the degree of the vertex"""
        return len(self._vertex.neighbours)


class Graph:
    """A graph.
    """
    # Private Instance Attributes:
    #     - _vertices: A collection of the vertices contained in this graph.
    #                  Maps item to _Vertex instance.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any, attributes: Optional[dict] = None) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, attributes=attributes if attributes else {})
        else:
            self._vertices[item].attributes.update(attributes if attributes else {})

    def add_vertices(self, items: list[Any], global_attributes: Optional[dict] = None):
        """Add multiple vertices

        An items can look like:
        - [item 1, item 2, ..., item n]
        - [(item 1, attribute 1), (item 2, attribute 2), ..., (item n, attribute n)]
        - [(item 1, attribute 1), item2, item3, ..., (item n, attribute n)]

        global_attributes will be added to all the vertices
        """
        if not global_attributes:
            global_attributes = {}

        for item in items:

            if isinstance(item, tuple) and len(item) == 2:
                item_value, item_attributes = item
                item_attributes.update(global_attributes)
                self.add_vertex(item_value, attributes=item_attributes)
            else:
                self.add_vertex(item)

    @property
    def vertices(self) -> set:
        """Return set of all the vertices in the graph"""
        return set(self._vertices.keys())

    def add_edge(self, item1: Any, item2: Any, attributes: Optional[dict] = None) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        and with the give attributes. attributes here is the list of properties if
        the edge between the two items.
        """
        # check if item1 != item2
        if item1 != item2:
            # if item1 is not in self._vertices then add it
            if item1 not in self._vertices:
                self.add_vertex(item1)
            # if item2 is not in self._vertices then add it
            if item2 not in self._vertices:
                self.add_vertex(item2)
            # extract the _Vertex object of item1 and item2
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            if item1 not in v2.neighbours and item2 not in v1.neighbours:
                # Add the new edge
                v1.neighbours[item2] = {'item': v2, 'attributes': attributes if attributes else {}}
                v2.neighbours[item1] = {'item': v1, 'attributes': attributes if attributes else {}}
            else:
                v1.neighbours[item2]['attributes'].update(attributes if attributes else {})
                v2.neighbours[item1]['attributes'].update(attributes if attributes else {})

    def add_edges(self, edges: Union[list[tuple[Any, Any]], list[tuple[Any, Any, dict]]]) -> None:
        """Add multiple edges to the graph

        Instance Attributes:
        - edges: it is a list of tuples representing an edge. The tuple could be of length 2 or 3

                if edge is of length 2 then it would look like:
                - (item1, item2)

                if edge is of length 2 then it would look like:
                - (item1, item2, edge-attributes)
        """
        for edge in edges:
            if not (len(edge) == 2 or len(edge) == 3):
                raise TypeError('The edges are not formatted properly')

        for edge in edges:

            if len(edge) == 2:
                self.add_edge(edge[0], edge[1])

            else:
                self.add_edge(edge[0], edge[1], edge[2])

    @property
    def edges(self) -> set:
        """Return set of all the edges"""

        # Set of all the edges
        set_so_far = set()
        # set of all the elements which have been visited
        visited = set()

        for vertex in self._vertices:
            # add vertex to visited
            visited.add(vertex)

            for neighbour in self._vertices[vertex].neighbours:
                # only add edge if not previously added
                if neighbour not in visited:
                    set_so_far.add((vertex, neighbour))

        return set_so_far

    def clear(self) -> None:
        """clear the graph"""
        for vertex in self.vertices:
            del self._vertices[vertex]
        self._vertices = {}

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            return item2 in self._vertices[item1].neighbours
        else:
            # We didn't find an existing vertex for both items.
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return set(v.neighbours.keys())
        else:
            raise ValueError

    @property
    def vertices_count(self) -> int:
        """Return the number of vertices"""
        return len(self._vertices)

    @property
    def edges_count(self) -> int:
        """Return the number of edges"""
        return len(self.edges)

    def get_degree(self, item: Union[set, Any]) -> Union[dict, int]:
        """Return the degree of the item in the graph if item is a single element
        otherwise if item is a set of elements then it would return a dict of
        elements mapped to their degrees

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        # If item is a set of elements
        if isinstance(item, set):
            dict_so_far = {}

            for element in item:
                dict_so_far[element] = self.get_degree(element)

            return dict_so_far
        # if item is a single element
        if item in self._vertices:
            return self[item].degree
        else:
            raise ValueError('The element or one of the elements is not on the graph')

    def __getitem__(self, item) -> _VertexView:
        """Returns a object containing all the information about the neighbours of vertex,
        and used to set/get properties of edges
        """
        if item not in self._vertices:
            raise ValueError

        return self._vertices[item].view

    def remove_vertex(self, item: Any) -> None:
        """Delete item from the graph"""
        if item in self._vertices:

            for neighbour in self._vertices[item].neighbours:
                self._vertices[neighbour].neighbours.pop(item)

            self._vertices.pop(item)

        else:
            raise ValueError('The item is not in the graph')

    def remove_edge(self, item1: Any, item2: Any) -> None:
        """Remove edge between item1 and item2"""
        if item1 in self._vertices and item2 in self._vertices:
            if item1 in self.get_neighbours(item2):
                self._vertices[item1].neighbours.pop(item2)
                self._vertices[item2].neighbours.pop(item1)
        else:
            raise ValueError('One/both of item1, item2 is/are not in the graph')

    def remove_vertices(self, items: list) -> None:
        """Remove all the vertices in items"""
        if not all(item in self._vertices for item in items):
            raise ValueError('One or more items in the list are not present in the graph')

        else:
            for item in items:
                self.remove_vertex(item)

    def remove_edges(self, edges: list[tuple]) -> None:
        """Remove all the edge pairs in <edges>"""
        if not all(item1 in self._vertices and item2 in self._vertices
                   for (item1, item2) in edges):
            raise ValueError('One or more of the edge pairs have elements which are not in graph')

        for (item1, item2) in edges:
            self.remove_edge(item1, item2)

    def add_global_attributes(self, attributes: dict) -> None:
        """Add attributes to all the vertices in the graph"""
        for item in self.vertices:
            self[item].attr.update(attributes)

    def sub_graph_by_value(self, predicate: Callable) -> Graph:
        """Return a sub-graph of self, with vertices which pass the predicate function"""
        subgraph = Graph()

        subgraph.add_vertices([(item, self[item].attr)
                               for item in self.vertices if predicate(item)])

        vertices = subgraph.vertices

        for (item1, item2) in self.edges:
            if item1 in vertices and item2 in vertices:
                subgraph.add_edge(item1, item2, self[item1][item2].copy())

        return subgraph

    def sub_graph_by_attribute(self, attribute: Any,
                               predicate: Optional[Callable] = lambda x: True) -> Graph:
        """Return a sub-graph of self, with vertices which contain attribute and
         pass the predicate function for that attribute"""

        subgraph = Graph()

        subgraph.add_vertices([(item, self[item].attr)
                               for item in self.vertices
                               if attribute in self[item].attr and predicate(item)])

        vertices = subgraph.vertices

        for (item1, item2) in self.edges:
            if item1 in vertices and item2 in vertices:
                subgraph.add_edge(item1, item2, self[item1][item2].copy())

        return subgraph

    def union(self, other: Graph) -> Graph:
        """Return a new graph which contains all the vertices of self and other. Attributes
        for duplicates would be combined to also form a union."""

        graph = Graph()

        graph.add_vertices([(item, self[item].attr) for item in self.vertices])
        graph.add_vertices([(item, other[item].attr) for item in other.vertices])

        graph.add_edges([(item1, item2, self[item1][item2].copy())
                         for (item1, item2) in self.edges])

        graph.add_edges([(item1, item2, other[item1][item2].copy())
                         for (item1, item2) in other.edges])

        return graph
