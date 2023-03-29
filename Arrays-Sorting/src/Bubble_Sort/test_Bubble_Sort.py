from unittest import TestCase


class Test(TestCase):
    def test_bubble_sort(self):
        from Bubble_Sort import Bubble_Sort
        arr = [34,21,345,765,44,67,32,1]
        expected = [1, 21,32, 34, 44, 67, 345, 765 ]
        self.assertEqual(Bubble_Sort(arr),expected)

    def test_bubble_sort2(self):
        from Bubble_Sort import Bubble_Sort
        arr2 = [1,34,21,345,765,44,67,32,1]
        expected2 = [1,1, 21, 32, 34, 44, 67, 345, 765 ]
        self.assertEqual(Bubble_Sort(arr2),expected2)

