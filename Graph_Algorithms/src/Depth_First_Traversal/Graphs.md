<h1>Graphs</h1>

Q1) Islands

#### An island is a small piece of land surrounded by water . A group of islands is said to be connected if we can reach from any given island to any other island in the same group . Given N islands (numbered from 1 to N) and two lists of size M (u and v) denoting island u[i] is connected to island v[i] and vice versa . Can you count the number of connected groups of islands.

```c++

void dfs(int curr, int* visited, int** adj_matrix, int n){
    visited[curr] = 1;
    for(int i = 0; i<n ; i++){
        if(adj_matrix[curr][i]==1 && visited[i] == 0 && curr!= i){
            dfs(i, visited, adj_matrix, n);
        }
    }
}

int solve(int n,int m,vector<int>u,vector<int>v)
{
	int** adj_matrix = new int*[n];
    for(int i = 0; i<n; i++){
        adj_matrix[i] = new int[n];
        for(int j = 0; j<n; j++){
            adj_matrix[i][j] = 0;
        }
    }
    
    for(int i = 0; i<m; i++){
        adj_matrix[u[i]-1][v[i]-1] = 1;
        adj_matrix[v[i]-1][u[i]-1] = 1;
    }
   

    int* visited = new int[n];
    for(int i = 0 ; i<n; i++){
        visited[i] = 0;
    }
    int count = 0;
    for(int i = 0; i<n; i++){
        if(visited[i] == 0){
            count++;
            dfs(i, visited, adj_matrix, n);
        }
    }
    return count;
    
    
}

```

Q2) 

