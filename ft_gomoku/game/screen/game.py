from math import sqrt
from time import sleep

import pygame
import time
import ctypes


from ft_gomoku.AI.AI import run_ai
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from ft_gomoku.game.screen.components import draw_board, place_rocks, redraw_board
from ft_gomoku.data_structure.GameStruct import GameStruct
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
				place_rocks(engine.screen, game_engine, result, debug, 35)
				return 'play'
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

	# Create the text
	font = pygame.font.Font(None, 36)
	text_timer = font.render(f"Time : {elapsed_time} seconds", True, (255, 255, 255))
	text_rect = text_timer.get_rect(topleft=(10, 10))

	text_p1_timer = font.render(f"Player 1 reflection time : {player_1_time} seconds", True, (255, 255, 255))
	text_p1_rect = text_p1_timer.get_rect(topleft=(10, 40))

	text_p2_timer = font.render(f"Player 2 reflection time : {player_2_time} seconds", True, (255, 255, 255))
	text_p2_rect = text_p2_timer.get_rect(topleft=(10, 70))

	# Fill a rectangle with the background color to clean screen
	pygame.draw.rect(engine.screen, (8, 26, 43), text_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_rect)

	engine.screen.blit(text_timer, (10, 10))
	engine.screen.blit(text_p1_timer, (10, 40))
	engine.screen.blit(text_p2_timer, (10, 70))


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
	game_engine.update_player_turn()
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
						rocks_ai = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win], player_turn, game_engine.get_opponent_turn())
						ai_rocks = rocks_ai
					if ai_rocks is not None:
						coords_to_place = rocks_coord[ai_rocks]
						draw_rocks(engine.screen, game_engine, coords_to_place, 35, 0)
				result = handle_events(engine, events_list, rocks_coord, game_engine, debug_mode)
				if result == 'play':
					ai_rocks = None
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
					run_ai_cpp(game_engine)
					rocks_ia = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win])
					coords_to_place = (rocks_ia, rocks_coord[rocks_ia])
					place_rocks(engine.screen, game_engine, coords_to_place, False, 35)
					pass
			if game_engine.grid.get_last_move() != game_engine.get_last_move(): # A CHANGER
				game_engine.set_last_move(game_engine.grid.get_last_move())
				redraw_board(engine, game_engine, rocks_coord)
			engine.clock.tick(engine.settings.get_fps())
			show_timer(engine, game_engine)
			if debug_mode or info_mode:
				redraw_board(engine, game_engine, rocks_coord)
				debug_screen(engine, game_engine, debug)
			pygame.display.update()


def convert_history(history_to_convert: []) -> str:
	return ':'.join('{}:{}:{}'.format(*move) for move in history_to_convert)


def run_ai_cpp(game: GameStruct):
	start_time = time.time()

	lib = ctypes.CDLL("./ft_gomoku/AI_cpp/ft_gomoku_ai.so")
	lib.run_ai.restype = ctypes.c_int
	lib.run_ai.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char, ctypes.c_char]

	history_str = convert_history(game.grid.history)

	grid_string = ''.join(game.grid.line_grid)
	bytes_history = (history_str + '\0').encode('utf-8')
	bytes_grid = (grid_string + '\0').encode('utf-8')
	c_history = ctypes.c_char_p(bytes_history)
	c_grid = ctypes.c_char_p(bytes_grid)

	p1 = b'1'
	p2 = b'2'

	result = lib.run_ai(c_grid, c_history, p1, p2)
	execution_time_ms = (time.time() - start_time) * 1000

	print("Execution time for run_ai :", execution_time_ms, "ms",
	      "In case of > 500 ms, sorry leo, we are in a big trouble.")
	print("Result:", result)