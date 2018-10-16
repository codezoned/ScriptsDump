# Code by BH4

import math


def memorize(f):
    """Simple memorization decorator.
    Defines a dictionary which is then checked if an entry exists for any
    argument which the function being decorated is called on. If it
    already exists then that value is returned without calling the function,
    if it does not exist then the function is called to determine the output
    and it is stored in the dictionary.
    """
    mem = {}

    def helper(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]

    return helper


@memorize
def num_integer_partitions(n):
    """Returns the number of ways n can be written in terms of a sum of
    positive integers.
    Uses memorization to speed up calculation.
    """

    if n == 0 or n == 1:
        return 1

    if n < 0:
        return 0

    # Recurrence relation for the partition function.
    tot = 0
    maxK = int((1+math.sqrt(1+24*n))/6)
    for k in range(1, maxK+1):
        a = n-k*(3*k-1)//2
        b = n-k*(3*k+1)//2

        if k % 2 == 0:
            tot -= num_integer_partitions(a)+num_integer_partitions(b)
        else:
            tot += num_integer_partitions(a)+num_integer_partitions(b)

    return tot


# Example of use
for i in range(0, 20):
    print(num_integer_partitions(i))
