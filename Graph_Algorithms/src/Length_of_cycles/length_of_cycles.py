'''
If a node is visited again in DFS it means there is a cycle. To get the length of that cycle, we save the parent of current node at every stage of that DFS.

Once a visited node is detected again, from this node go its parent and from there to its parent and so on till we reach the first node again. We keep track of how many nodes we have traversed in this process and that will be the length of the cycle.
'''


class Graph:
    def __init__(self, nnodes, nedges):
        self.nnodes = nnodes
        self.nedges = nedges
        self.adj = []
        for i in  range(nnodes+1):
            temp = []
            for j in range(nnodes+1):
                temp.append(0)
            self.adj.append(temp)
        self.cyclens = []
        #cyclens will save the length of all cycles 

    def addEdge(self, a, b):
        self.adj[a][b] = 1
        self.adj[b][a] = 1


    #function to perform dfs and simultaneously calculate lengths of cycles in the graph
    def dfsHelper(self, v, visited, myval, parent, parents):


        parents[v] = parent
        #save the parent if this node.


        visited[v] = True
        #mark this node as detected

        for i in range(1, len(self.adj[0])):

            if(self.adj[v][i] == 1):
                if(visited[i] == False):
                    self.dfsHelper(i, visited, myval+1, v, parents)

                else:               

                    if(i!=parent):
                        #cycle detected                     

                        cur = parent
                        count =1
                        #start traversing the parents from here till we reach the current node again
                        while(cur!=i):                          
                            cur = parents[cur]

                            count+=1
                            if(count>self.nedges):
                                break

                        #save count which is the length of the cycle.
                        if(count <self.nedges):
                            self.cyclens.append(count+1)

                visited[i] = True



    #wrapper function to call the above helper function.
    def dfs(self, v):
        visited = [0 for i in range(self.nnodes+1)]
        self.cyclens = []
        parents = [0]*(self.nnodes+1)
        self.dfsHelper(v, visited, 1, 0, parents)
        print(sum(self.cyclens))