import pygame
from typing import Type
from gomoku.game.engine import Engine


def mute_button(engine: Engine):
	"""Mute button"""
	image_mute = pygame.image.load('gomoku/assets/img/volume-mute.png')
	image_unmute = pygame.image.load('gomoku/assets/img/volume.png')
	image_mute = pygame.transform.scale(image_mute, (50, 50))
	image_unmute = pygame.transform.scale(image_unmute, (50, 50))
	image_mute_rect = image_mute.get_rect()
	image_unmute_rect = image_unmute.get_rect()
	image_mute_rect.bottomright = (engine.settings.get_width() - 30, engine.settings.get_height() - 30)
	image_unmute_rect.bottomright = (engine.settings.get_width() - 30, engine.settings.get_height() - 30)
	return image_mute, image_mute_rect, image_unmute, image_unmute_rect


def button_action(engine: Engine):
	"""Mute and unmute button action"""
	engine.settings.set_music(not engine.settings.get_music())
	pygame.mixer.music.set_volume(int(engine.settings.get_music()))
	return engine.settings.get_music()
