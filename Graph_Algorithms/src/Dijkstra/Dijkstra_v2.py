class Arch:
    initial_node = None
    arch_value = 0
    final_node = None

class Node:
    number = None
    archs = {}
    visited = False

class Graph:
    nodes = []

    def print_nodes(self):
        for node in self.nodes:
            print( str(node.number) )


def init():
    count = int(5)
    nodes = []

    for i in range(count):
        node = Node()
        node.number = (i + 1)
        nodes.append(node)

    graph = Graph()
    graph.nodes = nodes
    graph.print_nodes()

init()
