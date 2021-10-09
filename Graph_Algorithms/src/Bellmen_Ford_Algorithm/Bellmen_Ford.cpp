//Bellmen Ford algorithm to detect negative weight cycle
//Time Complexity is O(V*E)
//Space Complexity is O(V)

#include<bits/stdc++.h>
using namespace std;
#define inf INT_MAX

int main()
{
  int v,e;      //V=total vertices  e=total edges
  cin>>v>>e;
  vector<vector<int>>edges;
  for(int i=0;i<e;i++)
  {
    int x,y,w;
    cin>>x>>y>>w;
    edges.push_back({x,y,w});
  }

  //dis will store the minimum weight of that vertex
  int dis[v]={inf};
  dis[0]=0;

  for(int i=1;i<v;i++)
  {
   for(int j=0;j<e;j++)
   {
   int x=edges[j][0];
   int y=edges[j][1];
   int wt=edges[j][2];
     if(dis[y] > dis[x]+wt)
       dis[y]=dis[x]+wt;
   }
  }


  int flag=0;
  for(int j=0;j<e;j++)
   {
   int x=edges[j][0];
   int y=edges[j][1];
   int wt=edges[j][2];
     if(dis[y] > dis[x]+wt)
     {
       dis[y]=dis[x]+wt;
       flag=1;
     }
   }

   // If flag becomes 1 it means weight of vertex is still decreasing Hence is negative weight cycle
  if(flag)
   cout<<"Yes, this graph has negative weight cycle.";
  else
   cout<<"No, this graph doesn't have negative weight cycle.";

 return 0;

}


/*Description
If we iterate through all edges v-1 times then it guarantees the shortest distance of vettices.
If we again iterate through all edges one more time and get a shorter path for any vertex,
then there is a negative weight cycle.  */
