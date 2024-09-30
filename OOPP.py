class Point:
    def __init__(self, x, y, color="Black"):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return self.x, self.y, self.color

d = [Point(2 * i + 1, 2 * i) for i in range(0,1000)]
print(d)
