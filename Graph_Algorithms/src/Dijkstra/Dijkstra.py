from collections import defaultdict
import math

class Graph:
  def __init__(self):
    self.nodes = set()
    self.archs = defaultdict(list)
    self.values = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, init_node, final_node, value):
    self.archs[init_node].append(final_node)
    self.archs[init_node].append(final_node)
    self.values[(init_node, final_node)] = value


def dijkstra(graph, initial):
  visited = {initial: 0}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for arch in graph.archs[min_node]:
      try:
          weight = current_weight + graph.values[(min_node, arch)]
      except:
          weight = current_weight + math.inf
      if arch not in visited or weight < visited[arch]:
        visited[arch] = weight

  return visited


def main():

    #initializing values
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    g.add_edge('a', 'b', 10)
    g.add_edge('b', 'c', 2)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'd', 1)
    g.add_edge('b', 'd', 8)

    #output
    print(dijkstra(g, 'a'))

main()
