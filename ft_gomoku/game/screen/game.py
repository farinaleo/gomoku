import time
import pygame
from ft_gomoku.AI.AI import run_ai
from ft_gomoku.game.debug.debug import debug_screen
from ft_gomoku.game.screen.animations import anim_win
from ft_gomoku.game.screen.components import draw_rocks
from ft_gomoku import Engine, set_titlescreen, stop_sound
from ft_gomoku.data_structure.GameStruct import GameStruct
from ft_gomoku.data_structure.DebuggerStruct import DebuggerStruct
from ft_gomoku import five_to_win, double_three_forbidden, capture, ten_capture_to_win
from ft_gomoku.game.screen.components import draw_board, place_rocks, redraw_board, show_capture, show_timer


def handle_events_debug(game_engine: GameStruct, event):
	"""Handle the debug events
	:param game_engine: the game engine
	:param event: the event
	"""
	# Change the player turn with the 'r' key
	if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
		game_engine.update_player_turn()

	# Change the player turn to '0' with the 'd' key. Used for remove rocks
	if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
		game_engine.set_player_turn(('0', '0'))


def handle_events(engine: Engine, events_list, rocks_coord, game_engine: GameStruct, radius=15) -> str | None:
	"""Handle the events
	:param engine: the game engine
	:param events_list: the events list
	:param rocks_coord: the rocks coordinates list
	:param game_engine: the game engine
	:param radius: the radius of the rock
	"""
	for event in events_list:
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			# Quit the game with the 'esc' key or the close button
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return 'quit'

			# Activate the debug mode with the 'F3' key
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
				return 'debug'

			# Activate the info mode with the 'F4' key
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
				return 'info'

			# Activate the help mode with the 'F2' key
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
				return 'help'

		# Place a rock with the 'LMB' key
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			result = check_rocks_pos(rocks_coord, event.pos, radius)
			if result is not None:
				return place_rocks(engine.screen, game_engine, result, engine.debug_mode, engine.rocks_size)
		if engine.debug_mode:
			handle_events_debug(game_engine, event)
	return None


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


def game_screen(engine: Engine, ai: bool = False):

	# Stop music
	stop_sound()

	# Set the title screen
	set_titlescreen('Gomoku - Game')

	# Set the game engine
	game_engine = GameStruct(18, '1', '2')
	game_engine.init_img(engine.rocks_size)

	# Set timer
	game_engine.set_time(time.time())
	game_engine.start_player_timer(game_engine.get_player_turn()[1])

	ai_rocks = None
	debug = DebuggerStruct(engine, game_engine)

	# Draw the board and get the possible rocks coordinates
	rocks_coord = draw_board(engine, game_engine)
	redraw_board(engine, game_engine, rocks_coord)

	while True:
		events_list = pygame.event.get()
		player_turn = game_engine.get_player_turn()

		# Player turn only
		if not ai or (ai and player_turn[1] == '2') or (ai and engine.debug_mode):

			# Help mode
			if engine.help_mode and not (engine.debug_mode or engine.info_mode):
				if ai_rocks is None:
					rocks_ai = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win], player_turn[1], game_engine.get_opponent_turn(), 1)
					ai_rocks = rocks_ai
				if ai_rocks is not None:
					coords_to_place = rocks_coord[ai_rocks]
					draw_rocks(engine.screen, game_engine, coords_to_place, engine.rocks_size, '0')

			result = handle_events(engine, events_list, rocks_coord, game_engine)
			if result == 'play':
				ai_rocks = None
			if result == 'win':
				anim_win(engine, game_engine, rocks_coord)
				return
			if result == 'quit':
				return
			if result == 'debug':
				engine.debug_mode = not engine.debug_mode
				game_engine.update_player_turn()
				if engine.debug_mode:
					debug.update_cpu_info()
				redraw_board(engine, game_engine, rocks_coord)
			if result == 'info':
				engine.info_mode = not engine.info_mode
				if engine.info_mode:
					debug.update_cpu_info()
				redraw_board(engine, game_engine, rocks_coord)
			if result == 'help':
				engine.help_mode = not engine.help_mode
		else:
			# AI turn
			if not engine.debug_mode:
				rocks_ia = run_ai(game_engine.grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win])
				if rocks_ia is None:
					return
				coords_to_place = (rocks_ia, rocks_coord[rocks_ia])
				if place_rocks(engine.screen, game_engine, coords_to_place, False, engine.rocks_size) == 'win':
					anim_win(engine, game_engine, rocks_coord, True)
					return
				pass
		# Last rock placed design
		if game_engine.grid.get_last_move() != game_engine.get_last_move():
			game_engine.set_last_move(game_engine.grid.get_last_move())
			redraw_board(engine, game_engine, rocks_coord)
		show_timer(engine, game_engine)
		show_capture(engine, game_engine)

		# Show party information
		if engine.debug_mode or engine.info_mode:
			redraw_board(engine, game_engine, rocks_coord)
			debug_screen(engine, game_engine, debug)
		pygame.display.update()
		engine.clock.tick(engine.settings.get_fps())



