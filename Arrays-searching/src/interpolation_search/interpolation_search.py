#Interpolation Search by Master-Fury
#Time Complexity : O (log log n))

#Function for Interpolation Search
def interpolationSearch(arr,n,x):           #arr is an array of size n and x is our searching element        
    low=0                                   #low is the index of first element
    high=(n-1)                              #high is the index of last element

    while low <= high and x>=arr[low] and x<=arr[high]:
        pos = low+ int(((float(high-low)*(x-arr[low]))/(arr[high]-arr[low])))  #Formula to calculate postion
        if arr[pos]==x:
            return pos
        if arr[pos]<x:
            low=pos+1
        else:
            high=pos-1
    return -1

#Driver Code

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]  #Your array
n=len(arr)                                                          
x=22                                                                #Your Searching element
result= interpolationSearch(arr,n,x)                                #Function Call
if result == -1:
    print("Element not found")
else:
    print("Element found at position ",result)
