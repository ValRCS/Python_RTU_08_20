from collections import namedtuple

# https://docs.python.org/3/library/collections.html#collections.namedtuple

Point = namedtuple('Point', ['x', 'y', 'description'])

p = Point(10,20,"Just some point")
print(p.x, p.y)
print(p[0], p[1])
print(p.description, p[2]) # so same decription

p1 = Point(3,6, "yet another one")
print(p1)