from collections import namedtuple

point = namedtuple('Point','x,y') #create class names Point and fields x & y

pt = point(1,-1)
pt1 = point(0,0)

print(pt.x, pt.y)
print(pt)