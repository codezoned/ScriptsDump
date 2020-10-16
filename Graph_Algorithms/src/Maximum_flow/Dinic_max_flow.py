"""
Code by BH4

This file includes:
  - Flow graph data structure
  - Dinic's algorithm for max flow
"""


class Vertex():
    def __init__(self, node):
        """
        adjacent has keys of other vertices with values being the weight of
        the edge.
        """

        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, capacity=0, flow=0):
        self.adjacent[neighbor] = (flow, capacity)

    def get_residual(self, node_B):
        edge = self.adjacent[node_B]
        return edge[1] - edge[0]

    def get_flow(self, node_B):
        if node_B not in self.adjacent:
            return 0

        edge = self.adjacent[node_B]
        return edge[0]

    def set_flow(self, node_B, flow):
        edge = self.adjacent[node_B]
        self.adjacent[node_B] = (flow, edge[1])

    def get_capacity(self, node_B):
        edge = self.adjacent[node_B]
        return edge[1]

    def set_capacity(self, node_B, capacity):
        edge = self.adjacent[node_B]
        self.adjacent[node_B] = (edge[0], capacity)

    def get_neighbors(self):
        return self.adjacent.keys()


class Graph():
    def __init__(self):
        self.graph_dict = {}
        self.source = None
        self.sink = None

    def add_vertex(self, node):
        self.graph_dict[node] = Vertex(node)

    def add_edge(self, start, end, capacity=0):
        if start not in self.graph_dict:
            self.add_vertex(start)
        if end not in self.graph_dict:
            self.add_vertex(end)

        self.graph_dict[start].add_neighbor(end, capacity=capacity)

    def create_directed_graph(self, sources, sinks, capacities):
        """
        We will replace all the sources with a single source and all the sinks
        with a single sink to simplify the problem.

        The source will be labeled -1 and the sink will be labeled -2 to avoid
        collisions with names of other nodes.

        Capacities should be given as a matrix. Each element capacities[A][B]
        is the capacity available for the edge from A to B
        """

        for A in range(len(capacities)):
            node_A = A
            if A in sources:
                node_A = -1
            elif A in sinks:
                node_A = -2
            for B in range(len(capacities)):
                node_B = B
                if B in sources:
                    node_B = -1
                elif B in sinks:
                    node_B = -2

                # There is no reason to send bunnies to the same room.
                if capacities[A][B] > 0 and node_A != node_B:
                    if node_A in self.graph_dict and node_B in self.graph_dict[node_A].get_neighbors():
                        tot_cap = self.graph_dict[node_A].get_capacity(node_B)+capacities[A][B]
                        self.graph_dict[node_A].set_capacity(node_B, tot_cap)
                    else:
                        self.add_edge(node_A, node_B, capacity=capacities[A][B])

        self.source = -1
        self.sink = -2

    def residual_graph(self):
        G_f = Graph()

        for node_A in self.graph_dict:
            for node_B in self.graph_dict[node_A].get_neighbors():
                c_f_AB = self.graph_dict[node_A].get_residual(node_B)
                c_f_BA = self.graph_dict[node_A].get_flow(node_B)

                if c_f_AB > 0:
                    G_f.add_edge(node_A, node_B, capacity=c_f_AB)

                if c_f_BA > 0:
                    G_f.add_edge(node_B, node_A, capacity=c_f_BA)

        if self.source in G_f.graph_dict:
            G_f.source = self.source
        if self.sink in G_f.graph_dict:
            G_f.sink = self.sink
        return G_f

    def level_graph(self):
        """
        Use a bfs to define a level graph from the current graph.
        """

        G_L = Graph()

        # used_verts is a dictionary of the distances of each node from the source
        used_verts = dict()

        queue = [(self.source, 0)]
        used_verts[self.source] = 0
        sink_distance = None
        while len(queue) > 0:
            curr, dist = queue.pop(0)

            if sink_distance is None or dist < sink_distance:
                # Don't add any vertices which are as far or farther from
                # the source as the sink. Since they won't reach the sink.

                for neighbor in self.graph_dict[curr].get_neighbors():
                    c = self.graph_dict[curr].get_capacity(neighbor)

                    if neighbor not in used_verts:
                        queue.append((neighbor, dist+1))
                        used_verts[neighbor] = dist+1

                        G_L.add_edge(curr, neighbor, capacity=c)

                        if neighbor is self.sink:
                            sink_distance = dist+1
                    else:
                        if used_verts[neighbor] == dist+1:
                            G_L.add_edge(curr, neighbor, capacity=c)

        if self.source in G_L.graph_dict:
            G_L.source = self.source
        if self.sink in G_L.graph_dict:
            G_L.sink = self.sink
        return G_L, sink_distance

    def send_flow(self, node, n=None):
        if node == self.source:
            # Needs to be a number larger than the maximum possible flow
            n = 200000000000

        if node == self.sink:
            return n

        tot_new_flow = 0
        for neighbor in self.graph_dict[node].get_neighbors():
            if n > 0:
                to_send = self.graph_dict[node].get_residual(neighbor)
                if to_send > n:
                    to_send = n
                actual_used = self.send_flow(neighbor, n=to_send)

                already_sent = self.graph_dict[node].get_flow(neighbor)
                self.graph_dict[node].set_flow(neighbor, actual_used+already_sent)
                new_flow = actual_used
                n -= new_flow
                tot_new_flow += new_flow

        return tot_new_flow

    def blocking_flow(self):
        self.send_flow(self.source)

    def add_flow(self, other):
        """
        Given a second graph, for any edge from A to B in self add the flow of
        the same edge from other.
        """
        for node_A in self.graph_dict:
            for node_B in self.graph_dict[node_A].get_neighbors():
                f_self = self.graph_dict[node_A].get_flow(node_B)
                f_other = 0
                f_other_reverse = 0
                if node_A in other.graph_dict:
                    f_other = other.graph_dict[node_A].get_flow(node_B)
                if node_B in other.graph_dict:
                    f_other_reverse = other.graph_dict[node_B].get_flow(node_A)

                self.graph_dict[node_A].set_flow(node_B, f_self+f_other-f_other_reverse)

    def sum_flow(self, node_A):
        """
        Return total flow leaving node_A
        """

        tot = 0
        for node_B in self.graph_dict[node_A].get_neighbors():
            tot += self.graph_dict[node_A].get_flow(node_B)

        return tot


def max_flow(G):
    """
    Implementation of Dinic's algorithm for calculating maximum flow.
    """

    G_f = G.residual_graph()
    G_L, sink_distance = G_f.level_graph()

    # The algorithm repeats until the level
    while sink_distance is not None:
        G_L.blocking_flow()
        G.add_flow(G_L)

        G_f = G.residual_graph()
        G_L, sink_distance = G_f.level_graph()

    return G.sum_flow(G.source)


if __name__ == '__main__':
    """
    Defined here is a graph whose maximum flow is 19.

    Example from https://en.wikipedia.org/wiki/Dinic%27s_algorithm#Algorithm
    """
    source = [0]
    sink = [5]
    capacities = [[0, 10, 10, 0, 0,  0],
                  [0,  0,  2, 4, 8,  0],
                  [0,  0,  0, 0, 9,  0],
                  [0,  0,  0, 0, 0, 10],
                  [0,  0,  0, 6, 0, 10],
                  [0,  0,  0, 0, 0,  0]]

    G = Graph()
    G.create_directed_graph(source, sink, capacities)
    print('Maximum flow through graph is {}'.format(max_flow(G)))
