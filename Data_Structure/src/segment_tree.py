'''
Segment Tree is used for storing information about intervals, or segments. 
It allows querying which of the stored segments contain a given point.

A segment tree for a set I of n intervals uses O(n log n) storage and can be built in O(n log n) time. 
Segment trees support searching for all the intervals that contain a query point in O(log n + k), 
k being the number of retrieved intervals or segments.
\cite{https://en.m.wikipedia.org/wiki/Segment_tree }
'''


from typing import TypeVar, List, Callable
from functools import reduce


T = TypeVar('T')  # Basic Template allowing any variable as input.


def build(arr: List[T], n: int, func: Callable[[T, T], T]) -> List[T]:
    """
    builds the trees from the passed list.
    Time Complexity: O(n)
    
    Parameters
    ----------
    arr: iterable
       list of elements to be added to the data structure
    func: Callable
        function that will be binary operator

    Returns
    -------
    Built Segment Tree
    """
    tree = [0 for i in range(n)]
    tree.extend(arr)
    for i in range(n-1, 0, -1):
        tree[i] = func(tree[i << 1], tree[i << 1 | 1])
    return tree


def point_update(tree: List[T], n: int, pos: int, val: int, func: Callable[[T, T], T]) -> None:
    """
    Updates the tree with given value.
    Time Complexity: O(lgn)
    
    Parameters
    ----------
    tree: list
        built segment tree
    n: int
     size of segment tree
    pos: int
       index which is to be updated.
    val: int
        the value with which arr[pos] is to be updated.
    func: Callable
        binary operator which will be applied to the input parameters.
    """
    pos += n
    tree[pos] = val
    while pos > 1:
        tree[pos >> 1] = func(tree[pos], tree[pos ^ 1])
        pos >>= 1


def query(tree: List[T], l: int, r: int, n: int, func: Callable[[T, T], T], start_ans=0, right_inclusive=True):
    """
    Parameters
    ----------
    tree: segment Tree
    l: left
    r: right
    n: max size of array
    func: Callable to be operated on the input parameters.
    start_ans: seed value with which run is to be initialised
    """

    l += n
    r += n + right_inclusive
    ans = start_ans
    while l < r:
        if l & 1:
            ans = func(ans, tree[l])
            l += 1
        if r & 1:
            r -= 1
            ans = func(ans, tree[r])
        l >>= 1
        r >>= 1
    return ans



if __name__ == '__main__':
    arr = [3, 2, 4, 5, 6, 8, 2, 4, 5]
    n = len(arr)
    func = int.__mul__
    tree = build(arr, n, func)
    point_update(tree, n, 0, 0, func)
    l, r = 2, 4
    assert query(tree, l, r, n, func, start_ans=1) == reduce(func, arr[l: r+1]), "Segment Tree faulty"

