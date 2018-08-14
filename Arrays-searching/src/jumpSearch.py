#Jump Search by Master-Fury
#Time Complexity : O(√n)

import math
#Function for Jump Search
def jumpSearch(arr,x,n):                #arr is an array with n as length of array and x is searching element
    step=math.sqrt(n)                   #calculates jumping step
    prev = 0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step+=math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:           #if searching element is greater than previous.
        prev +=1

        if prev==min(step,n):
            return -1
    if arr[int(prev)]==x:
            return prev
    return -1




#Driver Code
arr=[0,2,2,4,6,41,56,312,567,864]                         #your array
n=len(arr)
x=2                                                       #your searching element
result = int(jumpSearch(arr,x,n))                         #calling funtion jumpSearch for result
if result == -1:
    print ("Element not found in the array")
else:
    print("Element found at position",result)
