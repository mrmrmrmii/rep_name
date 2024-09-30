from functools import partial
def ran(min, max, step):
    a = []
    for i in range(min, max, step):
        a.append(i)
    return a



con_class = partial(ran,0, 101)

print((con_class(2)))
