//DSU - Disjoint Set Union DataStructure
//A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
//Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
//Union: Join two subsets into a single subset.

//To check cycle in graph using DSU Data structure
import java.util.*;
import java.io.*;
 
class DSU
{
    int V, E;    
    Edge edge[]; 
 
    class Edge
    {
        int src, dest;
    };
 
    // Creates a graph with V vertices and E edges
    DSU(int v,int e)
    {
        V = v;
        E = e;
        edge = new Edge[E];
        for (int i=0; i<e; ++i)
            edge[i] = new Edge();
    }
 
    // Find function to find the subset of an element i
    int find(int parent[], int i)
    {
        if (parent[i] == -1)
            return i;
        return find(parent, parent[i]);
    }
 
    // Union function to do union of two subsets
    void Union(int parent[], int x, int y)
    {
        parent[x] = y;
    }
    int isCycle( DSU graph)
    {
        int parent[] = new int[graph.V];
        for (int i=0; i<graph.V; ++i)
            parent[i]=-1;
 
        // Iterate through all edges of graph, find subset of both
        // vertices of every edge, if both subsets are same, then
        // there is cycle in graph.
        for (int i = 0; i < graph.E; ++i)
        {
            int x = graph.find(parent, graph.edge[i].src);
            int y = graph.find(parent, graph.edge[i].dest);
 
            if (x == y)
                return 1;
 
            graph.Union(parent, x, y);
        }
        return 0;
    }
 
    // Driver Method
    public static void main (String[] args)
    {
        int V = 3, E = 3;
        DSU graph = new DSU(V, E);
 
        // add edge 0-1
        graph.edge[0].src = 0;
        graph.edge[0].dest = 1;
 
        // add edge 1-2
        graph.edge[1].src = 1;
        graph.edge[1].dest = 2;
 
        // add edge 0-2
        graph.edge[2].src = 0;
        graph.edge[2].dest = 2;
 
        if (graph.isCycle(graph)==1)
            System.out.println( "graph contains cycle" );
        else
            System.out.println( "graph doesn't contain cycle" );
    }
}
