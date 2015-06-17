#!/usr/bin/env python
import pygame, sys








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

    pygame.draw.circle(screen, red, (300,300), 20, 5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();