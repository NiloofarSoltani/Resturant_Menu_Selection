class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p = Point(1, 10)
g = Point(2, 20)

print(p + g)
