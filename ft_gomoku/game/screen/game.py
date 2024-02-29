from time import sleep

import pygame
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from ft_gomoku.game.screen.components import draw_board


def handle_events(engine, events_list) -> str | bool:
	for event in pygame.event.get():
		if event.type in [pygame.VIDEORESIZE]:
			if not engine.settings.get_fullscreen():
				engine.update_screen_size()
				return 'restart'
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				print('quit')
				engine.set_running(False)
				return 'quit'
	return True


def game_screen(engine: Engine):
	set_titlescreen('Gomoku - Game')

	while True:
		events_list = []

		engine.screen.fill((8, 26, 43))
		draw_board(engine, 18)
		running = True

		while running:
			result = handle_events(engine, events_list)
			if result == 'quit':
				return
			pygame.display.update()
			engine.clock.tick(engine.settings.get_fps())
