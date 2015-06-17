#!/usr/bin/env python
import pygame, sys
from vector import Vector


#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
position = Vector(300.0, 300.0)

velocity = Vector(0.05, 0.05)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#NONIMPORTANT VARIABLES==========================


r=20
#================================================


pygame.init()
screen = pygame.display.set_mode((460, 480))


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)



while True:
    screen.fill(black)

    pygame.draw.circle(screen, red, (int(position.x),int(position.y)), r, r/10)
    position.x = position.x+velocity.x
    position.y = position.y+velocity.y

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();