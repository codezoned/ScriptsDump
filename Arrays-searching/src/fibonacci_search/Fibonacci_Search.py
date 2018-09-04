#Made by SHASHANK CHAKRAWARTY
# Python3 program for Fibonacci search.
'''
Works for sorted arrays
A Divide and Conquer Algorithm.
Has Log n time complexity.

1)Fibonacci Search divides given array in unequal parts

'''

#Given a sorted array arr[] of size n and an element x to be searched in it. Return index of x if it is present in array else return -1.

def fibMonaccianSearch(arr, x, n):
     
    # Initialize fibonacci numbers 
   
    var2 = 0 # (m-2)'th Fibonacci No.
    var1 = 1 # (m-1)'th Fibonacci No.
    res = var2 + var1 # m'th Fibonacci

   
    # fibM is going to store the smallest 
    # Fibonacci Number greater than or equal to n 
    
    while (res < n):
        var2 = var1
        var1 = res
        res = var2 + var1
 
    # Marks the eliminated range from front
    offset = -1;
 
    # while there are elements to be inspected.
    # Note that we compare arr[var2] with x.
    # When fibM becomes 1, var2 becomes 0 
   

    while (res > 1):
         
        # Check if var2 is a valid location
        i = min(offset+var2, n-1)
 
        # If x is greater than the value at 
        # index var2, cut the subarray array 
        # from offset to i 
        if (arr[i] < x):
            res = var1
            var1 = var2
            var2 = res - var1
            offset = i
 
         # If x is greater than the value at 
        # index var2, cut the subarray 
        # after i+1
        elif (arr[i] > x):
            res = var2
            var1 = var1 - var2
            var2 = res - var1
 
        # element found. return index 
        else :
            return i
 
    # comparing the last element with x */
    if(var1 and arr[offset+1] == x):
        return offset+1;
 
    # element not found. return -1 
    return -1
 
# Driver Code, you can change the values accordingly
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100]
n = len(arr)
x = 85
print("Found at index:",
      fibMonaccianSearch(arr, x, n))

