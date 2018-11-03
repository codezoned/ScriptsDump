"""
   BINARY SEARCH
   Written By @searpheon - Arka
   Fixed by @ammarmallik
"""


def binary_search(sorted_array, search_key):
    """ Algorithm:
            1. Search a sorted array by repeatedly dividing the search interval in half.
            2. Begin with an interval covering the whole array.
            3. If the value of the search key is less than the item in the middle of the interval,
               narrow the interval to the lower half.
            4. Otherwise narrow it to the upper half.
            5. Repeatedly check until the value is found or the interval is empty.
    """
    if sorted_array:
        first_index = 0
        last_index = len(sorted_array) - 1
        found = False
        while first_index <= last_index and not found:
            mid = (first_index + last_index) // 2
            if sorted_array[mid] == search_key:
                found = True
                break
            else:
                if search_key < sorted_array[mid]:
                    last_index = mid - 1
                else:
                    first_index = mid + 1
        return found
    return "Empty Array"

print(binary_search([], 0))
print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))
