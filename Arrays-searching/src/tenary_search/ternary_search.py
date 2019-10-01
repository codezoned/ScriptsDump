"""
Ternary Search in Python by @Tr-Jono

Algorithm: (list must be sorted)
1. If list is empty, return False.
1. Assign m1 and m2 s.t. they are the boundaries when the list is cut into thirds.
2. If list[m1] or list[m2] is the desired value, return True.
3. Else, use the same algorithm on:
     a. The first third of the list, if the desired value is smaller than list[m1], else
     b. The last third of the list, if the desired value is larger than list[m2], else
     c. The middle third of the list.

Time Complexity: O(log3 n)
"""


def ternary_search(a, target):
    """Ternary search if `target` is in `a`."""
    if not a:
        return False
    m1 = len(a) // 3
    m2 = len(a) - m1 - 1
    if a[m1] == target or a[m2] == target:
        return True
    if target < a[m1]:
        return ternary_search(a[:m1], target)
    elif target > a[m2]:
        return ternary_search(a[m2 + 1:], target)
    else:
        return ternary_search(a[m1 + 1:m2], target)


def main():
    print("ternary_search([1, 2, 3], 5):", ternary_search([1, 2, 3], 5))
    print("ternary_search([3, 5, 7, 9, 11, 13, 15], 5):", ternary_search([3, 5, 7, 9, 11, 13, 15], 5))
    print("ternary_search([1, 2, 3, 4, 6, 7, 8, 9, 10], 5):", ternary_search([1, 2, 3, 4, 6, 7, 8, 9, 10], 5))


if __name__ == "__main__":
    main()
