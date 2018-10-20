from collections import namedtuple
from operator import attrgetter
from functools import reduce


'''
    Implementation of Kruskal algorithm: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    Time complexity: O(Elog(E))
    Space complexity: O(V + E)
    Throws: ValueError, if the Graph is not connected
'''
class Kruskal:

    Edge = namedtuple('Edge', ['start', 'end', 'cost'])

    def __init__(self, nodes, edges=[]):
        '''
            param: nodes: Number of nodes in the Graph
            param: edges: Init edges for the graph (empty as default)
        '''
        self.edges = []
        self.nodes = nodes
        self.parent = [i for i in range(nodes + 1)]
        for edge in edges:
            start, end, cost = edge
            self.edges.append(self.Edge(start, end, cost))
    
    def add_edge(self, edge):
        start, end, cost = edge
        self.edges.append(self.Edge(start, end, cost))
    
    def findparent(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        node1 = self.findparent(node1)
        node2 = self.findparent(node2)
        if node1 != node2:
            self.parent[node1] = self.parent[node2]
            return True
        return False
    
    def getMST(self):
        '''
            returns: mst: List of edges in one of the possible Minimum Spanning Trees
            returns: cost: Cost of the Minimum Spanning Tree(MST)
        '''
        mst = []
        visited = [False for i in range(self.nodes + 1)]
        visited[0] = True  #Because node doesn't exist
        cost = 0
        self.edges = sorted(self.edges, key=attrgetter('cost'))
        for edge in self.edges:
            if self.union(edge.start, edge.end):
                mst.append(edge)
                cost += edge.cost
                visited[edge.start] = visited[edge.end] = True
        connected = reduce(lambda x, y: x&y, visited)
        if connected == False:
            raise(ValueError('Graph is not connected.'))
        return mst, cost
        
    def printGraph(self):
        print(self.edges)

