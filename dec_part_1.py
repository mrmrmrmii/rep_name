from functools import wraps


def optional_introduce(func):

    def identity1(*args, **kwargs):
        if 'introduce' in kwargs.keys():
            if kwargs['introduce']:
                print(identity1.__name__)
        return func(*args)
    return identity1
