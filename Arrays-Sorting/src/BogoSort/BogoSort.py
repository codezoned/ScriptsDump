
'''
bogosort is a highly ineffective sorting function based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms. 
'''


import random


'''
Random shuffle elements in the array, by swaping random 2 elements in each loop iteration.

'''
def shuffle(array):
    for i in range(len(array)-1, -1, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]

'''
Checks if the array is sorted, by having non-decreasing sequence.

'''

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


'''
__main__ function of the sort.

'''
def bogosort(array):
    while not is_sorted(array):
        shuffle(array)
    return array
