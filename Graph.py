"""The file contains Graph object. The base code for the vertex and the graph object
is taken from University of Toronto's CSC111 course."""

from __future__ import annotations
from typing import Any, Optional, Union


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

    def add_vertices(self, items: list[Any]):
        """Add multiple vertices

        An items can look like:
        - [item 1, item 2, ..., item n]
        - [(item 1, attribute 1), (item 2, attribute 2), ..., (item n, attribute n)]
        - [(item 1, attribute 1), item2, item3, ..., (item n, attribute n)]
        """

        for item in items:

            if isinstance(item, tuple) and len(item) == 2:
                item_value, item_attributes = item
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

            # Add the new edge
            v1.neighbours[item2] = {'item': v2, 'attributes': attributes if attributes else {}}
            v2.neighbours[item1] = {'item': v1, 'attributes': attributes if attributes else {}}

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

    def get_degree(self, item: Any) -> int:
        """Return the degree of the item in the graph

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return len(v.neighbours)
        else:
            raise ValueError
