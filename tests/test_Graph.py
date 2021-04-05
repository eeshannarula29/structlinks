"""The file contains tests for graph library"""

from Graph import Graph


class TestGraph:

    def test_add_vertex(self) -> None:
        """test add_vertex function"""
        graph = Graph()

        graph.add_vertex(1)
        graph.add_vertex('string')
        graph.add_vertex(2, {'type': 'number'})
        graph.add_vertex('string2', {'type': 'string', 'attribute2': 'value'})
        graph.add_vertex(1, {'weight': 100})

        assert graph.vertices == {1, 'string', 2, 'string2'}

        assert graph[1].attr == {'weight': 100}
        assert graph['string'].attr == {}
        assert graph[2].attr == {'type': 'number'}

        assert graph.vertices_count == 4

    def test_add_vertices(self) -> None:
        """test add_vertices function"""

        graph = Graph()

        graph.add_vertex(1)
        graph.add_vertex(2)

        graph.add_vertices([1, 2, (3, {'type': int}), ('string', {'type': str, 'value': 'David'})])

        assert graph.vertices == {1, 2, 3, 'string'}

        assert graph[1].attr == {}
        assert graph['string'].attr == {'type': str, 'value': 'David'}
        assert graph[3].attr == {'type': int}

        assert graph.vertices_count == 4

    def test_add_edge(self) -> None:
        """test add_edge function"""
        graph = Graph()

        graph.add_vertices([1, 2, 3, 4, 5])

        graph.add_edge(1, 2)

        graph.add_edge(5, 3, {'weight': 100})

        graph.add_edge(100, 2)

        assert graph.vertices == {1, 2, 3, 4, 5, 100}

        assert graph[1].adjacent(2)
        assert graph[5].adjacent(3)
        assert graph[100].adjacent(2)

        assert graph.edges_count == 3

        assert graph[2].degree == 2
        assert graph[5].degree == 1
        assert graph[4].degree == 0

        assert graph[5][3] == {'weight': 100}
        assert graph[3][1] == {}
        assert graph[1][2] == {}

    def test_add_edges(self) -> None:
        """test add_edge function"""
        graph = Graph()

        graph.add_vertices([1, 2, 3, 4, 5])

        graph.add_edge(1, 2)

        graph.add_edges([(5, 3, {'weight': 100}), (100, 2), (1, 2, {'type': int})])

        assert graph.vertices == {1, 2, 3, 4, 5, 100}

        assert graph[1].adjacent(2)
        assert graph[5].adjacent(3)
        assert graph[100].adjacent(2)

        assert graph.edges_count == 3

        assert graph[2].degree == 2
        assert graph[5].degree == 1
        assert graph[4].degree == 0

        assert graph[5][3] == {'weight': 100}
        assert graph[3][1] == {}
        assert graph[1][2] == {'type': int}
