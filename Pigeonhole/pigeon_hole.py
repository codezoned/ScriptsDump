def pigeonhole_sort(list):
    min_elem = min(list)
    max_elem = max(list)
    size = max_elem - min_elem + 1
    holes = [0] * size
    for x in list:
        holes[x - min_elem] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            list[i] = count + min_elem
            i += 1
    return list
