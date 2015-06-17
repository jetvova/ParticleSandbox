#!/usr/bin/env python
import pygame, sys
from vector import Vector


#IMPORTANT VARIABLES=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
position = Vector(100.0, 100.0)

velocity = Vector(1.0, 0.9)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#NONIMPORTANT VARIABLES==========================


r=20
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

    pygame.draw.circle(screen, red, (int(position.x),int(position.y)), r, r/10)
    position.x = position.x+-velocity.x
    position.y = position.y+velocity.y
    if position.x < r:
        velocity.x = -velocity.x
        position.x = r

    if position.x > 600-r:
        velocity.x = -velocity.x
        position.x = 600-r

    if position.y < r:
        velocity.y = -velocity.y
        position.y = r

    if position.y > 600-r:
        velocity.y = -velocity.y
        position.y = 600-r



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();