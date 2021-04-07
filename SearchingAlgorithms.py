"""
A re-implementation of several searching algorithms, including:
    - Linear Search
    - Binary Search

Many of these sort are inspired by their implementations in the CSC111
University of Toronto Course.
"""

from typing import Any, Union, Optional

import math

from structlinks.Graph import Graph
from structlinks.Queue import Queue
from structlinks.Stack import Stack
from structlinks.LinkedList import LinkedList
from structlinks.DoublyLinkedList import DoublyLinkedList


def linear_search(lst: Union[list, LinkedList, DoublyLinkedList], item: Any) -> bool:
    """Return a boolean representing whether or not the given item
    exists in the list.
    """
    # Iterate through all items in the list
    for i in lst:
        if item == i:  # If the target item is found
            return True

    # If we reach this point, the item is not in the list
    return False


def binary_search(lst: Union[list, LinkedList, DoublyLinkedList], item: Any) -> bool:
    """Return a boolean representing whether or not the given item
    exists in the list.

    Preconditions:
        - lst must be sorted
    """
    # Initialize our upper and lower bounds of the search area
    b = 0
    e = len(lst)

    # We will have verified the entire list when b >= e
    while b < e:
        # Get the middle index
        m = (e + b) // 2

        # Check if the middle item is the target
        if lst[m] == item:
            return True
        elif lst[m] > item:
            e = m
        else:
            b = m + 1

    # If we reach this point, the item is not in the list
    return False


def _edges_from_path(lst: list) -> list[tuple]:
    """Return a list of edges form the given path"""
    edges = []

    for index in range(len(lst) - 1):
        edges.append((lst[index], lst[index + 1]))

    return edges


def breadth_first_search(g: Graph, origin: Any, target: Any) -> Optional[list]:
    """Search for the smallest path between two nodes of a graph using Queues

    source: https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/
    """
    if origin in g.vertices:
        path = [origin]
        queue = Queue()
        queue.enqueue(path)

        while queue:

            path = queue.dequeue()
            last = path[len(path) - 1]

            if last == target:
                return _edges_from_path(path)

            for neighbour in g[last].get_neighbours():
                if neighbour not in path:
                    new_path = path.copy()
                    new_path.append(neighbour)
                    queue.enqueue(new_path)

        return None
    else:
        return None


def depth_first_search(g: Graph, origin: Any, target: Any) -> Optional[list]:
    """Search for the shortest path between two nodes of a graph using Stacks
    """
    if origin in g.vertices:
        path = [origin]
        stack = Stack()
        stack.push(path)

        while stack:

            path = stack.pop()
            last = path[len(path) - 1]

            if last == target:
                return _edges_from_path(path)

            for neighbour in g[last].get_neighbours():
                if neighbour not in path:
                    new_path = path.copy()
                    new_path.append(neighbour)
                    stack.push(new_path)

        return None
    else:
        return None


def dijkstra_search_target(g: Graph, origin: Any, target: Any, metric: Any) -> Optional[list]:
    """Use Dijkstra Algorithm to find the shortest path for a weighted graph from one point to
    another

    sources:
    - https://www.techiedelight.com/single-source-shortest-paths-dijkstras-algorithm/

    - https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/#:~
    :text=Dijkstra's%20Algorithm%20finds%20the%20shortest,node%20and%20all%20other%20nodes.

    - https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
    """

    path = []  # list of all the visited vertices
    prev = {item: None for item in g.vertices}  # parent-child search dict

    dist = 'distance'  # distance attribute for a vertices

    # set distance attribute for all vertices to be infinity
    g.add_global_attributes({dist: math.inf})
    # setting distance attribute 0 for the origin vertex
    g[origin].attr[dist] = 0

    # creating a function by which the queue would prioritize
    def queue_metric(value: Any) -> Any:
        """Return the metric of the vertex with value <value>"""
        return - g[value].attr[dist]

    # creating a priority queue with -distance as the metric
    queue = Queue(list(g.vertices), queue_metric)

    while not queue.is_empty:  # while the queue still have vertices un-explored
        item = queue.dequeue()  # taking out the vertex with the shortest distance
        path.append(item)  # add the item to visited

        if item == target:  # Base case : if we reached the item
            try:
                return _edges_from_path(_path_from_dict(prev, origin, target))
            except KeyError:
                return None

        for neighbour in g[item].get_neighbours():
            # if neighbour is in the queue, that us when the distance of neighbour is infinity
            if g[neighbour].attr[dist] > g[item].attr[dist] + g[item][neighbour][metric]:
                #  set the new distance
                g[neighbour].attr[dist] = g[item].attr[dist] + g[item][neighbour][metric]
                #  mark the parent item
                prev[neighbour] = item

        #  update the order of the queue
        queue.update()

    # Return None if there is no path
    return None


def dijkstra_search_all(g: Graph, origin: Any, metric: Any) -> dict:
    """Use Dijkstra Algorithm to find the shortest path for a weighted graph from one point to
    all the the other points

    sources:
    - https://www.techiedelight.com/single-source-shortest-paths-dijkstras-algorithm/

    - https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/#:~
    :text=Dijkstra's%20Algorithm%20finds%20the%20shortest,node%20and%20all%20other%20nodes.

    - https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
    """

    path = []  # list of all the visited vertices
    prev = {item: None for item in g.vertices}  # parent-child search dict

    dist = 'distance'  # distance attribute for a vertices

    # set distance attribute for all vertices to be infinity
    g.add_global_attributes({dist: math.inf})
    # setting distance attribute 0 for the origin vertex
    g[origin].attr[dist] = 0

    # creating a function by which the queue would prioritize
    def queue_metric(value: Any) -> Any:
        """Return the metric of the vertex with value <value>"""
        return - g[value].attr[dist]

    # creating a priority queue with -distance as the metric
    queue = Queue(list(g.vertices), queue_metric)

    while not queue.is_empty:  # while the queue still have vertices un-explored
        item = queue.dequeue()  # taking out the vertex with the shortest distance
        path.append(item)  # add the item to visited

        for neighbour in g[item].get_neighbours():
            # if neighbour is in the queue, that us when the distance of neighbour is infinity
            if g[neighbour].attr[dist] > g[item].attr[dist] + g[item][neighbour][metric]:
                #  set the new distance
                g[neighbour].attr[dist] = g[item].attr[dist] + g[item][neighbour][metric]
                #  mark the parent item
                prev[neighbour] = item

        #  update the order of the queue
        queue.update()

    paths_dict = {}

    for item in g.vertices:
        if item != origin:
            try:
                paths_dict[item] = _edges_from_path(_path_from_dict(prev, origin, item))
            except KeyError:
                paths_dict[item] = None

    return paths_dict


def _path_from_dict(d: dict, src: Any, target: Any) -> list:
    """Helper function for dijkstra_search"""
    current_key = target
    path = LinkedList([target])

    while current_key != src:

        path.insert(0, d[current_key])
        current_key = d[current_key]

    return path.to_list()
