#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 11:13 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid, RuleStatus

# class Point(ctypes.Structure):
#     _fields_ = [("x", ctypes.c_int),
#                 ("y", ctypes.c_int)]


def next_generation(grid: Grid, rules, ai_value):
	"""Generate the next generation from the given grid by placing the player.
	:param grid: the grid to extend
	:param rules: the rules aplay to the game
	:param ai_value: the value used to identify the AI.
	:return: a list of ft_gomoku.grid representing the next generation
	"""
	new_gen = []
	line = grid.line_grid
	size = grid.size
	line_size = len(line)
	bypass = True if line.count('0') > line_size - 2 else False
	player, opponent = (grid.player1, grid.player2) if ai_value == grid.player1 else (grid.player2, grid.player1)

	cluster = __cluster(line, size, line_size, player, opponent, bypass)
	for cell in cluster:
		if (line[cell[0] + cell[1] * size] == '0'
				and 0 <= cell[0] < size
				and 0 <= cell[1] < size):
			_next = grid.__copy__()
			if _next.add_rock(row=cell[1], col=cell[0], player=player, rules=rules) != RuleStatus.NO:
				new_gen.append(_next)
	return new_gen


def __cluster(line, size, line_size, p1, p2, bypass):
	""" determining the search area and return a points cluster.
	:param line: the game as line.
	:param size: the grid size.
	:param line_size: the total line size len(line).
	:param p1: the player.
	:param p2: the opponent.
	:param bypass: allow the middle expansion if the grid contains one stone.
	:return: a points list.
	"""
	cluster = []

	try:
		first_p1 = line.index(p1)
	except ValueError:
		first_p1 = 19 * 19
		pass
	try:
		first_p2 = line.index(p2)
	except ValueError:
		first_p2 = 19 * 19
		pass
	i = min(first_p1, first_p2)
	i = max(i, 0)

	try:
		last_p1 = line_size - line[::-1].index(p1)
	except ValueError:
		last_p1 = 0
		pass
	try:
		last_p2 = line_size - line[::-1].index(p2)
	except ValueError:
		last_p2 = 0
		pass
	end = max(last_p1, last_p2)
	end = min(end, line_size)

	# lib = ctypes.CDLL('./ft_gomoku/AI/ft_gomoku.so')
	# lib.possible_mvt.restype = ctypes.POINTER(Point)
	#
	# line_c = ctypes.c_char_p(''.join(line).encode('utf-8'))
	# size_c = ctypes.c_int(size)
	# i_c = ctypes.c_int(i)
	# end_c = ctypes.c_int(end)
	# p = lib.possible_mvt(line_c, size_c, i_c, end_c)
	# for i in range(361):
	# 	if p[i].x == -1:
	# 		break
	# 	cluster.append((p[i].x, p[i].y))
	# lib.free_alloc(p)
	while i < end:
		x = i % size
		y = i // size
		if line[i] != '0':
			_up = y - 1
			_down = y + 1
			_left = x - 1
			_right = x + 1
			# up left
			if can_expend(line, i, x, y, _left, _up, size, p1, p2, bypass):
				cluster.append((_left, _up))
			# up mid
			if can_expend(line, i, x, y, x, _up, size, p1, p2, bypass):
				cluster.append((x, _up))
			# up right
			if can_expend(line, i, x, y, _right, _up, size, p1, p2, bypass):
				cluster.append((_right, _up))
			# mid left
			if can_expend(line, i, x, y, _left, y, size, p1, p2, bypass):
				cluster.append((_left, y))
			# mid right
			if can_expend(line, i, x, y, _right, y, size, p1, p2, bypass):
				cluster.append((_right, y))
			# down left
			if can_expend(line, i, x, y, _left, _down, size, p1, p2, bypass):
				cluster.append((_left, _down))
			# down mid
			if can_expend(line, i, x, y, x, _down, size, p1, p2, bypass):
				cluster.append((x, _down))
			# down right
			if can_expend(line, i, x, y, _right, _down, size, p1, p2, bypass):
				cluster.append((_right, _down))
		i = i + 1
	if len(cluster) == 0:
		mid = size // 2
		cluster.append((mid, mid))
	return cluster


def can_expend(line, i, x, y, x_exp, y_exp, size, player, opponent, bypass) -> bool:
	"""Allow the expansion for the search.
	:param line: the game as line.
	:param i: the starting point index
	:param x: the starting x coordinate.
	:param y: the starting y coordinate.
	:param x_exp: the expansion x coordinate.
	:param y_exp: the expansion y coordinate.
	:param size: the grid size.
	:param player: the player value.
	:param opponent: the opponent value.
	:param bypass: allow the middle expansion if the grid contains one stone.
	:return: True if the expansion is allowed, otherwise False.
	"""
	if line[i] == player:
		if have_friends(line, x, y, size, player):
			prev_x = x - (x_exp - x)
			prev_y = y - (y_exp - y)
			if not (0 <= prev_x < size and 0 <= prev_y < size and line[prev_x + prev_y * size] == player):
				return False
		if 0 <= x_exp < size and 0 <= y_exp < size and line[x_exp + y_exp * size] == '0':
			return True
	else:
		if 0 <= x_exp < size and 0 <= y_exp < size and line[x_exp + y_exp * size] == '0':
			if bypass and x == size // 2 and y == size // 2:
				return True
			prev_x = x - (x_exp - x)
			prev_y = y - (y_exp - y)
			if 0 <= prev_x < size and 0 <= prev_y < size and line[prev_x + prev_y * size] == opponent:
				prev2_x = x - 2 * (x_exp - x)
				prev2_y = y - 2 * (y_exp - y)
				if 0 <= prev2_x < size and 0 <= prev2_y < size and line[prev2_x + prev2_y * size] == opponent:
					return True
	return False


def have_friends(line, x, y, size, player) -> bool:
	""" Check if the player has friends around him.
	:param line: the game as line.
	:param x: the starting x coordinate.
	:param y: the starting y coordinate.
	:param size: the grid size.
	:param player: the player value.
	:return: True if the player has friends, otherwise False.
	"""
	if 0 <= x - 1 < size and 0 <= y - 1 < size and line[(x - 1) + (y - 1) * size] == player:
		return True
	if 0 <= x < size and 0 <= y - 1 < size and line[x + (y - 1) * size] == player:
		return True
	if 0 <= x + 1 < size and 0 <= y - 1 < size and line[(x + 1) + (y - 1) * size] == player:
		return True
	if 0 <= x - 1 < size and 0 <= y < size and line[(x - 1) + y * size] == player:
		return True
	if 0 <= x + 1 < size and 0 <= y < size and line[(x + 1) + y * size] == player:
		return True
	if 0 <= x - 1 < size and 0 <= y + 1 < size and line[(x - 1) + (y + 1) * size] == player:
		return True
	if 0 <= x < size and 0 <= y + 1 < size and line[x + (y + 1) * size] == player:
		return True
	if 0 <= x + 1 < size and 0 <= y + 1 < size and line[(x + 1) + (y + 1) * size] == player:
		return True
	return False
