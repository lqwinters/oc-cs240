## Author: Lindsey Winters
## Date: October 1, 2012
## Class: CS 240

## Description: Olympic flag is created here and imported into 
## readable_flag_movement. This is the class/object file for the Olymppic 
## flag.

import pygame

class Flag(object):
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.horizontal = 0
        self.vertical = 1
        self.width = 400
        self.height = 240

        
    def draw(self, screen):
        # Colors used in the flag
        snow = pygame.Color('#fffafa')
        blue = pygame.Color('#0000cd')
        black = pygame.Color('#000000')
        red = pygame.Color('#ff0000')
        yellow = pygame.Color('#ffff00')
        green = pygame.Color('#008000')

        # Draws Olympic flag
        pygame.draw.rect(screen, snow, (self.left, self.top, self.width, self.height) )     # Draws rectangle of flag
        pygame.draw.circle(screen, blue, (self.left + 100, self.top + 80), 65, 7)           # Draws blue ring
        pygame.draw.circle(screen, black, (self.left + 200, self.top + 80), 65, 7)          # Draws black ring
        pygame.draw.circle(screen, red, (self.left + 300, self.top + 80), 65, 7)            # Draws red ring
        pygame.draw.circle(screen, yellow, (self.left + 150, self.top + 150), 65, 7)        # Draws yellow ring
        pygame.draw.circle(screen, green, (self.left + 250, self.top + 150), 65, 7)         # Draws green ring
    
    def update(self, screen):
        screen_width, screen_height = screen.get_size()
        
        # Bounds checking
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        
        # Allows flag to move down and then right to left 
        if self.right > screen_width: 
            self.left -= 1              # Moves flag one pixel to the left
            self.horizontal = 0         # Moves flag up
            self.vertical = -1
        else:
            self.left += self.horizontal
            
        # Allows flag to move right        
        if self.left <= 0:
            self.horizontal = 0
            self.vertical = 1
        else:
            self.left += self.horizontal

        # Allows flag to move bottom to top and then left to right
        if self.bottom > screen_height:
            self.top -= 1                   # Moves flag one pixel down
            self.vertical = 0               # Moves flag left
            self.horizontal = 1
        else:
            self.top += self.vertical

        # Allows flag to move left
        if self.top <= 0:
            self.horizontal = -1 
            self.vertical = 0
        else: 
            self.top += self.vertical

        