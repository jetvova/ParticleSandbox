import pygame
from vector import Vector

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

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x),int(self.pos.y)), int(self.radius), int(self.radius/10.0)+1)

    def movement(self, dt):
        self.pos.x = self.pos.x+(self.vel.x*dt)
        self.pos.y = self.pos.y+(self.vel.y*dt)

    def walls(self):
        if self.pos.x < self.radius:
            self.vel.x = -self.vel.x
            self.pos.x = self.radius

        if self.pos.x > 600-self.radius:
            self.vel.x = -self.vel.x
            self.pos.x = 600-self.radius

        if self.pos.y < self.radius:
            self.vel.y = -self.vel.y
            self.pos.y = self.radius

        if self.pos.y > 600-self.radius:
            self.vel.y = -self.vel.y
            self.pos.y = 600-self.radius

    def collision(self):
        self.vel = Vector(0.0, 0.0, 0.0)
        self.color = colorNature

