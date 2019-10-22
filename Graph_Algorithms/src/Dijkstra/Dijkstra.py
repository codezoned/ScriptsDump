"""Dijkstra's algorithm."""

import math


class Vertex:

    def __init__(self, id):
        self.id = str(id)
        self.distance = 0
        self.neighbors = []
        self.edges = {}  # {vertex:distance}

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return self.distance < other.distance

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def add_neighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def add_edge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def dijkstra(graph, source, destiny):
    """Dijkstra's Algorithm."""
    q = []
    for v in graph:
        v.distance = math.inf
        q.append(v)
    source.distance = 0
    while q:
        v = min(q)
        q.remove(v)
        for u in v.neighbors:
            new = v.distance + v.edges[u.id]
            if new < u.distance:
                u.distance = new
    return destiny.distance
