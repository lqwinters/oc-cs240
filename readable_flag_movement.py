## Author: Lindsey Winters
## Date: October 1, 2012
## Class: CS 240

## Description: This is a basic program of pygame where
## two Olympic flags move about the pale blue screen.
## Much easier to read since we import flag. Start of
## Class/Object.

import pygame
import flag

width, height = 640, 480

def init():
    pygame.init()

    # Screen size
    return pygame.display.set_mode((width, height))

def main(screen):

    flag1 = flag.Flag(0, 0)
    flag2 = flag.Flag(240, 240)

    running = True
    
    while running:
        pale_blue = pygame.Color('#87cefa')
        # Fills screen with pale blue color
        screen.fill (pale_blue)

        flag1.update(screen)          # Allows first Olympic flag momvement
        flag2.update(screen)          # Allows second Olympic flag movement

        # Draws an Olympic Flag
        flag1.draw(screen)            # Draws first Olympic flag
        flag2.draw(screen)            # Draws second Olympic flag
        # Flips to surface
        pygame.display.flip()

        # Exits program by hitting the 'x' or pushing q
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False 
            

screen = init()
main(screen)