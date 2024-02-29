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
			get_rocks_pos((j * square_size) + start_x, (i * square_size + start_y), i, j, size, square_size, engine.screen)
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


def get_rocks_pos(x: int, y: int, i: int, j: int, size: int, square_size: int, screen: pygame.Surface):
	print('Point: ', x, y)
	tmp = pygame.Surface((square_size // 2, square_size // 2))
	tmp1 = None
	tmp2 = None
	tmp3 = None
	if j + 1 == size:
		tmp1 = tmp2 = pygame.Surface((square_size // 2, square_size // 2))
	if i + 1 == size:
		tmp2 = pygame.Surface((square_size // 2, square_size // 2))
		if j + 1 == size:
			tmp3 = pygame.Surface((square_size // 2, square_size // 2))
	pygame.draw.circle(tmp, (255, 255, 255), (square_size // 4, square_size // 4), square_size // 4)
	screen.blit(tmp, (x - square_size // 4, y - square_size // 4))
	if tmp1 is not None:
		pygame.draw.circle(tmp1, (255, 255, 255), (square_size // 4, square_size // 4), square_size // 4)
		screen.blit(tmp, (x + square_size - square_size // 4, y - square_size // 4))
	if tmp2 is not None:
		pygame.draw.circle(tmp2, (255, 255, 255), (square_size // 4, square_size // 4), square_size // 4)
		screen.blit(tmp, (x - square_size // 4, y + square_size - square_size // 4))
	if tmp3 is not None:
		pygame.draw.circle(tmp3, (255, 255, 255), (square_size // 4, square_size // 4), square_size // 4)
		screen.blit(tmp, (x + square_size - square_size // 4, y + square_size - square_size // 4))
