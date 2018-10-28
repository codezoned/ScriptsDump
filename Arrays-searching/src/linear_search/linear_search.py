"""
    Linear search
    Search Key in an Array
    Written by: author-@rats123
    Updated by: @ammarmallik
"""


def linear_search(arr, search_key):
    """ Algorithm:
            1. If array is empty, return -2
            2. Iterate array and compare each value with search_key
            3. if search_key is found, return index
            4. Otherwise return -1
    """
    if arr:
        for index, element in enumerate(arr):
            if element == search_key:
                return index

        return -1

    return -2


def print_result(search_key, index):
    """Returns error based on given index"""
    errors = {
        -1: "{} doesn't exist in array".format(search_key),
        -2: "Array is Empty"
    }
    print(errors[index] if index in errors else "Index: {}".format(index))


if __name__ == "__main__":
    """ Test cases """

    samples = [
        {"arr": [1, 2, 3, 4, 5], "search_key": 5},
        {"arr": [], "search_key": 5},
        {"arr": [1, 2, 3, 4, 5], "search_key": 6}
    ]

    for item in samples:
        index = linear_search(item.get("arr"), item.get("search_key"))
        print_result(item.get("search_key"), index)
