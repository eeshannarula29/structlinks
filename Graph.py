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

        The base code is taken from University of Toronto's CSC111 course
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

    def get_connected(self, visited: set[_Vertex]) -> set:
        """Return a set of all ITEMS connected to self by a path that does not use
        any vertices in visited.

        The items of the vertices in visited CANNOT appear in the returned set.

        Preconditions:
            - self not in visited

        The base code is taken from University of Toronto's CSC111 course
        """

        all_in_visited = True

        items_set = {self.item}

        for neighbour in self.neighbours:

            neighbour_vertex = self.neighbours[neighbour]['item']

            if neighbour_vertex not in visited:
                all_in_visited = False

        if all_in_visited:
            visited.add(self)
            return items_set

        else:
            visited.add(self)

            for neighbour in self.neighbours:

                neighbour_vertex = self.neighbours[neighbour]['item']

                if neighbour_vertex not in visited:
                    items_set = items_set.union(neighbour_vertex.get_connected(visited))

            return items_set

    def spanning_graph(self, visited: set[_Vertex]) -> list[tuple]:
        """Return a Graph that form a spanning tree of all vertices that are
        connected to this vertex WITHOUT using any of the vertices in visited.

        The edges are returned as a list of sets, where each set contains the two
        ITEMS corresponding to an edge.

        Preconditions:
            - self not in visited

        The base code is taken from University of Toronto's CSC111 course
        """
        edges_so_far = []

        visited.add(self)

        for neighbour in self.neighbours:
            # Only recurse on vertices that haven't been visited
            if self.neighbours[neighbour]['item'] not in visited:
                edges_so_far.append((self.item, neighbour,
                                     self.neighbours[neighbour]['attributes']))
                edges_so_far.extend(self.neighbours[neighbour]['item'].spanning_graph(visited))

        return edges_so_far

    def paths_to(self, item: Any, visited: set, current_path: list, paths: set) -> None:
        """Return a set of all the paths between self and item"""

        visited.add(self.item)
        current_path.append(self.item)

        if self.item == item:
            paths.add(tuple(current_path))

        else:
            for neighbour in self.neighbours:
                if neighbour not in visited:
                    self.neighbours[neighbour]['item'].paths_to(item, visited, current_path, paths)

        current_path.pop()
        visited.remove(self.item)

    def update_attributes(self, other) -> None:
        """update the attributes of the edge"""
        if other in self.neighbours:

            other_vertex = self.neighbours[other]['item']

            attributes = other_vertex.neighbours[self.item]['attributes']

            self.neighbours[other]['attributes'].update(attributes)


class _VertexView:
    """Used to get/view a vertex"""

    def __init__(self, _vertex: _Vertex) -> None:
        self._vertex = _vertex

    def __repr__(self) -> str:
        """Return string representation of vertex"""

        string_so_far = 'NeighboursView({ \n'

        for neighbour in self._vertex.neighbours:
            string_so_far += \
                '  {' + f'{neighbour}: {self._vertex.neighbours[neighbour]["attributes"]}' + '}, \n'

        return string_so_far + '})'

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

        other_vertex = self._vertex.neighbours[other]['item']

        self._vertex.update_attributes(other)
        other_vertex.update_attributes(self._vertex.item)

        return self._vertex.neighbours[other]['attributes']

    @property
    def attr(self) -> dict:
        """Return the attribute dict of the vertex"""
        return self._vertex.attributes

    def check_connected(self, item: Any) -> bool:
        """Check if vertex is connected to the item"""
        return self._vertex.check_connected(item, set())

    def get_connected(self) -> set:
        """Return set of all elements connected to vertex"""
        return self._vertex.get_connected(set())

    def in_cycle(self) -> bool:
        """Return whether vertex is in a cycle or not

        The base code is taken from University of Toronto's CSC111 course
        """

        return any(self._vertex.neighbours[neighbour1]['item'].check_connected(neighbour2,
                                                                               {self._vertex})
                   for neighbour1 in self._vertex.neighbours
                   for neighbour2 in self._vertex.neighbours
                   if neighbour1 != neighbour2)

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

    def create_spanning_graph(self) -> Graph:
        """Create a spanning graph from this vertex"""
        graph = Graph()
        edges = self._vertex.spanning_graph(set())
        graph.add_edges(edges)
        return graph

    def get_all_paths_to(self, item: Any) -> set:
        """Return all the paths to the item from self"""
        paths = set()
        self._vertex.paths_to(item, set(), [], paths)
        return paths


class Graph:
    """A graph.

    The base code for this class taken from University of Toronto's CSC111 course
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

        The base code is taken from University of Toronto's CSC111 course
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

        The base code is taken from University of Toronto's CSC111 course
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

        The base code is taken from University of Toronto's CSC111 course
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

        The base code is taken from University of Toronto's CSC111 course
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

        The base code is taken from University of Toronto's CSC111 course
        """
        if item1 in self._vertices and item2 in self._vertices:
            return item2 in self._vertices[item1].neighbours
        else:
            # We didn't find an existing vertex for both items.
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Raise a ValueError if item does not appear as a vertex in this graph.

        The base code is taken from University of Toronto's CSC111 course
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

    @property
    def is_connected(self) -> bool:
        return all(self[item1].check_connected(item2)
                   for item1 in self.vertices for item2 in self.vertices)

    def create_spanning_graph(self) -> Graph:
        """Return a spanning graph of self

        Precondition:
        - self.is_connected

        The base code is taken from University of Toronto's CSC111 course
        """
        if not self.is_connected:
            raise TypeError('The graph should be connected')

        if self.vertices_count > 0:
            return self[list(self.vertices)[0]].create_spanning_graph()

        else:
            return Graph()

    def __str__(self) -> str:
        """Return a string representation of the graph"""
        string_representation = '{ \n'

        for item in self.vertices:
            string_representation += f'{item}: {self[item].get_neighbours()} \n'

        string_representation += '}'

        return string_representation

    def __repr__(self) -> str:
        """Return a string representation of the graph"""
        string_representation = '{ \n'

        for item in self.vertices:
            string_representation += f'{item}: {self[item].get_neighbours()} \n'

        string_representation += '}'

        return 'Graph(' + string_representation + ')'
