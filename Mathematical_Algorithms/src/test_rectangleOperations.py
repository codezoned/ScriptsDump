from Mathematical_Algorithms.src.RectangleOperations import Rectangle

def test_multiply():
    # two rectangles
    r1 = Rectangle(0, 0, 10, 10)
    r2 = Rectangle(5, 2, 7, 9)
    t2 = r1.multiply(r2)
    assert t2.writer() == "Rectangle(5, 2, 5, 7)"