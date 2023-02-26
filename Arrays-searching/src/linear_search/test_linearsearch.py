import linear_search 



def test1():
    assert 3 == linear_search.linear_search([17, 1, 8, 29, 5],5)

def test2():
    assert -2 == linear_search.linear_search([],5)

def test3():
    assert -1 == linear_search.linear_search([17, 1, 8, 29, 5],6)
