from random import randint

import pygame
from ft_gomoku.engine import get_image, play_sound
from ft_gomoku.data_structure.GameStruct import GameStruct


#TODO: change player value type

def anim_win(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, player: int):
	print(game_engine.grid.line_grid)
