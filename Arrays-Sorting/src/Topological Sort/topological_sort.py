''' 
     TOPOLOGICAL SORT :
     Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, 
     vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
     
     For more Information about Topological Sort visit : https://cp-algorithms.com/graph/topological-sort.html

     You are given a directed graph with n vertices and m edges. 
     You have to number the vertices so that every edge leads from the vertex with a smaller number assigned to the vertex with a larger one.     
'''

from __future__ import print_function

'''
     a
    / \
   b  c
  / \
  d  e
'''

edges = {'a': ['c', 'b'], 'b': ['d', 'e'], 'c': [], 'd': [], 'e': []}
vertices = ['a', 'b', 'c', 'd', 'e']


def topological_sort(start, visited, sort):
   #Perform topolical sort on a directed acyclic graph.
    current = start
    # add current to visited
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    # return sort
    return sort


sort = topological_sort('a', [], [])
print(sort) # prints the sorted array

''' 
     OUTPUT : ['c', 'd', 'e', 'b', 'a']
     
     Time Complexity: O(V+E). 
     The above algorithm is simply DFS so time complexity is the same as DFS which is. O(V+E).

'''
