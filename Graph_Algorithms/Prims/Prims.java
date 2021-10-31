//Prim’s algorithm is also a Greedy algorithm.
//The idea behind Prim’s algorithm is simple, a spanning tree means all vertices must be connected. So the two disjoint subsets of vertices must be connected to make a Spanning Tree and they must be connected with the minimum weight edge to make it a Minimum Spanning Tree.
//Prim's algorithm starts with the single node and explore all the adjacent nodes with all the connecting edges at every step. The edges with the minimal weights causing no cycles in the graph got selected.
import java.util.*;
import java.io.*;
public class Prims {

	public static class Pair implements Comparable<Pair>{
		int v;
		int wt;
		Pair(int v, int wt){
			this.v=v;
			this.wt=wt;
		}
		public int compareTo(Pair o){
			return this.wt-o.wt;
		}
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int m = scn.nextInt();
		ArrayList<ArrayList<Pair>>graph = new ArrayList<>();
		for(int i=0;i<=n;i++){
			graph.add(new ArrayList<>());
		}
		for(int i=0;i<m;i++){
			int u = scn.nextInt();//vertex 1
			int v = scn.nextInt();//vertex 2
			int w = scn.nextInt();//weight between both of them
			graph.get(u).add(new Pair(v,w));
			graph.get(v).add(new Pair(u,w));
		}
		long ans = 0;
		PriorityQueue<Pair>pq = new PriorityQueue<>();
		boolean [] vis = new boolean[n+1];
		pq.add(new Pair(1,0));
		while(pq.size()>0){
			Pair rem = pq.remove();
			if(vis[rem.v]==true){//if a vertex is already selected and marked with a lower weight then do nothing and simply move forward
				continue;
			}
			//while removing we mark visited and weight is added due to that vertex i.e minimum
			vis[rem.v]=true;
			ans+=rem.wt;//adding minimum weights without creating cycle
			ArrayList<Pair>nbrs = graph.get(rem.v);
			for(Pair nbr:nbrs){
				if(vis[nbr.v]==false){
					pq.add(nbr);
				}
			}
		}
		System.out.println(ans);
	}
}

//Time Complexity of Prims Algorithm - O(V+E)