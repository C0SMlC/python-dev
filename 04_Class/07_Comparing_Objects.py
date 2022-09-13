class Point:
    def __init__(self, x, y):  # MAGIC METHOD
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y+other.y)

    def __str__(self):   # MAGIC METHOD
        return f"({self.x},{self.y})"


point = Point(1, 2)
other = Point(1, 4)
# print(point == other)
# print(point > other)
# print(point < other)
# add = point + other
# print(add)
print((point))
