import pygame
from time import sleep
from ft_gomoku.engine import Engine
from ft_gomoku.game.screen.square import Square


def draw_board(engine: Engine, size: int, sleep_time=0.0):
	"""Draw the game board"""
	square_size = get_size_square(engine.get_window_size(), size)
	start_x, start_y = get_start_pos(engine.get_window_size(), size, square_size)

	for i in range(size):
		for j in range(size):
			square = Square((j * square_size) + start_x, (i * square_size + start_y), engine.get_window_size(), i + j, square_size)
			square.create_surface()
			square.draw(engine.screen)
			if sleep_time > 0:
				pygame.display.update()
				sleep(sleep_time)


def get_size_square(window_size: tuple, size: int) -> int:
	"""Get the size of the square"""
	ratio_square = window_size[1] / 1080
	ratio_nbr = 19 / size
	print(int(50 * ratio_square * ratio_nbr))
	return int(50 * ratio_square * ratio_nbr)


def get_start_pos(window_size: tuple, size: int, square_size: int) -> tuple:
	"""Get the start position of the board"""
	start_x = (window_size[0] - (square_size * size)) // 2
	start_y = (window_size[1] - (square_size * size)) // 2
	return start_x, start_y
