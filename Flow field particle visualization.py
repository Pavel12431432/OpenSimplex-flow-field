from math import pi
from random import randint

import numpy as np
import pygame
from opensimplex import OpenSimplex

from particle import Particle

# define constants
WIDTH, HEIGHT = 800, 600
SCALE = 25
ZOOM = 0.1
STEP = 0.01
BRIGHTNESS = 200
SPEED = 1
COLOR = (200, 200, 200)
PARTICLE_COUNT = 30
# define noise object
NOISE = OpenSimplex(seed=randint(0, 1000000))

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Flow field particle visualization')
clock = pygame.time.Clock()


def loop():
	global CURRENT, tiles
	for particle in particles:
		# create new pygame surface to draw onto because drawing doesnt support rgba
		surf = pygame.Surface((100, 100))
		surf.set_colorkey((0, 0, 0))
		# set alpha value
		surf.set_alpha(BRIGHTNESS)
		# draw pixel
		pygame.draw.rect(surf, COLOR, ((0, 0), (0, 0)))
		# draw surface onto screen
		screen.blit(surf, surf.get_rect(topleft=tuple(map(int, particle.pos))))

		# update particle
		particle.update(tiles, SCALE, WIDTH, HEIGHT)

	# increase z axis counter
	CURRENT += STEP
	# update flow field
	tiles = gen_tiles()

	pygame.display.update()


# generate flow field
def gen_tiles():
	return [[get_vector(NOISE.noise3d(i * ZOOM, j * ZOOM, CURRENT) * pi) for j in range(HEIGHT // SCALE)] for i in
			range(WIDTH // SCALE)]


# get vector based on angle
def get_vector(angle):
	return np.cos(angle) * SPEED, np.sin(angle) * SPEED


# handle input
def inp():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


CURRENT = 0
tiles = gen_tiles()
particles = [Particle((randint(0, WIDTH), randint(0, HEIGHT))) for i in range(PARTICLE_COUNT)]

# main loop
while True:
	inp()
	loop()
	clock.tick(100)
