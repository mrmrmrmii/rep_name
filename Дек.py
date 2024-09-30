
from functools import wraps, partial

def bucket(func = None, **bkwargs ):
    if func is None:
        return partial(bucket, **bkwargs)
    else:
        @wraps(func)
        def f(*args,**kwargs):
            return func(*args,**kwargs)
        return f

bucket(one = 1, two = 2, three = 3)
def identity(x):
  return x

#print(identity(42))
