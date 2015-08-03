from functools import wraps

__author__ = 'stephenosullivan'

""" Tangled dependencies and memoization """

def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

class Dynamic:
    def __init__(self):
        print(self.fib(10))
        print(self.fib_gen(10))

    @memo
    def fib(self, i):
        if i < 2:
            return 1
        return self.fib(i - 1) + self.fib(i - 2)

    @memo
    def fib_gen(self, i):
        if i < 2:
            yield 1
        yield self.fib(i - 1) + self.fib(i - 2)



if __name__ == '__main__':
    sol = Dynamic()
