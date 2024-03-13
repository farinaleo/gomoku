from math import sqrt
from time import sleep

import pygame
import time

from ft_gomoku.AI.AI import run_ia
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound
from ft_gomoku.game.screen.components import draw_board, place_rocks, redraw_board
from ft_gomoku.data_structure.GameStruct import GameStruct


def handle_events(engine, events_list, rocks_coord, game_engine: GameStruct, radius=15) -> str | bool:
	for event in pygame.event.get():
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return 'quit'
		if event.type == pygame.MOUSEBUTTONDOWN:
			result = check_rocks_pos(rocks_coord, event.pos, radius)
			if result is not None:
				place_rocks(engine.screen, game_engine, result, 35)
				return 'play'
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
	# Main loop
	while True:
		events_list = []
		engine.screen.fill((8, 26, 43))

		# Draw the board and get the possible rocks coordinates
		rocks_coord = draw_board(engine, game_engine)
		redraw_board(engine, game_engine, rocks_coord)
		running = True
		while running:
			player_turn = game_engine.get_player_turn()
			if not ai or (ai and player_turn[1] == '2'):
				result = handle_events(engine, events_list, rocks_coord, game_engine)
				if result == 'quit':
					return
			else:
				rocks_ia = run_ia(game_engine.grid, None)
				coords_to_place = (rocks_ia, rocks_coord[rocks_ia])
				place_rocks(engine.screen, game_engine, coords_to_place, 35)
				pass
			if game_engine.grid.get_last_move() != game_engine.get_last_move(): # A CHANGER
				game_engine.set_last_move(game_engine.grid.get_last_move())
				redraw_board(engine, game_engine, rocks_coord)
			engine.clock.tick(engine.settings.get_fps())
			show_timer(engine, game_engine)
			pygame.display.update()
