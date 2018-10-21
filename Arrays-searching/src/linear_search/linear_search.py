#Linear search for an element 'ele' in array 'a'
#author-@rats123

def linear(a,ele):
    for i in range(len(a)):   #for loop iterates through every single element in array
        if ele==a[i]:         #if match is found it returns the index
            return i



    return 'Not found'



##example run


print(linear([1,2,3,4,5,6,12,23],4))
