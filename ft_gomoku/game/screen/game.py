from math import sqrt
from time import sleep

import pygame
import time

from ft_gomoku.AI.AI import run_ai
from ft_gomoku import Engine, set_titlescreen, stop_sound
from ft_gomoku.game.screen.components import draw_board, place_rocks, redraw_board
from ft_gomoku.data_structure.GameStruct import GameStruct
from ft_gomoku.game.screen.animations import anim_win
from ft_gomoku import RuleStatus, five_to_win, double_three_forbidden, capture, ten_capture_to_win

from ft_gomoku.data_structure.DebuggerStruct import DebuggerStruct

from ft_gomoku.game.debug.debug import debug_screen
from ft_gomoku.game.screen.components import draw_rocks
# from ft_gomoku.data_structure.DebuggerStruct import DebuggerStruct


def handle_events_debug(engine, game_engine: GameStruct, event):
	if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
		game_engine.update_player_turn()
	if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
		game_engine.set_player_turn(('0', '0'))


def handle_events(engine, events_list, rocks_coord, game_engine: GameStruct, debug: bool, radius=15) -> str | bool:
	for event in events_list:
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return 'quit'
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
				return 'debug'
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
				return 'info'
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
				return 'help'
		if event.type == pygame.MOUSEBUTTONDOWN:
			result = check_rocks_pos(rocks_coord, event.pos, radius)
			if result is not None:
				return place_rocks(engine.screen, game_engine, result, debug, 35)
		if debug:
			handle_events_debug(engine, game_engine, event)
	return True


def check_rocks_pos(rocks_coord: dict, mouse_pos: tuple, radius=15) -> tuple | None:
	"""Check if the mouse is on a rock
	:param rocks_coord: the rocks coordinates
	:param mouse_pos: the mouse position
	:param radius: the radius of the rock
	return: the rock position or None
	"""
	for _coords, _board_coords in rocks_coord.items():
		dx = abs(_board_coords[0] - mouse_pos[0])
		dy = abs(_board_coords[1] - mouse_pos[1])
		if dx <= radius and dy <= radius:
			return _coords, _board_coords
	return None


def show_timer(engine: Engine, game_engine: GameStruct):
	"""Show the timer
	:param engine: the game engine
	:param game_engine: the game engine
	"""
	elapsed_time = int(time.time() - game_engine.get_time())
	player_1_time = round(game_engine.total_time_player_1[1], 2)
	player_2_time = round(game_engine.total_time_player_2[1], 2)
	player_1_avg = round(sum(game_engine.list_time_player_1) / len(game_engine.list_time_player_1), 2) if len(game_engine.list_time_player_1) > 0 else 0
	player_2_avg = round(sum(game_engine.list_time_player_2) / len(game_engine.list_time_player_2), 2) if len(game_engine.list_time_player_2) > 0 else 0

	# Create the text
	font = engine.font
	text_timer = font.render(f"Time : {elapsed_time} seconds", True, (255, 255, 255))
	text_rect = text_timer.get_rect(topleft=(10, 10))

	text_p1_timer = font.render(f"Player 1 reflection time : {player_1_time} seconds", True, (255, 255, 255))
	text_p1_rect = text_p1_timer.get_rect(topleft=(10, 40))

	text_p2_timer = font.render(f"Player 2 reflection time : {player_2_time} seconds", True, (255, 255, 255))
	text_p2_rect = text_p2_timer.get_rect(topleft=(10, 70))

	text_p1_avg = font.render(f"Player 1 average reflection time : {player_1_avg} seconds", True, (255, 255, 255))
	text_p1_avg_rect = text_p1_avg.get_rect(topleft=(10, 100))

	text_p2_avg = font.render(f"Player 2 average reflection time : {player_2_avg} seconds", True, (255, 255, 255))
	text_p2_avg_rect = text_p2_avg.get_rect(topleft=(10, 130))

	# Fill a rectangle with the background color to clean screen
	pygame.draw.rect(engine.screen, (8, 26, 43), text_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_avg_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_avg_rect)

	engine.screen.blit(text_timer, (10, 10))
	engine.screen.blit(text_p1_timer, (10, 40))
	engine.screen.blit(text_p2_timer, (10, 70))
	engine.screen.blit(text_p1_avg, (10, 100))
	engine.screen.blit(text_p2_avg, (10, 130))


