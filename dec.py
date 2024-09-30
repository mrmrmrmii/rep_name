from functools import wraps
from types import NoneType


def memoized(maxsize=None):
    def dec(func):
        memory={}
        @wraps(func)
        def iner(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key not in memory and len(memory) != maxsize:
                memory[key] = func(*args, **kwargs)
            if key in memory:
                return memory[key]
            if key not in memory and len(memory) == maxsize:
                memory.popitem()
                memory[key] = func(*args, **kwargs)

            return memory[key]
        return iner
    return dec
@memoized(maxsize=2)
def sum_of_two(a, b):
    print(a, b, end='; ')
    return a + b
print(sum_of_two(2, 0), '\n')
print(sum_of_two(2, 0), '\n')

print(sum_of_two(4, 2), '\n')
print(sum_of_two(4, 2), '\n')

print(sum_of_two(5, 0), '\n')
print(sum_of_two(5, 0), '\n')
