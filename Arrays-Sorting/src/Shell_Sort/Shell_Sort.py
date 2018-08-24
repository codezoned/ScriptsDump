#Shell Sort by Master-Fury
#Time complexity:O(n^2) 

def Shell_Sort(arr):
    l=int(len(arr))
    gap=int(l/2)
    while gap > 0:
        for i in range(gap,l):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2             #int division operator is used here

#Driver Code
arr=[32,452,52,1,45,30,22,13]               #Your array
Shell_Sort(arr)
print("Sorted array: ",arr)


#Description
#ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead.
#When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items.
#In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1.
#An array is said to be h-sorted if all sublists of every h’th element is sorted.
