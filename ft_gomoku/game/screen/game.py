from math import sqrt
from time import sleep

import pygame
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from ft_gomoku.game.screen.components import draw_board, draw_transparent_circle, place_rocks, redraw_board
from ft_gomoku.data_structure.GameStruct import GameStruct


def handle_events(engine, events_list, rocks_coord, game_engine: GameStruct, radius=15) -> str | bool:
	for event in pygame.event.get():
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				print('quit')
				engine.set_running(False)
				return 'quit'
		if event.type == pygame.MOUSEBUTTONDOWN:
			result = check_rocks_pos(rocks_coord, event.pos, radius)
			if result is not None:
				print('OK !')
				place_rocks(engine.screen, game_engine, result, 35)
				return 'play'
	return True


def game_screen(engine: Engine):

	# Set the title screen
	set_titlescreen('Gomoku - Game')

	# Set the game engine
	game_engine = GameStruct(18, "Nolan", "Leo")

	# Main loop
	while True:
		events_list = []
		engine.screen.fill((8, 26, 43))

		# Draw the board and get the possible rocks coordinates
		rocks_coord = draw_board(engine, game_engine)
		redraw_board(engine, game_engine)
		running = True
		while running:
			result = handle_events(engine, events_list, rocks_coord, game_engine)
			if result == 'quit':
				return
			# font = pygame.font.Font(None, 36)
			# elapsed_time = pygame.time.get_ticks() - start_time
			# seconds = elapsed_time / 1000.0
			# text = font.render(f"Temps écoulé : {seconds:.2f} secondes", True, (0, 0, 0))
			# engine.screen.blit(text, (10, 10))
			pygame.display.update()
			engine.clock.tick(engine.settings.get_fps())
			# redraw_board(engine, game_engine)
			# game_engine.update_time(1)


def check_rocks_pos(rocks_coord: dict, mouse_pos: tuple, radius=15) -> tuple | None:
	"""Check if the mouse is on a rock
	:param rocks_coord: the rocks coordinates
	:param mouse_pos: the mouse position
	:param radius: the radius of the rock
	return: the rock position or None
	"""
	for _rect, _dict in rocks_coord.items():
		dx = abs(_rect[0] - mouse_pos[0])
		dy = abs(_rect[1] - mouse_pos[1])
		if dx <= radius and dy <= radius:
			return _dict['coords'], (_dict['x'], _dict['y'])
	return None
