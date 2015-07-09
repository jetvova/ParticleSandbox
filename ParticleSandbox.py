#!/usr/bin/env python
from numpy.lib.function_base import average
import pygame, sys, random, time, math
from vector import Vector
from particle import Particle

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 20
plist = []

for i in range (0,n):
    p1 = Particle()
    p1.mass = 1.0
    p1.pos = Vector(float(random.randint(20, 500)), float(random.randint(20, 500)))
    p1.vel = Vector(random.randint(0,2000)/5.0, random.randint(0, 2000)/5.0)
    p1.radius = random.randint(1, 5)
    plist.append(p1)


def dist(v1,v2):
    return math.sqrt( (v1.x - v2.x)**2 + (v1.y - v2.y)**2 )

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
    now = time.time()
    dt = now - t
    t = now

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

    for i in range (0, n):
        for j in range (i+1, n):
            pi = plist[i]
            pj = plist[j]
            if dist(pi.pos, pj.pos) < pi.radius + pj.radius:
                pi.collision()
                pj.collision()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


