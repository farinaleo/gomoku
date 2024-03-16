import pygame
from dataclasses import dataclass


@dataclass
class Square:
	"""Class to represent a square in the board"""
	x: int
	y: int
	window_size: tuple
	square_id: int
	square_size: int
	square_surface: pygame.Surface = None
	bottom_surface: pygame.Surface = None
	rect_square: pygame.Rect = None
	rect_bottom: pygame.Rect = None

	def create_surface(self):
		"""Create surface and rect for the square and bottom"""
		color_square = (10, 130, 141) if self.square_id % 2 == 0 else (12, 154, 165)
		color_bottom = (12, 88, 95) if self.square_id % 2 == 0 else (9, 110, 119)
		self.square_surface = pygame.Surface((self.square_size, self.square_size))
		self.square_surface.fill(color_square)
		self.bottom_surface = pygame.Surface((self.square_size, self.square_size // 3))
		self.bottom_surface.fill(color_bottom)
		self.rect_square = pygame.Rect(self.x, self.y,  self.square_size, self.square_size)
		self.rect_bottom = pygame.Rect(self.x, self.y + self.square_size, self.square_size, self.square_size // 3)

	def draw(self, screen: pygame.Surface):
		"""Draw the square on the screen"""
		screen.blit(self.square_surface, self.rect_square)
		screen.blit(self.bottom_surface, self.rect_bottom)
