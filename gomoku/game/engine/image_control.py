import pygame
from gomoku.game.engine import Engine
import os


def get_image(image_file: str, width: int, height: int) -> pygame.Surface:
	"""Load and return image file.
	:param image_file: image file name.
	:param width: image width.
	:param height: image height.
	"""
	try:
		path_file = os.path.join('gomoku', 'assets', 'img', image_file)
		image = pygame.image.load(path_file)
	except Exception as e:
		print(f'load image error: {e}')
		return pygame.Surface((width, height))
	return pygame.transform.scale(image, (width, height))
