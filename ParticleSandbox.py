#!/usr/bin/env python
from numpy.lib.function_base import average
import pygame, sys, random, time, math
from vector import Vector
from particle import Particle

from ocempgui.widgets import *
from ocempgui.widgets.components import TextListItem
from ocempgui.widgets.Constants import *

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 4
totalvel = 1000
maxradius = 30
minradius = 10
maxpos = 500

maxScreenX=1300
maxScreenY=700

heatMapSquareSideLength = 10

heatMapQuantityX = maxScreenX/heatMapSquareSideLength
heatMapQuantityY = maxScreenY/heatMapSquareSideLength



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


pygame.init()
screen = pygame.display.set_mode((maxScreenX, maxScreenY))
myfont = pygame.font.SysFont("monospace", 20)

gui = Renderer()
gui.screen = screen

uiWidth = 200
tab = 1

mainframe = VFrame()
mainframe.set_position(maxScreenX-uiWidth,0)
mainframe.set_size(uiWidth,maxScreenY)
gui.add_widget (mainframe)

tabgroup = HFrame()
mainframe.add_child(tabgroup)
tabgroup.set_padding(0)
tabgroup.set_spacing(0)

tab1 = VFrame()

butn = ToggleButton ("tab1")
#butn.topleft = (maxScreenX - 200, 1)
def test3():
    global tab1
    tab1 = 2
tabgroup.add_child (butn)
butn.connect_signal(SIG_CLICKED,test3,)

tabgroup.add_child(ToggleButton("tab2"))
tabgroup.add_child(ToggleButton("tab3"))
tabgroup.add_child(ToggleButton("tab4"))
tabgroup.add_child(ToggleButton("tab5"))

butn = Button ("Foo")
#butn.topleft = (maxScreenX - 180, 50)
def test():
    print ("proteinbar")
tab1.add_child(butn)
butn.connect_signal(SIG_CLICKED,test,)

HMbutton = CheckButton ("HM")
#butn2.topleft = (maxScreenX - 180, 90)
def HMbuttonToggled():
    global heatMap
    heatMap = HMbutton.active
tab1.add_child(HMbutton)
HMbutton.connect_signal(SIG_TOGGLED,HMbuttonToggled,)
mainframe.add_child(tab1)






gray = (64,64,64)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

heatMap = False
drawUi = True
t=time.time()
averageFps = 0.0

while True:
    now = time.time()
    dt = now - t
    t = now



    if heatMap:
        for i in range (0,heatMapQuantityX):
            for j in range (0,heatMapQuantityY):
                squareCenterPosition = Vector((i+0.5)*heatMapSquareSideLength,(j+0.5)*heatMapSquareSideLength,0.0)

                gravity = Vector(0.0, 0.0, 0.0)

                for k in range (0, n):
                    distVector = squareCenterPosition - plist[k].pos
                    dist = Vector.len(distVector)
                    partialGravity = (distVector/dist) * (plist[k].mass/(dist**2))
                    gravity = gravity + partialGravity

                # Calculates hetamapsquare color
                c = int(Vector.len(gravity)*50)
                if c > 255:
                    c = 255
                if (c % 2) != 0:
                    c = 0
                #c = int((math.sin(5/Vector.len(gravity)) + 1)*126)

                pygame.draw.rect (screen, (c,0,0), (i*heatMapSquareSideLength,j*heatMapSquareSideLength,heatMapSquareSideLength,heatMapSquareSideLength))
    else:
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

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
           heatMap = not heatMap

        elif drawUi:
            gui.distribute_events((event))


