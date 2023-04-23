import sys

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    a = int(sys.argv[1])
    print(list(fib(a))) 

