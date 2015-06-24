from vector import Vector
class Particle:
    def __init__(self):
        self.pos = Vector (0.0, 0.0, 0.0)
        self.vel = Vector (0.0, 0.0, 0.0)
        self.mass = 0.0
        self.radius = 1.0