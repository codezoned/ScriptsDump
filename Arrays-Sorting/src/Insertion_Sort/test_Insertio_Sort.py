
def test_Insertion_Sort():
    from Insertion_Sort import Insertion_Sort
    # Test avec un tableau vide
    arr = []
    Insertion_Sort(arr)
    assert arr == []
   
    # Test avec un tableau déjà trié
    arr = [1, 2, 3, 4, 5]
    Insertion_Sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    # Test avec un tableau non trié
    arr = [5, 2, 4, 6, 1, 3]
    Insertion_Sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6]
    # Test avec un tableau contenant des doublons
    arr = [2, 1, 4, 2, 3, 4]
    Insertion_Sort(arr)

