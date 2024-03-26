import pygame
from ft_gomoku.engine import Engine


def get_1vs1_button(engine: Engine):
	"""Return 1vs1 button
	:param engine: Engine
	"""
	image = pygame.image.load('ft_gomoku/assets/img/button_1vs1.png')
	image_width = 530
	image_height = 130
	ratio_width = engine.get_window_size()[0] / 1920
	ratio_height = engine.get_window_size()[1] / 1080
	image = pygame.transform.scale(image, (image_width * ratio_width, image_height * ratio_height))
	image_rect = image.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] // 2))
	return image, image_rect


def get_ai_button(engine: Engine):
	"""Return AI button
	:param engine: Engine
	"""
	image = pygame.image.load('ft_gomoku/assets/img/button_ai.png')
	image_width = 530
	image_height = 130
	ratio_width = engine.get_window_size()[0] / 1920
	ratio_height = engine.get_window_size()[1] / 1080
	ratio_spacing = (image_width * ratio_width - image_height * ratio_height) // 2
	image = pygame.transform.scale(image, (image_width * ratio_width, image_height * ratio_height))
	image_rect = image.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] // 2 + ratio_spacing))
	return image, image_rect
