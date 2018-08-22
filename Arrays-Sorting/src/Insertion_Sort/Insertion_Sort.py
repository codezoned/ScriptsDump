#Insertion Sort by Master-Fury
#Time Complexity: O(n*n)

def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        pos=arr[i]
        j=i-1
        while j>=0 and pos<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=pos

#Driver Code
arr=[43,25,44,78,453,897,6,54]         #Your array
Insertion_Sort(arr)
print(arr)


#Description
#We can use binary search to reduce the number of comparisons in normal insertion sort.
#Binary Insertion Sort find use binary search to find the proper location to insert the selected item at each iteration.
# Insertion sort is used when number of elements is small. 
#It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
