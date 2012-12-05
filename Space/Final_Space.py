## Author: Lindsey Winters
## Date: October 22, 2012
## Description: Another pygame program. Creating space and adding 
## a space ship image. Space ship image displays engines changing and 
## displays the chop image resutlting in ship being displayed.  
## Ship is able to move with up, down, left and right keys. Ship
## stops moving with space bar. Loaded a princess character.


import random
import pygame

class NewShip(object):
    def __init__(self):
        self.image = pygame.image.load('ship.png').convert()
        self.x = 400
        self.y = 20
        self.size = self.image.get_size()
        colorkey = self.image.get_at((self.size[0] - 1, self.size[1] -1))
        self.frame = 0
        self.y_velocity = 0
        self.x_velocity = 0

        # Hunting for the width of engine parts
        for i in range(self.size[0]):
            color = self.image.get_at((i, 0))
            if color == colorkey:
                break
        width = i

        # Hunting for the height of engine parts
        for i in range(self.size[1]):
            color = self.image.get_at((0, i))
            if color == colorkey:
                break
        height = i

        self.engines = self.image.subsurface((0, 0, width, height)).copy()

        # Finding the horizontal location of engine gap
        seen_ck = False
        past_grid = False
        for i in range(self.size[0]):
            color = self.image.get_at((i, 50))
            if color == colorkey:
                seen_ck = True
                if past_grid:
                    break

            if color != colorkey and seen_ck:
                past_grid = True
        gap_x = i

        # Finding the vertical location of engine gap
        seen_ship = False
        for i in range(self.size[1]):
            color = self.image.get_at((gap_x + 1, i))
            if color != colorkey:
                seen_ship = True
            if color == colorkey and seen_ship:
                break
        gap_y = i

        # Chops entire ship imgae to just display ship with engines
        self.image = self.image.subsurface((111, 0, self.size[0] / 2, self.size[1] / 2))

        # Makes ship image trasnparent, getting rid of green background color
        self.image.set_colorkey(colorkey)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        engine_part = self.frame / 20
        width = 24
        height = 28
        row = engine_part / 4 * height
        col = (engine_part % 4) * width
        engine = self.engines.subsurface((col, row, width, height))

        gap_x, gap_y = 45, 28
        self.image.blit(engine, (gap_x, gap_y))

        self.frame = (self.frame + 1) % 160

        self.y += self.y_velocity
        if self.y > screen.get_height() and self.y_velocity > 0:
            self.y = -self.image.get_height() + 70   # -101
        if self.y < -self.image.get_height() and self.y_velocity < 0:
            self.y = screen.get_height() - 70

        self.x += self.x_velocity
        if self.x > screen.get_width() and self.x_velocity > 0:
            self.x = -self.image.get_width() + 70   # -101
        if self.x < -self.image.get_width() and self.x_velocity < 0:
            self.x = screen.get_width() - 70

        return
        d = random.randint(1, 8)
        if d < 5:
            self.x += 2
        else:
            self.x += -2
        self.y += 1

    def move_down(self):
        self.y_velocity = 1
        self.x_velocity = 0

    def move_right(self):
        self.x_velocity = 1
        self.y_velocity = 0

    def move_left(self):
        self.x_velocity = -1
        self.y_velocity = 0

    def move_up(self):
        self.y_velocity = -1
        self.x_velocity = 0
    def stop(self):
        self.y_velocity = 0
        self.x_velocity = 0

def init():
    width, height = 800, 600
    pygame.init()
    # Screen
    return pygame.display.set_mode((width, height))


def draw_space(surface, stars):
	surface.fill((0, 0, 0)) 			# Draw the vacuum of space
	for s in stars:
		if s[2] == 3:
			star = pygame.Color(255, 255, 255)
		elif s[2] == 2:
			star = pygame.Color(200, 200, 255) 
		elif s[2] == 1:
			star = pygame.Color(255, 170, 170)
		pygame.draw.circle(surface, star, s[:2], s[2])


def build_space(screen):
	# Get a new surface and its parameters
	space = screen.copy()
	width, height = screen.get_size()

	stars = []
	for star in range(60):
		x = random.randint(0, width)
		y = random.randint(0, height)
		rand = random.randint(1, 10)
		if rand <= 6:
			r = 1
		elif rand <= 9:
			r = 2
		else:
			r = 3
		stars.append((x, y, r))

	draw_space(space, stars)
	return space

def load_character():
	character = pygame.image.load('Character Princess Girl.png').convert_alpha()
	raw_size = character.get_size()

	return character

def main(screen):
    ship = NewShip()
    character = load_character()
    space = build_space(screen)
    running = True
    while running:
        screen.blit(space, (0, 0))          # Redraw background
        ship.draw(screen)
        ship.update()
        screen.blit(character, (350, 170))
        pygame.display.flip()           # Display screen in window

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ship.move_down()
                if event.key == pygame.K_UP:
                    ship.move_up()
                if event.key == pygame.K_LEFT:
                    ship.move_left()
                if event.key == pygame.K_RIGHT:
                    ship.move_right()
                if event.key == pygame.K_SPACE:
                    ship.stop()


screen = init()
main(screen)