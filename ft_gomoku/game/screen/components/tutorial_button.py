import pygame
from ft_gomoku.engine import Engine


def get_tutorial_button(engine: Engine):
	"""Return tutorial button
	:param engine: Engine
	"""
	image = pygame.image.load('ft_gomoku/assets/img/button_tutorial.png')
	image_width = 530
	image_height = 130
	ratio_width = engine.get_window_size()[0] / 1920
	ratio_height = engine.get_window_size()[1] / 1080
	image = pygame.transform.scale(image, (image_width * ratio_width, image_height * ratio_height))
	ratio_spacing = (image_width * ratio_width - image_height * ratio_height) // 2
	image_rect = image.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] // 2 + ratio_spacing * 2))
	return image, image_rect
