import math

class Point(object):

	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	def __str__(self):
		return str(self.x) + ', ' + str(self.y) + ', ' + str(self.z)

def cross(a, b):
	'''Returns the cross product of two vectors'''
	x = a.y * b.z - a.z * b.y
	y = a.z * b.x - a.x * b.z
	z = a.x * b.y - a.y * b.x
	return Point(x, y, z)

def sub(a, b):
	'''Subtracts two vectors'''
	return Point(a.x - b.x, a.y - b.y, a.z - b.z)

def dot(a, b):
	'''Returns the dot product of two vectors'''
	return (a.x * b.x + a.y * b.y + a.z * b.z)

def absv(a):
	'''Returns the absolute value of a vector'''
	return (a.x ** 2 + a.y ** 2 + a.z ** 2) ** 0.5

def torsional(X, Y):
	'''Returns the torsional angle of two vectors'''
	return math.degrees(math.acos(dot(X, Y) / (absv(X) * absv(Y))))

points = []

for i in range(0, 4):
	p = raw_input().strip().split()
	points.append(Point(p[0], p[1], p[2]))
    
a = points[0]
b = points[1]
c = points[2]
d = points[3]

AB = sub(a,b)
BC = sub(b,c)
CD = sub(c,d)

X = cross(AB, BC)
Y = cross(BC, CD)

print round(torsional(X, Y), 2)