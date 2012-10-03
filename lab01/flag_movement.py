## Author: Lindsey Winters
## Date: October 1, 2012
## Class: CS 240

## Description: This is a basic program of pygame where
## two Olympic flags move about the pale blue screen.


import pygame

width, height = 640, 480

def init():
    pygame.init()

    # Screen size
    return pygame.display.set_mode((width, height))

def draw_flag(screen, left, top, width, height):
    # Colors used in the flag
    snow = pygame.Color('#fffafa')
    blue = pygame.Color('#0000cd')
    black = pygame.Color('#000000')
    red = pygame.Color('#ff0000')
    yellow = pygame.Color('#ffff00')
    green = pygame.Color('#008000')

    # Draws Olympic flag
    pygame.draw.rect(screen, snow, (left, top, width, height))                # Draws rectangle of flag
    pygame.draw.circle(screen, blue, (left + 100, top + 80), 65, 7)           # Draws blue ring
    pygame.draw.circle(screen, black, (left + 200, top + 80), 65, 7)          # Draws black ring
    pygame.draw.circle(screen, red, (left + 300, top + 80), 65, 7)            # Draws red ring
    pygame.draw.circle(screen, yellow, (left + 150, top + 150), 65, 7)        # Draws yellow ring
    pygame.draw.circle(screen, green, (left + 250, top + 150), 65, 7)         # Draws green ring

def main(screen):
    horizontal, vertical = 0, 1
    fleft, ftop = 0, 0

    # FLag size
    Flag_width, Flag_height = 360, 240
    Flag = pygame.Rect((width - Flag_width)/2, (height - Flag_height)/2, Flag_width, Flag_height)

    running = True

    while running:

        # Fills screen with pale blue color
        pale_blue = pygame.Color('#87cefa')
        screen.fill (pale_blue)

        # Drawing
        draw_flag(screen, fleft, ftop, 400, 240)
        draw_flag(screen, width - fleft - 400, height - ftop - 240, 400, 240)
        # Flips to the surface
        pygame.display.flip()

        # Bounds checking
        fright = fleft + 400
        fbottom = ftop + 240
        if fright <= width and fleft >= 0:
            fleft += horizontal
        else:
            horizontal = -horizontal
            fleft += horizontal

        if fbottom <= height and ftop >= 0:
            ftop += vertical
        else:
            vertical = -vertical
            ftop += vertical

        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.k_q):         
                running = False    
            if event.type == pygame.KEYDOWN and event.key == pygame.k_z:         
                fleft, ftop = 0, 0
        
        print fleft, ftop, horizontal, vertical

screen = init()
main(screen)


    