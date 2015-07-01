#!/usr/bin/env python
import pygame, sys, random
from vector import Vector
from particle import Particle

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 100
plist = []

for i in range (0,n):
    p1 = Particle()
    p1.mass = 1.0
    p1.pos = Vector(100.0, 100.0)
    p1.vel = Vector(random.randint(0,1000)/1000.0, random.randint(0, 1000)/1000.0)
    p1.radius = random.randint(1, 20)
    plist.append(p1)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



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

    for i in range (0,n):
        plist[i].draw(screen)

    for i in range (0,n):
        plist[i].movement()
        plist[i].walls()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


