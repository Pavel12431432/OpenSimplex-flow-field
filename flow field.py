import pygame
from opensimplex import OpenSimplex
import random
from math import pi
import numpy as np

# define constants
WIDTH, HEIGHT = 600, 400
CURRENT = 0
SIZE = 10
ZOOM = 0.1
STEP = 0.03
# define noise object
noise = OpenSimplex(seed=random.randint(0, 1000000))

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flow field')
clock = pygame.time.Clock()


def loop():
	global CURRENT, tiles
	screen.fill((0, 0, 0))
	for i in range(WIDTH // SIZE):
		for j in range(HEIGHT // SIZE):
			# draw each vector
			pygame.draw.line(screen, (255, 255, 255), (i * SIZE, j * SIZE),
							 tuple(map(sum, zip(tiles[i][j], (i * SIZE, j * SIZE)))))
	# update flow field
	tiles = gen_tiles()
	# increase z axis counter
	CURRENT += STEP
	pygame.display.update()


# generate flow field
def gen_tiles():
	return [[get_vector(noise.noise3d(i * ZOOM, j * ZOOM, CURRENT) * pi) for j in range(HEIGHT // SIZE)] for i in
			range(WIDTH // SIZE)]


# get vector from angle
def get_vector(angle):
	return np.cos(angle) * SIZE, np.sin(angle) * SIZE


# handle input
def inp():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


tiles = gen_tiles()

while True:
	inp()
	loop()
	clock.tick(60)
