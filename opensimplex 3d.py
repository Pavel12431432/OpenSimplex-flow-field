import pygame
from opensimplex import OpenSimplex
from random import randint

# define constants
WIDTH, HEIGHT = 600, 400
CURRENT = 0
SIZE = 10
ZOOM = 0.1
STEP = 0.03
# define noise object
noise = OpenSimplex(seed=randint(0, 100000000))

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('OpenSimplex 3d noise visualization')
clock = pygame.time.Clock()


def loop():
	global CURRENT, tiles
	screen.fill((0, 0, 0))
	for i in range(WIDTH // SIZE):
		for j in range(HEIGHT // SIZE):
			# draw each tile
			pygame.draw.rect(screen, (tiles[i][j], tiles[i][j], tiles[i][j]), ((i * SIZE, j * SIZE), (SIZE, SIZE)))
	# increase z axis counter
	CURRENT += STEP
	# update tiles
	tiles = gen_tiles()

	pygame.display.update()


# generate tiles from 3d simplex noise
def gen_tiles():
	return [[(noise.noise3d(i * ZOOM, j * ZOOM, CURRENT) + 1) * 127 for j in range(HEIGHT // SIZE)] for i in
			range(WIDTH // SIZE)]


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