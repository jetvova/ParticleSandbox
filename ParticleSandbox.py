#!/usr/bin/env python
from numpy.lib.function_base import average
import pygame, sys, random, time, math
from vector import Vector
from particle import Particle

from ocempgui.widgets import *
from ocempgui.widgets.components import TextListItem
from ocempgui.widgets.Constants import *

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 20
totalvel = 9000
maxradius = 10
minradius = 5
maxpos = 500

plist = []

for i in range (0,n):
    p1 = Particle()
    p1.mass = 1.0
    p1.pos = Vector(float(random.randint(20, maxpos)), float(random.randint(20, maxpos)))
    p1.vel = Vector(random.randint(0,totalvel)/5.0, random.randint(0, totalvel)/5.0)
    p1.radius = float(random.randint(minradius, maxradius))
    p1.mass = p1.radius**3
    plist.append(p1)




#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



#================================================
maxScreenX=1000
maxScreenY=700

pygame.init()
screen = pygame.display.set_mode((maxScreenX, maxScreenY))
myfont = pygame.font.SysFont("monospace", 20)

gui = Renderer()
gui.screen = screen

uiWidth = 100
butn = Button ("Foo")
butn.topleft = (maxScreenX - 60, 10)
def test():
    print ("proteinbar")
gui.add_widget (butn)
butn.connect_signal(SIG_CLICKED,test,)


gray = (64,64,64)
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

    label = myfont.render("N=" + str(int(n)), 1, (255,255,0))
    screen.blit(label, (5, 25))

    label = myfont.render("TotalVel=" + str(int(totalvel)), 1, (255,255,0))
    screen.blit(label, (5, 45))

    label = myfont.render("MaxRadius=" + str(int(maxradius)), 1, (255,255,0))
    screen.blit(label, (5, 65))

    label = myfont.render("MinRadius=" + str(int(minradius)), 1, (255,255,0))
    screen.blit(label, (5, 85))


    for i in range (0,n):
        plist[i].draw(screen)

    for i in range (0,n):
        plist[i].movement(dt)
        plist[i].walls(maxScreenX, maxScreenY)

    for i in range (0, n):
        for j in range (i+1, n):
            pi = plist[i]
            pj = plist[j]
            if not pi.deleted and not pj.deleted:
                if Vector.dist(pi.pos, pj.pos) < pi.radius + pj.radius:
                    Particle.Bounce(pi, pj)
    i = 0
    while i < n:
        if plist[i].deleted:
            del plist[i]
            n = n - 1
        i = i + 1

    if drawUi == True:
        rect = pygame.Surface((uiWidth,maxScreenY), pygame.SRCALPHA, 32)
        rect.fill((23, 100, 255, 50))
        screen.blit(rect, (maxScreenX - uiWidth,0))
        gui.update()
        gui.refresh()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSLASH:
           drawUi = not drawUi
        elif drawUi:
            gui.distribute_events((event))

