import pygame
from gomoku.game import Engine
from gomoku.game.engine import load_music


def main_menu(engine: Engine):
	""" Main menu screen """
	pygame.display.set_caption('Gomoku - Title screen')
	engine.screen.fill((8, 26, 43))
	pygame.display.flip()
	load_music('title_screen.mp3')
	while 1 == 1:
		engine.screen.fill((8, 26, 43))
