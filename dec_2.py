from functools import wraps
def bucket(*args1, **kwargs1):
    def bucket1(func):
        @wraps(func)
        def identity(*args, **kwargs):
            print((args1, kwargs1))
            #print((args, kwargs))
            return func(*args, **kwargs)
        return identity
    return bucket1
@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
def identity(x):
  return x
print(identity(42))
