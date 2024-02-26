import pygame
from dataclasses import dataclass


@dataclass
class Square:
	"""Class to represent a square in the board"""
	x: int
	y: int
	color: tuple
	color_bottom: tuple
	window_size: tuple
	rect_square: pygame.Rect = None
	rect_bottom: pygame.Rect = None

	def create_surface(self):
		"""Create a surface for the square and set the rect"""
		ratio_x = self.window_size[0] // 1920
		ratio_y =  self.window_size[1] // 1080
		self.rect_square = pygame.Rect(self.x, self.y, 50 * ratio_x, 50 * ratio_y)
		self.rect_bottom = pygame.Rect(self.x, self.y + 50, 50, 20)

	def draw(self, screen: pygame.Surface):
		"""Draw the square on the screen"""
		pygame.draw.rect(screen, self.color, self.rect_square)
		pygame.draw.rect(screen, self.color_bottom, self.rect_bottom)
