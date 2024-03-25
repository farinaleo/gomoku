import pygame
from ft_gomoku.engine import Engine


def maximize_button(engine: Engine):
	"""Return maximize button
	:param engine: Engine
	"""
	image_maximize = pygame.image.load('ft_gomoku/assets/img/maximize.png')
	image_maximize = pygame.transform.scale(image_maximize, (50, 50))
	image_maximize_rect = image_maximize.get_rect()
	image_maximize_rect.bottomright = (engine.get_window_size()[0] - 30, engine.get_window_size()[1] - 120)
	return image_maximize, image_maximize_rect
