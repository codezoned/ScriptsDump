#Binomial Coefficient by Master-Fury
  
def binomialCoefficient(n , k): 
  
    if k==0 or k ==n : 
        return 1
  
    
    return binomialCoefficient(n-1 , k-1) + binomialCoefficient(n-1 , k)   # Recursive Call 
  
# Driver Program  
n = 6
k = 3
print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoefficient(n , k)) )
