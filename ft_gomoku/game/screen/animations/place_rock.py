from random import randint

import pygame
from ft_gomoku.engine import get_image, play_sound
from ft_gomoku.data_structure.GameStruct import GameStruct


def anim_place_rock(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, radius: int, player: int):
	"""Animate the rock placement
	"""
	rock_img = None
	if player == '1':
		rock_img = get_image('rocks_white.png', radius, radius)
	else:
		rock_img = get_image('rocks_black.png', radius, radius)

	rock_img.convert_alpha()
	rock_img.set_alpha(0)

	sound = ('explode' + str(randint(1, 5)) + '.mp3')
	play_sound(sound)
	for i in range(1, 10):
		screen.blit(rock_img, (coords[0] - radius // 2, coords[1] - radius // 2))
		pygame.display.update()
		rock_img.set_alpha(i * 25)
		pygame.time.wait(30)
	pygame.display.update()

