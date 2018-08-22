#Selection Sort by Master-Fury
#Time Complexity:O(n^2)

def Selection_Sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr;

#Driver Code
A=[1,33,56,21,3,78,54]         #Your array
res=Selection_Sort(A)
for i in range(len(res)):
    print(res[i])


#Description
#The selection sort algorithm sorts an array by repeatedly finding the minimum element
#(considering ascending order) from unsorted part and putting it at the beginning.
