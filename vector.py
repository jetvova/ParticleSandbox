import math
class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "("+str(self.x) +", "+ str(self.y) +", "+ str(self.z)+")"

    @staticmethod
    def dist(v1, v2):
        return math.sqrt( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2 )

    def __sub__(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

    def __add__(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


    def __mul__(v, n):
        return Vector(v.x * n, v.y * n, v.z * n)


    def __div__(v, n):
        return Vector(v.x / n, v.y / n, v.z / n)

    @staticmethod
    def dotProduct(v1, v2):
        return (v1.x*v2.x)+(v1.y*v2.y)+(v1.z*v2.z)







