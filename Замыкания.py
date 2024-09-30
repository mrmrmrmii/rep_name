def print_given():
    def inner(*args, **kwargs):
        for i in args:
            print(i ,end=' ')
            print(type(i))
        for k, v in kwargs.items():
            print(k, v, type(kwargs))
        return
    return inner
c = print_given()
c(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
