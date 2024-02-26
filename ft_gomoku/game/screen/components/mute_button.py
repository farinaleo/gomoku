import pygame
from ft_gomoku.engine import Engine


def mute_button(engine: Engine):
	"""Mute button"""
	image_mute = pygame.image.load('ft_gomoku/assets/img/volume-mute.png')
	image_unmute = pygame.image.load('ft_gomoku/assets/img/volume.png')
	image_mute = pygame.transform.scale(image_mute, (50, 50))
	image_unmute = pygame.transform.scale(image_unmute, (50, 50))
	image_mute_rect = image_mute.get_rect()
	image_unmute_rect = image_unmute.get_rect()
	image_mute_rect.bottomright = (engine.get_window_size()[0] - 30, engine.get_window_size()[1] - 30)
	image_unmute_rect.bottomright = (engine.get_window_size()[0] - 30, engine.get_window_size()[1] - 30)
	return image_mute, image_mute_rect, image_unmute, image_unmute_rect


def mute_action(engine: Engine):
	"""Mute and unmute button action"""
	engine.mute()
	return engine.settings.get_music()
