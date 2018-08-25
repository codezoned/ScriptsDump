#Comb Sort by Master-Fury
#Time Complexity : Worst case complexity of this algorithm is O(n^2).
#Best Case complexity is O(n).

#DESCRIPTION
##Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values.
##So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1.
##The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1.
##Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bublle Sort.
##The shrink factor has been empirically found to be 1.3 (by testing Combsort on over 200,000 random lists) [Source: Wiki]


def new_gap(gap):                #Function to find the gap(or range)
    gap=(gap*10)//13
    if(gap<1):
        return 1
    return gap

def Comb_Sort(arr):               #Comb Sort Function
    n=len(arr)
    gap=n
    swapped = True
    while gap!=1 or swapped == 1:
        gap=new_gap(gap)
        swapped=False
        for i in range(0,n-gap):
            if (arr[i]>arr[i+gap]):
                arr[i],arr[i+gap]=arr[i+gap],arr[i]
                swapped =True
#Driver Code

arr=[2,85,443,7,8,3,67,3,89,0]      #Your array
Comb_Sort(arr)
print ("Sorted array: ",arr)
