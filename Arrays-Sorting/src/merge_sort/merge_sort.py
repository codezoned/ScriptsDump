#made by SHASHANK CHAKRAWARTY
#The code demostrates step by step process of the merge sort how it splites, dividesin tothe 2 halves and then after getting sorted in the steps it gets merged

#Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
'''
1)Time Complexity: Can be represented by Recurrance relation Time Complexity:T(n) = 2T(n/2) + \Theta(n)
2)Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array in two halves.
3)Auxiliary Space: O(n)
4)Algorithmic Paradigm: Divide and Conquer
5)Sorting In Place: No in a typical implementation
6)Stable: Yes
'''

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
#the array gets divided into the halves

        mid = len(alist)//2

#here the subarrays are created

        lefthalf = alist[:mid]
        righthalf = alist[mid:]

#function calling occurs
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i] #copy the value to the newly created array in the lefthalf
                i=i+1
            else:
                alist[k]=righthalf[j] #copy the value to the newly created array in the righthalf
                j=j+1
            k=k+1
#the process of merging goes from here
        while i < len(lefthalf):  
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
#The DRIVER CODE,YOU CAN CHANGE THE VALUE ACCORDINGLY


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
