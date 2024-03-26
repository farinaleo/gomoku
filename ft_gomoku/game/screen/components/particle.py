import pygame
from random import randint, choice, uniform


class Particle(pygame.sprite.Sprite):
	def __init__(self, groups: pygame.sprite.Group, pos: tuple[int, int], color: str, direction: pygame.math.Vector2):
		super().__init__(groups)
		self.pos = pos
		self.color = color
		self.direction = direction
		self.image = None
		self.rect = None
		self.alpha = 255
		self.create_surface()

	def create_surface(self):
		"""Create a surface for the particle and set the rect"""
		self.image = pygame.Surface((4, 4)).convert_alpha()
		self.image.set_colorkey((8, 26, 43))
		pygame.draw.circle(surface=self.image, color=self.color, center=(2, 2), radius=2)
		self.rect = self.image.get_rect(center=self.pos)

	def move(self):
		"""Move the particle in the direction and reduce the alpha"""
		self.pos += self.direction
		if self.alpha < 255 or randint(1, 50) == 1:
			if self.alpha == 0:
				self.kill()
			self.alpha -= 5
		self.rect.center = self.pos

	def update(self):
		self.move()
		self.image.set_alpha(self.alpha)


def stars_effect(max_stars: int, max_width: int, max_height: int, group: pygame.sprite.Group):
	"""Create stars effect on the screen
	:param max_stars: maximum number of stars on the screen
	:param max_width: maximum width of the screen
	:param max_height: maximum height of the screen
	:param group: group to add the stars to
	"""
	num_sprites = len(group.sprites())
	if num_sprites < max_stars:
		Particle(group, (randint(0, max_width), randint(0, max_height)), choice(("white", "yellow")), pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1)))
