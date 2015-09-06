import pygame
from vector import Vector
gray = (125,125,125)
darkGray = (25,25,25)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
colorNature = (0,160,0)
class Particle:
    def __init__(self):
        self.pos = Vector (0.0, 0.0, 0.0)
        self.vel = Vector (0.0, 0.0, 0.0)
        self.mass = 0.0
        self.radius = 1.0
        self.color = blue
        self.mass = 1.0
        self.deleted = False

    def draw(self, screen, zoomFactor, panPos):
        if self.deleted:
            self.color = darkGray
        drawPos = self.pos * zoomFactor - panPos
        pygame.draw.circle(
            screen,
            self.color,
            (int(drawPos.x), int(drawPos.y)),
            int(self.radius*zoomFactor),
            int(self.radius*zoomFactor/10.0)+1)

    "    TIME CONTROL   "
    def movement(self, dt):
        self.pos.x = self.pos.x+(self.vel.x*dt)/1.0
        self.pos.y = self.pos.y+(self.vel.y*dt)/1.0

    def walls(self, maxX, maxY):
        if self.pos.x < self.radius:
            self.vel.x = -self.vel.x
            self.pos.x = self.radius

        if self.pos.x > maxX-self.radius:
            self.vel.x = -self.vel.x
            self.pos.x = maxX-self.radius

        if self.pos.y < self.radius:
            self.vel.y = -self.vel.y
            self.pos.y = self.radius

        if self.pos.y > maxY-self.radius:
            self.vel.y = -self.vel.y
            self.pos.y = maxY-self.radius


    @staticmethod
    def Bounce(p1, p2):
        collisionVelocity = Vector.dotProduct(p1.vel - p2.vel , p1.pos - p2.pos)/ (Vector.len(p1.pos- p2.pos))
        collisionEnergy = ((collisionVelocity ** 2)*(p1.mass+p2.mass))/2
        if collisionVelocity < 0:
            # https://en.wikipedia.org/wiki/Elastic_collision
            v1 = p1.vel-(p1.pos-p2.pos) * Vector.dotProduct(p1.vel - p2.vel , p1.pos - p2.pos)/ (Vector.len(p1.pos- p2.pos)**2) * (2*p2.mass/(p1.mass+p2.mass))
            v2 = p2.vel-(p2.pos-p1.pos) * Vector.dotProduct(p2.vel - p1.vel , p2.pos - p1.pos)/ (Vector.len(p2.pos- p1.pos)**2) * (2*p1.mass/(p1.mass+p2.mass))

            p1.vel = v1
            p2.vel = v2
            print collisionEnergy, collisionVelocity
            if collisionEnergy > 1E9:
                p1.color = colorNature
                p2.color = colorNature
                p1.deleted = True
                p2.mass = p2.mass + p1.mass
                p2.radius = ((p1.radius**3) + (p2.radius**3)) ** (1.0/3.0)
                p2.vel = (p1.vel*p1.mass + p2.vel*p2.mass)/(p1.mass + p2.mass)
                p2.pos = (p1.pos + p2.pos)/2.0