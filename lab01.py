## Author: Lindsey Winters
## CLass: CS 240
## Date: September 19, 2012
## Assignment: Lab01
## Description: This is a basic program of pygame allowing the 
## display of a pale blue background, olympic flag, and the ability
## to quit/exit the program

## September 24, 2012: Added two images, soccer ball and USA Woman's soccer 
## photo. The two images rotate and move around the screen.


import pygame

width, height = 640, 480

def init():

    pygame.init()

    # Screen size
    width, height = 640, 480
    # Screen
    return pygame.display.set_mode((width, height))

def main(screen):

    # FLag size
    Flag_width, Flag_height = 360, 240
    Flag = pygame.Rect((width - Flag_width)/2, (height - Flag_height)/2, Flag_width, Flag_height)

    # Colors used in the flag
    pale_blue = pygame.Color('#87cefa')
    snow = pygame.Color('#fffafa')
    blue = pygame.Color('#0000cd')
    black = pygame.Color('#000000')
    red = pygame.Color('#ff0000')
    yellow = pygame.Color('#ffff00')
    green = pygame.Color('#008000')

    # Loads soccer ball image
    soccer = pygame.image.load("soccer-ball3.png").convert_alpha()
    soccer_rect = soccer.get_rect()

    # Loads USA Woman's soccer image
    usa = pygame.image.load("usa-soccer.jpg").convert_alpha()
    usa_rect = usa.get_rect()

    # Starting position of soccer ball image
    horizontal_1 = 4
    vertical_1 = 4
    # Starting position of USA Woman's soccer image
    horizontal_2 = 1
    vertical_2 = 1

    running = True

    while running:
        # Fills screen with pale blue color
        screen.fill (pale_blue)
          
        # Draws soccer ball image to screen
        screen.blit(soccer, soccer_rect)
        # Allows soccer ball image to rotate
        soccer = pygame.transform.rotate(soccer, 90)

        # Draws USA Woman's soccer image to screen
        screen.blit(usa, usa_rect)
        # Allows USA Woman's soccer image to rotate
        usa = pygame.transform.rotate(usa, 90)

        # Draws Olympic flag
        pygame.draw.rect(screen, snow, Flag)                            # Draws rectangle of flag
        pygame.draw.circle(screen, blue, (220,200), 65, 7)              # Draws blue ring
        pygame.draw.circle(screen, black, (320, 200), 65, 7)            # Draws black ring
        pygame.draw.circle(screen, red, (420, 200), 65, 7)              # Draws red ring
        pygame.draw.circle(screen, yellow, (270, 270), 65, 7)           # Draws yellow ring
        pygame.draw.circle(screen, green, (370, 270), 65, 7)            # Draws green ring
            
        # Displays screen in window
        pygame.display.flip()

        # Motion of both images
        soccer_rect.move_ip(horizontal_1, vertical_1)
        usa_rect.move_ip(horizontal_2, vertical_2)


        # Bounds checking
        if soccer_rect.right >= width or soccer_rect.left <= 0:
            horizontal_1 *= -1
        if soccer_rect.bottom >= height or soccer_rect.top <= 0:
            vertical_1 *= -1

        # Bounds checking
        if usa_rect.right >= width or usa_rect.left <= 0:
            horizontal_2 *= -1
        if usa_rect.bottom >= height or usa_rect.top <= 0:
            vertical_2 *= -1


        # Allows user to quit by pressing the X button or by pressing 'q' on the keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.k_q):         
                running = False    

screen = init()
main(screen)                                                                                                                         
