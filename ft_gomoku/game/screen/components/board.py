import pygame
from time import sleep
from ft_gomoku.engine import Engine
from ft_gomoku.game.screen.square import Square


def draw_board(engine: Engine, size: int, sleep_time=0.0):
	"""Draw the game board
	:param engine: the game engine
	:param size: the size of the board
	:param sleep_time: the time to sleep between each square
	"""
	coords_dict = {}
	square_size = get_size_square(engine.get_window_size(), size)
	start_x, start_y = get_start_pos(engine.get_window_size(), size, square_size)

	for i in range(size):
		for j in range(size):
			square = Square((j * square_size) + start_x, (i * square_size + start_y), engine.get_window_size(), i + j, square_size)
			square.create_surface()
			square.draw(engine.screen)
			coords_dict.update(get_rocks_pos((j * square_size + start_x), (i * square_size + start_y), square_size, engine.screen))
			if sleep_time > 0:
				pygame.display.update()
				sleep(sleep_time)


def get_size_square(window_size: tuple, size: int) -> int:
	"""Get the size of the square
	:param window_size: the size of the window
	:param size: the size of the board
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
	"""
	start_x = (window_size[0] - (square_size * size)) // 2
	start_y = (window_size[1] - (square_size * size)) // 2
	return start_x, start_y


def get_rocks_pos(x: int, y: int, square_size: int, screen: pygame.Surface) -> dict:
	"""Get the position of the rocks
	:param x: the x position of the square
	:param y: the y position of the square
	:param square_size: the size of the square
	:param screen: the pygame screen
	"""
	coords_dict = {
		(x, y, square_size, square_size): (x, y),
		(x + square_size, y, square_size, square_size): (x + square_size, y),
		(x, y + square_size, square_size, square_size): (x, y + square_size),
		(x + square_size, y + square_size, square_size, square_size): (x + square_size, y + square_size)
	}
	return coords_dict


def draw_transparent_circle(screen: pygame.Surface, color: tuple, pos: tuple, radius: int, alpha: int = 100):
	"""Draw a transparent circle on the screen
	:param screen: the pygame screen
	:param color: the color of the circle
	:param pos: the position (x, y) of the circle
	:param radius: the radius of the circle
	:param alpha: the alpha of the circle (0-255)
	"""
	tmp_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
	pygame.draw.circle(tmp_surface, color+(alpha,), (radius, radius), radius)
	screen.blit(tmp_surface, (pos[0]-radius, pos[1]-radius))

# DEBUG FUNCTION
# def draw_all_rocks(screen: pygame.Surface, coords_dict: dict, color: tuple, radius: int, alpha: int = 255):
# 	"""Draw all the rocks on the screen
# 	:param screen: the pygame screen
# 	:param coords_dict: the dictionary of the coordinates of the rocks
# 	:param color: the color of the rocks
# 	:param radius: the radius of the rocks
# 	:param alpha: the alpha of the rocks (0-255)
# 	"""
# 	i = 1
# 	for pos, _ in coords_dict.items():
# 		print(i)
# 		i += 1
# 		draw_transparent_circle(screen, color, _, radius, alpha)
# 	pygame.display.update()
