import random
from math import pi
from particle import Particle
import numpy as np
import pygame
from opensimplex import OpenSimplex

# define constants
WIDTH, HEIGHT = 800, 600
CURRENT = 0
SCALE = 25
ZOOM = 0.1
STEP = 0.015
# define noise object
NOISE = OpenSimplex(seed=random.randint(0, 100000000000))

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flow field single particle')
clock = pygame.time.Clock()


def loop():
	global CURRENT, tiles
	screen.fill((0, 0, 0))
	for i in range(WIDTH // SCALE):
		for j in range(HEIGHT // SCALE):
			# draw each vector
			pygame.draw.line(screen, (255, 255, 255), (i * SCALE, j * SCALE),
							 tuple(map(sum, zip(tuple(map(lambda x: x * SCALE, tiles[i][j])), (i * SCALE, j * SCALE)))))

	# update particle pos
	particle.update(tiles, SCALE, WIDTH, HEIGHT)
	# draw particle
	pygame.draw.circle(screen, (40, 200, 40), tuple(map(int, particle.pos)), 10)

	# update flow field
	tiles = gen_tiles()
	# increase z axis counter
	CURRENT += STEP

	pygame.display.update()


# generate flow field
def gen_tiles():
	return [[get_vector(NOISE.noise3d(i * ZOOM, j * ZOOM, CURRENT) * pi) for j in range(HEIGHT // SCALE)] for i in
			range(WIDTH // SCALE)]


# get vector from angle
def get_vector(angle):
	return np.cos(angle), np.sin(angle)


# handle input
def inp():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


tiles = gen_tiles()
particle = Particle((400, 300))

while True:
	inp()
	loop()
	clock.tick(60)
