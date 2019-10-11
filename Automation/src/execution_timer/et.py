"""
Decorator for execution time evaluation
Usage
=====
# @exec_time
# def function_name():
"""
def exec_time(func):
    """Returns the execution time of a function"""
    import timeit

    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        res = func(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print('Elapsed time: %f' % elapsed)
        return res

    return wrapper
