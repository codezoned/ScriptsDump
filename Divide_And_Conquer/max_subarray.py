def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -1
    sum = 0
    for i in range(mid, 0, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
    
    right_sum = -1
    sum = 0
    for j in range(mid+1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
    
    return (left_sum + right_sum)

def find_max_subarray(arr, low, high):

    if high == low:
        return arr[low]
    
    else:
        mid = (low + high) // 2
        left_sum = find_max_subarray(arr, low, mid)
        right_sum = find_max_subarray(arr, mid+1, high)
        cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum

arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(find_max_subarray(arr, 0, len(arr) - 1))            