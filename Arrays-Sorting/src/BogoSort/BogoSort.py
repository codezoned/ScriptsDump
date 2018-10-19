import random
def shuffle(array):
    for i in range(len(array)-1, -1, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
def bogosort(array):
    while not is_sorted(array):
        shuffle(array)
    return array
