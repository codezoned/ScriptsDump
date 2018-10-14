
# Python program for Zeckendorf's theorem. It finds 
# representation of n as sum of non-neighbouring 
# Fibonacci Numbers. 
  
# Returns the greatest Fibonacci Numberr smaller than 
# or equal to n. 
def nearestSmallerEqFib(n): 
      
    # Corner cases 
    if (n == 0 or n == 1): 
        return n 
         
    # Finds the greatest Fibonacci Number smaller 
    # than n. 
    f1, f2, f3 = 0, 1, 1
    while (f3 <= n): 
        f1 = f2; 
        f2 = f3; 
        f3 = f1 + f2; 
    return f2; 
  
  
# Prints Fibonacci Representation of n using 
# greedy algorithm 
def printFibRepresntation(n): 
      
    while (n>0): 
  
        # Find the greates Fibonacci Number smaller 
        # than or equal to n 
        f = nearestSmallerEqFib(n); 
   
        # Print the found fibonacci number 
        print (f), 
   
        # Reduce n 
        n = n-f 
  
# Driver code test above functions 
n = 30
print ("Non-neighbouring Fibonacci Representation of", n, "is")
printFibRepresntation(n) 
