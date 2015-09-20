#!/usr/bin/env python
from numpy.lib.function_base import average
import pygame, sys, random, time, math
from vector import Vector
from particle import Particle

from ocempgui.widgets import *
from ocempgui.widgets.components import TextListItem
from ocempgui.widgets.Constants import *

#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n = 10
startingvel = 2000
maxradius = 30
minradius = 20
maxpos = 500
zoomFactor = 2E+11
panPos = Vector(-650.0, -350.0, 0.0)
timeFactor = 2.0**-45
fusionLight = 0.0
panDirection = Vector (0.0, 0.0, 0.0)
zoomVel = 1.0
totalenergy = 0.0
maxScreenX=1300
maxScreenY=700
enableFusion = False

containerSize = Vector(1.0E-9, 1.0E-9, 1.0E-9)



heatMapSquareSideLength = 10

heatMapQuantityX = maxScreenX/heatMapSquareSideLength
heatMapQuantityY = maxScreenY/heatMapSquareSideLength



plist = []

for i in range (0,n):
    p1 = Particle()
    p1.mass = 1.6737236E-27   # Atomic mass of H(ydrogen) in kilos
    p1.pos = Vector(
        random.randint(0, 1E6)/1E6 * containerSize.x,
        random.randint(0, 1E6)/1E6 * containerSize.y)
    p1.vel = Vector(random.randint(0,startingvel), random.randint(0, startingvel))
    p1.radius = 5.3E-11  # Hydrogen atom radius in meters
    plist.append(p1)

"""
Physics debug settings:
plist[0].pos = Vector(400.0, 400.0, 0.0)
plist[1].pos = Vector(800.0, 400.0, 0.0)

plist[0].vel = Vector(40.0, 0.0, 0.0)
plist[1].vel = Vector(-40.0, 0.0, 0.0)

plist[0].mass = 100.0
plist[1].mass = 100.0
"""

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
tabgroup.set_padding(0)
tabgroup.set_spacing(0)

tab1 = VFrame()
allTabButtons = []
allTabs = []
activeTab = 0
def tabButnClicked(i):
    for j in range (0, len (allTabButtons)):
        allTabButtons [j].active   = (i == j)
    if activeTab != i:
        mainframe.remove_child(allTabs[activeTab])
        global activeTab
        activeTab = i
        mainframe.add_child (allTabs[activeTab])


for i in range (0, 5):
    tabButn = ToggleButton ("tab" + str(i + 1))
    tabgroup.add_child (tabButn)
    tabButn.connect_signal(SIG_TOGGLED,lambda j=i: tabButnClicked(j),)
    allTabButtons.append (tabButn)
mainframe.add_child(tabgroup)
allTabButtons [0].active = True
butn2 = Button ("Foo")
#butn.topleft = (maxScreenX - 180, 50)
def test():
    print "proteinbar"

tab1.add_child(butn2)
butn2.connect_signal(SIG_CLICKED,test,)

HMbutton = CheckButton ("Heat Map")
Fbutton = CheckButton ("Enable Fusion")
Fbutton.set_active(enableFusion)
#butn2.topleft = (maxScreenX - 180, 90)
def HMbuttonToggled():
    global heatMap
    heatMap = HMbutton.active
def FbuttonToggled():
    global enableFusion
    enableFusion = Fbutton.active


mainframe.add_child(tab1)
allTabs.append (tab1)

tab2 = VFrame()
tab2.add_child(HMbutton)
tab2.add_child(Fbutton)
HMbutton.connect_signal(SIG_TOGGLED,HMbuttonToggled,)
Fbutton.connect_signal(SIG_TOGGLED,FbuttonToggled,)
allTabs.append (tab2)
for i in range (0, 3):
    allTabs.append (VFrame())


gray = (64,64,64)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

heatMap = False
drawUi = False
t=time.time()
averageFps = 0.0
fusionCount = 0


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
        screen.fill((int(fusionLight), int(fusionLight), int(fusionLight)))

    fps = 1 / dt
    averageFps = (fps + (10*averageFps))/11
    label = myfont.render("FPS=" + str(int(averageFps)), 1, (255,255,0))
    screen.blit(label, (5, 5))

    label = myfont.render("N=" + str(int(n)), 1, (255,255,0))
    screen.blit(label, (5, 25))

    label = myfont.render("StartVel=" + str(int(startingvel)), 1, (255,255,0))
    screen.blit(label, (5, 45))

    label = myfont.render("TotalEnergy=" + str(totalenergy), 1, (255,255,0))
    screen.blit(label, (5, 145))

    label = myfont.render("MaxRadius=" + str(int(maxradius)), 1, (255,255,0))
    screen.blit(label, (5, 65))

    label = myfont.render("MinRadius=" + str(int(minradius)), 1, (255,255,0))
    screen.blit(label, (5, 85))

    label = myfont.render("Zoom=" + str(float(zoomFactor)), 1, (255,255,0))
    screen.blit(label, (5, 105))

    label = myfont.render("TimeFact.=" + str(float(timeFactor)), 1, (255,255,0))
    screen.blit(label, (5, 125))

    for i in range (0,n):
        plist[i].draw(screen, zoomFactor, panPos)

    for i in range (0,n):
        plist[i].movement(dt, timeFactor)
        plist[i].walls(containerSize.x, containerSize.y)
    fusionCount = 0
    for i in range (0, n):
        for j in range (i+1, n):
            pi = plist[i]
            pj = plist[j]
            if not pi.deleted and not pj.deleted:
                if Vector.dist(pi.pos, pj.pos) < pi.radius + pj.radius:
                    fused = Particle.Bounce(pi, pj, enableFusion)
                    if fused:
                        fusionCount = fusionCount + 1
    if fusionCount > 0:
        fusionLight = 255.0
    else:
        fusionLight = max(0, fusionLight - (dt*255/0.10)*timeFactor)


    "=-=-=-=-=-=-=-=-=-=-=-=-=-=  PLACEHOLDER FUSION ENERGY  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    EnergyReleased = fusionCount * 1e10
    "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    totalenergy = 0.0
    for i in range (0, n):
        pi = plist[i]
        kineticEnergy = pi.vel.len()**2 * pi.mass / 2
        kineticEnergy = kineticEnergy + EnergyReleased / n
        newVelocity = math.sqrt(2*kineticEnergy/pi.mass)
        pi.vel = (pi.vel * newVelocity / pi.vel.len())
        totalenergy = totalenergy + kineticEnergy

    panPos = panPos + panDirection * dt * 400
    zoomFactor = max(min(zoomFactor * (zoomVel**dt), 5E+20), 0.01)

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


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
           zoomVel = 5.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_EQUALS:
           zoomVel = 1


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
           zoomVel = 1 / 5.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_MINUS:
           zoomVel = 1





        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            panDirection.x = 1.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            panDirection.x = 0.0



        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            panDirection.x = -1.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            panDirection.x = 0.0


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            panDirection.y = -1.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            panDirection.y = 0.0



        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            panDirection.y = 1.0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            panDirection.y = 0.0



        elif event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
            timeFactor = min(timeFactor * 2, 2**8)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
            timeFactor = max(timeFactor / 2, 2.0**-75)
            #timeFactor = timeFactor - 1
        elif drawUi:
            gui.distribute_events((event))


