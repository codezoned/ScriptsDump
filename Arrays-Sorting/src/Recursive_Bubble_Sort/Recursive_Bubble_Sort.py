#Recursive Bubble Sort by Master Fury


def Bubble_sort_rec(arr,l):
    if l==1:
        return
    for i in range(l-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        Bubble_sort_rec(arr,l-1)                   #Recursion 
    return arr

#Driver Code
arr=[34,76,45,342,54,6,788,23]                  #Your array
l=len(arr)
Bubble_sort_rec(arr,l)
print(arr)




#Recursive Bubble Sort has no performance/implementation advantages,
#but can be a good question to check one’s understanding of Bubble Sort and recursion.
