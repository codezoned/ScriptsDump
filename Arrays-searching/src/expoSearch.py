#Exponential Search by Master-Fury
#Time Complexity : O(log n)


#Recursive Binary Search Funnction
def binarySearch(arr,l,r,x):                                        #arr[l...r] is an array, x is searching element
    if r>=l:
        mid=int((l+r)/2)
        if arr[mid]==x:                                             #if mid element is searching element
            return mid
        if arr[mid]>x:                                              #if mid element is greater than searching element
            return binarySearch(arr,l,mid-1,x)
        return binarySearch(arr,mid+1,r,x)                          #if mid element is smaller than searching element 
    return -1

#Function for finding range
def expoSearch(arr,n,x):
    if arr[0]==x:                                                   #to check if searching element is first element
        return 0
    i=1
    while i<n and arr[i]<=x:                                        #to find the range for binary search
        i=i*2
    return binarySearch(arr,int(i/2),min(i,n),x)


# Driver Code
arr=[2,3,4,10,32,43]                                                #your array
n=len(arr)
x=43                                                                #your searching element
result=expoSearch(arr,n,x)                                          #calling funtion expoSearch for result
if result == -1:
    print ("Element not found in the array")
else:
    print ("Element found at position " , result+1)
        
    
    
