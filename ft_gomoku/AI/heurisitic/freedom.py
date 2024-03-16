#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/13/24, 9:36 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


def freedom_rate(line, grid, x, y, player, opponent, size, line_size) -> float:
	"""Evaluate the freedom stone rate.
	:param line: the game as list.
	:param grid: the node.
	:param x: last move played.
	:param y: last move played.
	:param player: player who played the move to evaluate.
	:param opponent: the opponent.
	:param size: the grid size.
	:param line_size: the total lien size.
	:return: the sum of freedom for each direction over 8.
	"""
	count = 0
	# left up
	count = count + freedom_dir(line, x, y, size, opponent, -1, -1)
	# up
	count = count + freedom_dir(line, x, y, size, opponent, 0, -1)
	# right up
	count = count + freedom_dir(line, x, y, size, opponent, 1, -1)
	# left
	count = count + freedom_dir(line, x, y, size, opponent, -1, 0)
	# right
	count = count + freedom_dir(line, x, y, size, opponent, 1, 0)
	# left down
	count = count + freedom_dir(line, x, y, size, opponent, -1, 1)
	# down
	count = count + freedom_dir(line, x, y, size, opponent, 0, 1)
	# right down
	count = count + freedom_dir(line, x, y, size, opponent, 1, 1)
	return count / 8


def freedom_dir(line, x, y, size, opponent, dir_x, dir_y) -> float:
	"""Evaluate the freedom for a specific direction.
	:param line: the game as list.
	:param x: last move played.
	:param y: last move played.
	:param size: the grid size.
	:param opponent: the opponent value.
	:param dir_x: the x direction.
	:param dir_y: the y direction.
	:return: the number of free steps possible from (x, y) [0,4].
	"""
	count = 0
	while count < 5 and 0 <= x < size and 0 <= y < size and line[x + y * size] != opponent:
		x = x + dir_x
		y = y + dir_y
		count = count + 1
	if count > 0:
		count = count - 1
	return count
