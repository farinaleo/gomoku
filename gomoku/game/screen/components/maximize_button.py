import pygame
from gomoku.game.engine import Engine


def maximize_button(engine: Engine):
	"""Maximize button"""
	image_maximize = pygame.image.load('gomoku/assets/img/maximize.png')
	image_maximize = pygame.transform.scale(image_maximize, (50, 50))
	image_maximize_rect = image_maximize.get_rect()
	image_maximize_rect.bottomright = (engine.get_window_size()[0] - 30, engine.get_window_size()[1] - 120)
	return image_maximize, image_maximize_rect


def maximize_action(engine: Engine):
	"""Maximize button action"""
	engine.maximize()
