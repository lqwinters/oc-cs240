## Lindsey Winters
## CS 240
## September 19, 2012
## Lab01

import pygame

pygame.init ( ) 

# Screen size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Location and colors used in the flag
Flag = pygame.Rect((150,120),(360,240))
pale_blue = pygame.Color('#87cefa')
grey = pygame.Color('#dcdcdc')
blue = pygame.Color('#0000cd')
black = pygame.Color('#000000')
red = pygame.Color('#ff0000')
yellow = pygame.Color('#ffff00')
green = pygame.Color('#008000')

running = True
while running:
    # Draw an olympic flag on a pale blue background
    screen.fill (pale_blue)
    # screen.fill (grey, Flag) can use to fill rectangle but harder to understand

    pygame.draw.rect(screen, grey, Flag)                            # Draws grey rectangle
    pygame.draw.circle(screen, blue, (230,200), 65, 7)              # Draws blue ring
    pygame.draw.circle(screen, black, (330, 200), 65, 7)            # Draws black ring
    pygame.draw.circle(screen, red, (430, 200), 65, 7)              # Draws red ring
    pygame.draw.circle(screen, yellow, (280, 270), 65, 7)           # Draws yellow ring
    pygame.draw.circle(screen, green, (380, 270), 65, 7)            # Draws green ring
    
    # Display screen in window
    pygame.display.flip()

    # Allows user to quit by pressing the X button or by pressing 'q' on the keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.k_q):         
            running = False                                                                                                                             
