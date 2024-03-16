from random import randint

import pygame
from ft_gomoku.engine import get_image, play_sound
from ft_gomoku.data_structure.GameStruct import GameStruct


def anim_place_rock(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, radius: int, player: int, sound: bool = True):
	"""Animate the rock placement
	"""
	rock_img = game_engine.get_rocks_img(player, True)
	rock_img.convert_alpha()
	rock_img.set_alpha(0)
	sound_file = ('explode' + str(randint(1, 5)) + '.mp3')

	if sound is True:
		play_sound(sound_file)
	for i in range(1, 16):
		rock_img.set_alpha(i * 17)
		screen.blit(rock_img, (coords[0] - radius // 2, coords[1] - radius // 2))
		pygame.display.update()
		pygame.time.wait(20)
	pygame.display.update()

