"""
A re-implementation of several searching algorithms, including:
    - Linear Search
    - Binary Search

Many of these sort are inspired by their implementations in the CSC111
University of Toronto Course.
"""

from typing import Any, Union, Optional

from Graph import Graph
from Queue import Queue
from Stack import Stack
from LinkedList import LinkedList
from DoublyLinkedList import DoublyLinkedList


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


def BreadthFirstSearch(g: Graph, origin: Any, target: Any) -> Optional[list]:
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
        raise ValueError('the vertices do not exist in the graph')


def DepthFirstSearch(g: Graph, origin: Any, target: Any) -> Optional[list]:
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
        raise ValueError('the vertices do not exist in the graph')
