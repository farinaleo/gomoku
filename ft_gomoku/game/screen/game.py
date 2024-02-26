from time import sleep

import pygame
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from .square import Square




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
		draw_board(engine, 0.01)
		running = True

		while running:
			result = handle_events(engine, events_list)
			if result == 'quit':
				return
			engine.clock.tick(engine.settings.get_fps())


def draw_board(engine: Engine, sleep_time=0.0):
	"""Draw the game board"""
	for i in range(19):
		for j in range(19):
			start_x = (engine.get_window_size()[0] - 950) / 2
			start_y = (engine.get_window_size()[1] - 950) / 2
			color = (10, 130, 141) if (i + j) % 2 == 0 else (12, 154, 165)
			color_bottom = (12, 88, 95) if (i + j) % 2 == 0 else (9, 110, 119)
			print(engine.get_window_size()[0])
			square = Square((j * 50) + start_x, (i * 50 + start_y), color, color_bottom, engine.get_window_size())
			square.create_surface()
			square.draw(engine.screen)
			if sleep_time > 0:
				pygame.display.update()
				sleep(sleep_time)
