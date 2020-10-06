class Particle:
	def __init__(self, pos):
		self.pos = pos

	# update particle's position and velocity
	def update(self, tiles, scale, width, height):
		# increase pos by vector on flow field
		self.pos = list(map(sum, zip(self.pos, tiles[int(self.pos[0]) // scale][int(self.pos[1]) // scale])))
		# edge cases
		self.pos[0] %= width
		self.pos[1] %= height
