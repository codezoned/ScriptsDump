

"""Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements
where the number of elements (n) and the length of the range of possible key values (N) are approximately the same"""

# Time complexity O(n + N)
# Space complexity O(n)

def pigeonhole_sort(list):
    min_elem = min(list)
    max_elem = max(list)
    size = max_elem - min_elem + 1
    holes = [0] * size               # auxiliary list of pigeonholes
    for x in list:                   # Populate the pigeonholes.
        holes[x - min_elem] += 1
    i = 0
    for count in range(size):         # Put the elements back into the array in order.
        while holes[count] > 0:
            holes[count] -= 1
            list[i] = count + min_elem
            i += 1
    return list


list = [10,2,7,9,4,5,3]
print pigeonhole_sort(list)


