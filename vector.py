import math
class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dist(v1, v2):
        return math.sqrt( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2 )

