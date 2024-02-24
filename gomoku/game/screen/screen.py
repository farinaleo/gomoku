import pygame
from gomoku.game import Engine


def main_menu(engine: Engine):
	""" Main menu screen """
	pygame.display.set_caption('Gomoku - Title screen')
	while True:
		engine.screen.fill("purple")
		pygame.display.flip()
		if pygame.event.get(pygame.KEYDOWN):
			print('Key pressed')
			break
