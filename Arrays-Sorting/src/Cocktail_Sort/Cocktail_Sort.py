#Cocktail Sort by Master-Fury
#Worst and Average Case Time Complexity: O(n*n)
#Best Case Time Complexity: O(n)

def Cocktail_Sort(arr):                    #Cocktail Sort Function
    l=len(arr)
    swapped= True
    start=0
    end=l-1
    while(swapped == True):
        swapped=False
        for i in range(start,end):                   #Forward loop
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped= True
        if(swapped==False):
            break
        swapped = False
        end=end-1
        for i in range (end-1,start-1,-1):            #Backward Loop
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped= True
        start=start+1

#Driver Code

arr=[2,5,21,431,4,53,22,144,123,8]      #Your array
Cocktail_Sort(arr)
print("Sorted array: ",arr)


##Description
##Cocktail Sort is a variation of Bubble sort.
##The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct
##position in first iteration and second largest in second iteration and so on.
##Cocktail Sort traverses through a given array in both directions alternatively.
