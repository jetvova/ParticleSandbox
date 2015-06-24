#!/usr/bin/env python
import pygame, sys
from vector import Vector
from particle import Particle

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
p = Particle()
p.mass = 1.0
p.pos = Vector(100.0, 100.0)
p.vel = Vector(1.0, 0.9)
p.radius = 20.0
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
    pygame.draw.circle(screen, red, (int(p.pos.x),int(p.pos.y)), int(p.radius), int(p.radius/10))


    p.pos.x = p.pos.x+p.vel.x
    p.pos.y = p.pos.y+p.vel.y
    if p.pos.x < p.radius:
        p.vel.x = -p.vel.x
        p.pos.x = p.radius

    if p.pos.x > 600-p.radius:
        p.vel.x = -p.vel.x
        p.pos.x = 600-p.radius

    if p.pos.y < p.radius:
        p.vel.y = -p.vel.y
        p.pos.y = p.radius

    if p.pos.y > 600-p.radius:
        p.vel.y = -p.vel.y
        p.pos.y = 600-p.radius



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();