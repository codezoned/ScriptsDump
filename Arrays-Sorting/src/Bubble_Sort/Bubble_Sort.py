#Bubble Sorting by Master-Fury
#Worst and Average Case Time Complexity: O(n*n)

def Bubble_Sort(arr):
    l=len(arr)
    for i in range(l):
        for j in range(0,l-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return (arr)


#Driver Code
 #Your array
res=Bubble_Sort([1,34,21,345,765,44,67,32])
print(res)


#DESCRIPTION
#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
