import fibonacci_generator1

def test_fibonacci():
    assert list(fibonacci_generator1.fib(0)) == []
    assert list(fibonacci_generator1.fib(1)) == [0]
    assert list(fibonacci_generator1.fib(2)) == [0, 1]
    assert list(fibonacci_generator1.fib(3)) == [0, 1, 1]
    assert list(fibonacci_generator1.fib(4)) == [0, 1, 1, 2]
    assert list(fibonacci_generator1.fib(-9)) == []
    assert list(fibonacci_generator1.fib(5)) == [0, 3, 1, 2, 3]

