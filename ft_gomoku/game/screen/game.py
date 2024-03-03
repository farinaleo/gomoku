from math import sqrt
from time import sleep

import pygame
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from ft_gomoku.game.screen.components import draw_board, draw_transparent_circle, place_rocks


def handle_events(engine, events_list, rocks_coord, player_turn, radius=15) -> str | bool:
	for event in pygame.event.get():
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				print('quit')
				engine.set_running(False)
				return 'quit'
		if event.type == pygame.MOUSEBUTTONDOWN:
			result = check_rocks_pos(rocks_coord, event.pos, radius)
			if result is not None:
				print(player_turn)
				place_rocks(engine.screen, result, player_turn, 35)
				return 'play'
	return True


def game_screen(engine: Engine):
	set_titlescreen('Gomoku - Game')

	while True:
		events_list = []
		player_turn = 1
		engine.screen.fill((8, 26, 43))
		rocks_coord = draw_board(engine, 18)
		running = True

		while running:
			result = handle_events(engine, events_list, rocks_coord, player_turn)
			if result == 'quit':
				return
			elif result == 'play':
				player_turn = 2 if player_turn == 1 else 1
			pygame.display.update()
			engine.clock.tick(engine.settings.get_fps())


def check_rocks_pos(rocks_coord: dict, mouse_pos: tuple, radius=15) -> tuple | None:
	"""Check if the mouse is on a rock
	:param rocks_coord: the rocks coordinates
	:param mouse_pos: the mouse position
	:param radius: the radius of the rock
	return: the rock position or None
	"""
	for pos, _ in rocks_coord.items():
		dx = abs(pos[0] - mouse_pos[0])
		dy = abs(pos[1] - mouse_pos[1])
		if dx <= radius and dy <= radius:
			return _
	return None
