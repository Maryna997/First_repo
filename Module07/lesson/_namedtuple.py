from collections import namedtuple

# point = (0, 1, 3)
# x = point[0]
# y = point[1]      or x, y, z = point
# z = point[2]
# print(point[0], point[1], point[2])
# print(x, y, z)

Point = namedtuple("Point", ["x", "y", "z"])
print(Point)
point = Point(0, 1, 3)
print(point) 
print(point.x) 
print(point.y) 
print(point.z) 