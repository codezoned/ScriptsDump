# Kadane's Algorithm by Master-Fury
# Worst and Average Case Time Complexity: O(n)

from sys import maxsize  # importing maximum int from sys module


def kadane_algorithm(arr: int):

    len_arr = len(arr)  # Finding the len of array

    max_so_far = -maxsize - 1  # Setting max value as maximum negative value
    max_ending_here = 0

    for i in range(0, len_arr):
        max_ending_here = max_ending_here + arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


# Driver function
sample_array = [-5, -2, 5, 9, -8, 9, 4, 7, -7, -1]
max_cont_subarray_sum = kadane_algorithm(sample_array)

print("The maximum sum of contigous sub array is - ", max_cont_subarray_sum)

# DESCRIPTION
# This algorithm is widely used to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum.
# The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this).
# And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this).
# Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far .
# It can be viewed both as a greedy and DP problem.
