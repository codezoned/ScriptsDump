// Floyd Warshall Algorithm
// A space efficient algorithm to find shortest distance in space complexity of (O(1))
// Time complexity - O(v^3)

#include<bits/stdc++.h>
using namespace std;

// Function which finds the shortest distance
void shortest_distance(vector<vector<int>>&matrix)
{
       // Making first loop as intermediate between two vertices
	    for(int k=0;k<matrix.size();k++)
	    {
	        // Value of i is treated as starting vertex of edge
	        for(int i=0;i<matrix.size();i++)
	        {
	            // Value of j is treated as starting vertex of edge
	              for(int j=0;j<matrix.size();j++)
	              {
                    // Avoiding self edge as well as intermediate vertex which is same as either of the two vertices of edge
	                if(k!=i && k!=j  && i!=j)
	                {
	                    // Not trying to put unavailable edge as intermediate edge And also adding edge if not available
	                    if(matrix[i][k]!=-1 && matrix[k][j]!=-1 && ((matrix[i][j] > (matrix[i][k]+matrix[k][j])) || matrix[i][j]==-1))
	                     matrix[i][j]=matrix[i][k]+matrix[k][j];
	                }
	              }

	        }
	    }
}

int main()
{
 int v;
 cin>>v;
 vector<vector<int>>matrix(v,vector<int>(v,-1));
 for(int i=0;i<v;i++)
 {
  for(int j=0;j<v;j++)
  {
   cin>>matrix[i][j];
  }
 }
 shortest_distance(matrix);

 // Printing the updated matrix
 for(int i=0;i<v;i++)
 {
  for(int j=0;j<v;j++)
  {
   cout<<matrix[i][j]<<" ";
  }
  cout<<endl;
 }
 return 0;
}

// Description
// This algorithm helps in finding shortest distance between
// every pair of vertices in a given edge weighted directed Graph in in-place.
// Core idea:- add any other vertex in between two edge and check if the previous distance
// is greater than adding two edge connected with the intermediate edge, if yes update it.
