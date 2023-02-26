# Recursive function to search x in arr[l..r]
# Another python program to search an element linearly in an array using Recursion (Read again 💯 ) 
# Why recursion? Because it makes the task easier and reduces time complexity.
def rec_search(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return rec_search(arr, l + 1, r - 1, x)


"""
# Main Code  

arr = [12, 34, 54, 2, 3] 
n = len(arr) 
x = 3
index = rec_search(arr, 0, n-1, x) 
if index != -1: 
    print "Element", x,"is present at index %d" %(index) 
else: 
    print "Element %d is not present" %(x)
"""
