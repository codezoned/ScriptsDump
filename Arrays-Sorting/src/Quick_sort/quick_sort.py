def quickSort(arr):
    """Apply quick sort on the given array

    :param arr: the array to sort
    :type arr: list
    """
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

# Unit test
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]  # The array to sort
a = quickSort(a)
assert all(a[i] <= a[i+1] for i in range(len(a)-1))  # Assert array is sorted

# Quick sort: Quicksort is a comparison sort, meaning that it can 
# sort items of any type for which a "less-than" relation is defined. 
# In efficient implementations it is not a stable sort, meaning 
# that the relative order of equal sort items is not preserved. 
# Quicksort can operate in-place on an array, requiring small 
# additional amounts of memory to perform the sorting. It is very 
# similar to selection sort, except that it does not always choose 
# worst-case partition.
