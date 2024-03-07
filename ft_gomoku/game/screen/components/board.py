import pygame
from time import sleep
from ft_gomoku import RuleStatus, five_to_win
from ft_gomoku.engine import Engine, play_sound
from ft_gomoku.game.screen.square import Square
from ft_gomoku.data_structure import GameStruct
from ft_gomoku.engine.image_control import get_image
from ft_gomoku.game.screen.animations import anim_place_rock


def draw_board(engine: Engine, game_engine: GameStruct) -> dict:
	"""Draw the game board
	:param engine: the game engine
	:param game_engine: the game engine
	:return: the coordinates of the rocks
	"""
	size = game_engine.get_board_size()
	coords_dict = {}

	# Get the size of the square
	square_size = get_size_square(engine.get_window_size(), size)

	# Get the start position of the board
	start_x, start_y = get_start_pos(engine.get_window_size(), size, square_size)

	for i in range(size):
		for j in range(size):

			# Create the square and add it to the board
			square = Square((j * square_size) + start_x, (i * square_size + start_y), engine.get_window_size(), i + j, square_size)
			square.create_surface()
			game_engine.add_square(square)

			# Add the rocks coordinates to the dictionary
			coords_dict.update(get_rocks_pos((j * square_size + start_x), (i * square_size + start_y), square_size, j, i))
	return coords_dict


def get_size_square(window_size: tuple, size: int) -> int:
	"""Get the size of the square
	:param window_size: the size of the window
	:param size: the size of the board
	:return: the size of the square
	"""
	ratio_square = window_size[1] / 1080
	ratio_nbr = 19 / size
	print(int(40 * ratio_square * ratio_nbr))
	return int(40 * ratio_square * ratio_nbr)


def get_start_pos(window_size: tuple, size: int, square_size: int) -> tuple:
	"""Get the start position of the board
	:param window_size: the size of the window
	:param size: the size of the board
	:param square_size: the size of the square
	:return: the start position of the board
	"""
	start_x = (window_size[0] - (square_size * size)) // 2
	start_y = (window_size[1] - (square_size * size)) // 2
	return start_x, start_y


def get_rocks_pos(x: int, y: int, square_size: int, g_x: int, g_y: int) -> dict:
	"""Get the position of the rocks
	:param x: the x position of the square
	:param y: the y position of the square
	:param square_size: the size of the square
	:param g_x: the x position of the grid
	:param g_y: the y position of the grid
	"""
	rocks_size = square_size
	coords_dict = {
		(g_x, g_y): (x, y),
		(g_x + 1, g_y): (x + square_size, y),
		(g_x, g_y + 1): (x, y + square_size),
		(g_x + 1, g_y + 1): (x + square_size, y + square_size),
	}
	return coords_dict


def place_rocks(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, radius: int):
	"""Place the rocks on the screen
	:param screen: the pygame screen
	:param game_engine: the game engine
	:param coords: the coordinates of the rocks
	:param radius: the radius of the rocks
	"""
	print(coords[0])
	player_turn = game_engine.get_player_turn()
	result = game_engine.grid.add_rock(coords[0][1], coords[0][0], player_turn[1], None)
	print(result)
	# if result is RuleStatus.WIN:
	# 	print(f"Player {player_turn[1]} win")
	# 	sleep(5)
	# 	return
	if result is not RuleStatus.OK:
		play_sound('wrong.mp3')
		pygame.time.wait(500)
		return
	game_engine.update_player_turn()
	anim_place_rock(screen, game_engine, coords[1], radius, player_turn[1])
	# draw_rocks(screen, game_engine, engine, coords, radius, player_turn[1])
	# print(game_engine.grid.get_grid())
	pygame.display.update()


def draw_rocks(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, radius: int, player: int):
	"""Draw the rocks on the screen
	:param screen: the pygame screen
	:param game_engine: the game engine
	:param coords: the coordinates of the rocks
	:param radius: the radius of the rocks
	:param player: the player
	"""
	rock_img = None
	if player == '1':
		rock_img = get_image('rocks_white.png', radius, radius)
	else:
		rock_img = get_image('rocks_black.png', radius, radius)

	screen.blit(rock_img, (coords[0] - radius // 2, coords[1] - radius // 2))


def redraw_board(engine: Engine, game_engine: GameStruct, coords_dict: dict):
	engine.screen.fill((8, 26, 43))
	for square in game_engine.board:
		square.draw(engine.screen)
	grid = game_engine.grid.get_grid()
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			value = grid[i][j]
			if value is not 0:
				coords = coords_dict[(j, i)]
				print(coords)
				draw_rocks(engine.screen, game_engine, coords, 35, value)

