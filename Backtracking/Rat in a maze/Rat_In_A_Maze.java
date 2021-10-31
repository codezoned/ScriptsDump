
//A Maze is given as N*N binary matrix of blocks where source block is the upper left most block(maze[0][0]) and destination block is lower rightmost block (maze[N-1][N-1]). 
//A rat starts from source and has to reach the destination. 
//The rat can move only in two directions: left, right, down, up.
//In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. 
//Backtracking - Solving one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time is the process of backtracking.
public class Rat_In_A_Maze {
 
    // Size of the maze
    static int N;
 
    //function to print solution matrix 
    void printSolution(int sol[][])
    {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                System.out.print(
                    " " + sol[i][j] + " ");
            System.out.println();
        }
    }
 
    boolean isSafe(
        int maze[][], int x, int y)
    {
        // if x, y outside maze return false directly
        return (x >= 0 && x < N && y >= 0
                && y < N && maze[x][y] == 1);
    }
 
    boolean solveMaze(int maze[][])
    {
        int sol[][] = new int[N][N];
 
        if (solveMazeUtil(maze, 0, 0, sol) == false) {
        	//No solution possible
            System.out.print("Solution doesn't exist");
            return false;
        }
 
        printSolution(sol);
        return true;
    }
 

    boolean solveMazeUtil(int maze[][], int x, int y,
                          int sol[][])
    {
        // if x, y is destination return true
        if (x == N - 1 && y == N - 1
            && maze[x][y] == 1) {
            sol[x][y] = 1;
            return true;
        }
 
        // Check if maze[x][y] is valid
        if (isSafe(maze, x, y) == true) {
              // Check if the current block is already visited.   
              if (sol[x][y] == 1)
                  return false;
           
            // mark x, y as visited
            sol[x][y] = 1;
            if (solveMazeUtil(maze, x + 1, y, sol))
                return true;
            if (solveMazeUtil(maze, x, y + 1, sol))
                return true;
            if (solveMazeUtil(maze, x - 1, y, sol))
                return true;
            if (solveMazeUtil(maze, x, y - 1, sol))
                return true;
            
            sol[x][y] = 0;//un-mark the maze index so that other paths can be explored
            return false;
        }
 
        return false;
    }
 
    public static void main(String args[])
    {
        Rat_In_A_Maze rat = new Rat_In_A_Maze();
        int maze[][] = { { 1, 1, 1, 1 },
                         { 1, 1, 0, 1 },
                         { 0, 1, 0, 1 },
                         { 1, 1, 0, 1 } };
 
        N = maze.length;
        rat.solveMaze(maze);
    }
}

//Time complexity - O(2^(n*n))