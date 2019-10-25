'''
Code to find the strongly connected components of a graph using Kosaraju's Algorithm
Time complexity: O(V + E)
'''

from collections import defaultdict

class Graph:
    
    #Constructor that basically initiallises every new vertex in dict as an 
    #empty list
    def __init__(self):
        self.graph = defaultdict(list)
        self.transpose = defaultdict(list)
        self.vertexList = []

    def addEdgeDirected(self, u, v, w = 1):
        self.graph[u].append([v, w])
        self.transpose[v].append([u, w])
        if u not in self.vertexList:
            self.vertexList.append(u)
        if v not in self.vertexList:
            self.vertexList.append(v)

    def addEdgeUndirected(self, u, v, w = 1):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])
        if u not in self.vertexList:
            self.vertexList.append(u)
        if v not in self.vertexList:
            self.vertexList.append(v)

    #s here is the source node
    def BFS(self, s):
        color = ['w']*len(self.graph)
        #Queue that will store the nodes in BFS
        queue = []
        queue.append(s)
        color[s] = 'g'
        while(queue):
            s = queue.pop(0) #dequeue operation
            color[s] = 'b'
            print s,
            for i in self.graph[s]:
                if (color[i] == 'w'):
                    queue.append(i)
                    color[i] = 'g'

    def DFS(self, s, time = 0, startTime = {}, endTime = {}, visited = defaultdict(bool), DFSList = []):
        startTime[s] = time
        visited[s] = True
        DFSList.append(s)
        for i in self.graph[s]:
            if(visited[i[0]] == False):
                time += 1
                self.DFS(i[0], time, startTime, endTime, visited, DFSList)
                endTime[i[0]] = time
        return DFSList


    def TopologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        print visited
        for i in self.graph[v]:
            if (visited[i[0]] == False):
                self.TopologicalSortUtil(i[0], visited, stack)
            
        stack.insert(0, v)  #adding to bottom of stack same as adding to top then printing in reverse


    def TopologicalSort(self):
        #self.vertexList.sort()
        visited = defaultdict(bool)
        stack = []

        for i in self.vertexList:
            if (visited[i] == False):
                self.TopologicalSortUtil(i, visited, stack)

        print "The Graph vertices after topological sort are:"
        print stack

    def DFSUtil(self, s, visited):
        visited[s] = True
        print s,
        for i in self.transpose[s]:
            if (visited[i[0]] == False):
                self.DFSUtil(i[0], visited)

    def FillOrder(self, s, visited, stack):
        visited[s] = True
        for i in self.graph[s]:
            if (visited[i[0]] == False):
                self.FillOrder(i[0], visited, stack)

        stack.append(s)

    def Kosarajus(self):
        #Step1: Create the stack
        stack = []
        visited = defaultdict(bool)
        for i in self.vertexList:
            if (visited[i] == False):
                self.FillOrder(i, visited, stack)

        #Step2: Empty the stack, and print the SCC's

        visited = defaultdict(bool)
        while (stack):
            i = stack.pop()
            if (visited[i] == False):
                self.DFSUtil(i, visited)
                print ""

#Testing on graph

g = Graph()
g.addEdgeDirected(0, 3)
g.addEdgeDirected(3, 2)
g.addEdgeDirected(2, 1)
g.addEdgeDirected(1, 0)
g.addEdgeDirected(4, 2)
g.addEdgeDirected(5, 4)

print "Following are strongly connected components in given graph"

g.Kosarajus()



