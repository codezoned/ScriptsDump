from collections import deque, namedtuple

# Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path 
# from one particular starting node (a in our case) to all other nodes in the graph.


"""
  To keep track of the total cost from the start node to each destination we will make use of the distance instance variable in the Vertex class. 
  The distance instance variable will contain the current total weight of the smallest weight path from the start to the vertex in question. 
  The algorithm iterates once for every vertex in the graph; 
  However, the order in which we iterate over the vertices is controlled by a double ended queue.

  The value that is used to determine the order of the objects in the priority queue is distance. 
  When a vertex is first created distance is set to a very large number.

  When the algorithm finishes the distances are set correctly as are the predecessor (previous in the code) links for each vertex in the graph.

"""

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

# Let's initialize our data:
class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]
        

#  Find the vertices. In the original implementation the vertices are defined in the _ _ init _ _, 
#  but we'll need them to update when edges change, so we'll make them a property, 
#  they'll be recounted each time we address the property. 
#  Probably not the best solution for big graphs, but for small ones it'll go.


    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )


# Implemented Basic Functionalities
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))


# Find Neighbours for every node.
    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours
        
        
  # Implementation of Dijkstra.
    # We set the initial node as the current_vertex        

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node 
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
          # 3. Select the unvisited node with the smallest distance, 
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            # 6. Stop, if the smallest distance 
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break
                
            # 4. Find unvisited neighbors for the current node 
            # and calculate their distances through the current node.
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                
                # Compare the newly calculated distance to the assigned 
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex
                    
            # 5. Mark the current node as visited 
            # and remove it from the unvisited set.

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

# Invoke the constructor by passing (node, node, distance) pairs in the object created 
# And then calling the dijkstra function.
graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])

print(graph.dijkstra("a", "e"))