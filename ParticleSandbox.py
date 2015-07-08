#!/usr/bin/env python
from numpy.lib.function_base import average
import pygame, sys, random, time
from vector import Vector
from particle import Particle

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 200
plist = []

for i in range (0,n):
    p1 = Particle()
    p1.mass = 1.0
    p1.pos = Vector(100.0, 100.0)
    p1.vel = Vector(random.randint(0,1000)/5.0, random.randint(0, 1000)/5.0)
    p1.radius = random.randint(1, 20)
    plist.append(p1)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



#================================================


pygame.init()
screen = pygame.display.set_mode((600, 600))
myfont = pygame.font.SysFont("monospace", 20)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

t=time.time()
averageFps = 0.0

while True:
    dt = time.time() - t
    t = time.time()

    screen.fill(black)
    fps = 1 / dt
    averageFps = (fps + (10*averageFps))/11
    label = myfont.render("FPS=" + str(int(averageFps)), 1, (255,255,0))
    screen.blit(label, (5, 5))

    for i in range (0,n):
        plist[i].draw(screen)

    for i in range (0,n):
        plist[i].movement(dt)
        plist[i].walls()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


