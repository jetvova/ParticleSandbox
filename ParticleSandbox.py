#!/usr/bin/env python
import pygame, sys
from vector import Vector
from particle import Particle

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
p1 = Particle()
p1.mass = 1.0
p1.pos = Vector(100.0, 100.0)
p1.vel = Vector(1.0, 0.9)
p1.radius = 20.0
p2 = Particle()
p2.mass = 1.0
p2.pos = Vector(100.0, 100.0)
p2.vel = Vector(-1.0, -0.9)
p2.radius = 20.0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#NONIMPORTANT VARIABLES==========================



#================================================


pygame.init()
screen = pygame.display.set_mode((600, 600))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


while True:
    screen.fill(black)
    p1.draw(screen)
    p2.draw(screen)

    p1.movement()
    p1.walls()
    p2.movement()
    p2.walls()




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();