def show_capture(engine: Engine, game_engine: GameStruct):
	"""Show the capture
	:param engine: the game engine
	:param game_engine: the game engine
	"""
	font = engine.font
	player_1_capture = game_engine.grid.get_captured_stones(game_engine.player_1[1])
	player_2_capture = game_engine.grid.get_captured_stones(game_engine.player_2[1])
	text_p1_capture = font.render(f'Player 1: {player_1_capture} x ', True, (255, 255, 255))
	text_p2_capture = font.render(f'Player 2: {player_2_capture} x ', True, (255, 255, 255))
	img_p1 = game_engine.get_rocks_img(game_engine.player_2[1], False)
	img_p2 = game_engine.get_rocks_img(game_engine.player_1[1], False)
	text_p1_rect = text_p1_capture.get_rect(topleft=(10, engine.window_size[1] // 2))
	text_p2_rect = text_p1_capture.get_rect(topleft=(10, engine.window_size[1] // 2 + 50))
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_rect)
	engine.screen.blit(text_p1_capture, (10, engine.window_size[1] // 2))
	engine.screen.blit(text_p2_capture, (10, engine.window_size[1] // 2 + 50))
	engine.screen.blit(img_p1, (130, engine.window_size[1] // 2 - 5))
	engine.screen.blit(img_p2, (130, engine.window_size[1] // 2 + 50 - 5))


def game_screen(engine: Engine, ai: bool = False):

	# Stop music
	stop_sound()

	# Set the title screen
	set_titlescreen('Gomoku - Game')

	# Set the game engine
	game_engine = GameStruct(18, '1', '2')
	game_engine.init_img(35)

	# Set timer
	game_engine.set_time(time.time())
	game_engine.start_player_timer(game_engine.get_player_turn()[1])

	debug_mode = False
	info_mode = False
	help_mode = False
	ai_rocks = None
	debug = DebuggerStruct(engine, game_engine)
	# Main loop
	while True:
		events_list = []
		engine.screen.fill((8, 26, 43))
		# Draw the board and get the possible rocks coordinates
		rocks_coord = draw_board(engine, game_engine)
		redraw_board(engine, game_engine, rocks_coord)
		running = True
		while running:
			events_list = pygame.event.get()
			player_turn = game_engine.get_player_turn()
			if not ai or (ai and player_turn[1] == '2') or (ai and debug_mode):
				if help_mode and not (debug_mode or info_mode):
					if ai_rocks is None:
						rocks_ai = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win], player_turn[1], game_engine.get_opponent_turn(), 1)
						ai_rocks = rocks_ai
					if ai_rocks is not None:
						coords_to_place = rocks_coord[ai_rocks]
						draw_rocks(engine.screen, game_engine, coords_to_place, 35, 0)
				result = handle_events(engine, events_list, rocks_coord, game_engine, debug_mode)
				if result == 'play':
					ai_rocks = None
				if result == 'win':
					anim_win(engine, game_engine, rocks_coord)
					return
				if result == 'quit':
					return
				if result == 'debug':
					debug_mode = not debug_mode
					game_engine.update_player_turn()
					if debug_mode:
						debug.update_cpu_info()
					redraw_board(engine, game_engine, rocks_coord)
				if result == 'info':
					info_mode = not info_mode
					if info_mode:
						debug.update_cpu_info()
				if result == 'help':
					help_mode = not help_mode
			else:
				if not debug_mode:
					rocks_ia = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win])
					coords_to_place = (rocks_ia, rocks_coord[rocks_ia])
					if place_rocks(engine.screen, game_engine, coords_to_place, False, 35) == 'win':
						anim_win(engine, game_engine, rocks_coord, True)
						return
					pass
			if game_engine.grid.get_last_move() != game_engine.get_last_move(): # A CHANGER
				game_engine.set_last_move(game_engine.grid.get_last_move())
				redraw_board(engine, game_engine, rocks_coord)
			engine.clock.tick(engine.settings.get_fps())
			show_timer(engine, game_engine)
			show_capture(engine, game_engine)
			if debug_mode or info_mode:
				redraw_board(engine, game_engine, rocks_coord)
				debug_screen(engine, game_engine, debug)
			pygame.display.update()



