# WE USE NAMED TUPLE WHEN WE HAVE TO DECLARE A CLASS WHICH DO NOTHING
# THAT IS WE REPLACE  A CLASS(WITHOUT ANY FUNCTION) WITH NAMEDTUPLE

# class Point:
#     def __init__(self, x, y):  # MAGIC METHOD
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)

# INSTAED OF DOING ALL THIS WE CAN DO

from collections import namedtuple

Stream = namedtuple("Stream", ["x", "y"])

p1 = Stream(x=1, y=2)

p2 = Stream(x=1, y=2)

print(p1 == p2)
