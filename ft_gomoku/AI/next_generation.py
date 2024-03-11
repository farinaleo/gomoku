#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 11:13 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import ctypes

from ft_gomoku import Grid, RuleStatus

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def next_generation(grid: Grid, rules, player1=True):
	"""Generate the next generation from the given grid by placing the player.
	:param grid: the grid to extend
	:param rules: the rules aplay to the game
	:param player1: True if the new generation is with the first player, otherwise False
	:return: a list of ft_gomoku.grid representing the next generation
	"""
	new_gen = []
	line = grid.line_grid
	size = grid.size
	line_size = len(line)
	player, opponent = (grid.player1, grid.player2) if player1 else (grid.player2, grid.player1)

	cluster = __cluster(line, size, line_size, player, opponent)
	for cell in cluster:
		if (line[cell[0] + cell[1] * size] == '0'
				and 0 <= cell[0] < size
				and 0 <= cell[1] < size):
			_next = grid.__copy__()
			if _next.add_rock(row=cell[1], col=cell[0], player=player, rules=rules) != RuleStatus.NO:
				# _rate = evaluate(_next)
				new_gen.append(_next)
	return new_gen


def __cluster(line, size, line_size, p1, p2):
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
			if line[i] == p2 and x != size // 2 and y != size // 2:
				if (line[_left + _up * size] != p2
					and line[x + _up * size] != p2
					and line[_right + _up * size] != p2
					and line[_left + y * size] != p2
					and line[_right + y * size] != p2
					and line[_left + _down * size] != p2
					and line[x + _down * size] != p2
					and line[_right + _down * size] != p2):
					i = i + 1
					continue

			# up left
			if 0 <= _left < size and 0 <= _up < size and line[_left + _up * size] == '0':
				cluster.append((_left, _up))
			# up mid
			if 0 <= x < size and 0 <= _up < size and line[x + _up * size] == '0':
				cluster.append((x, _up))
			# up right
			if 0 <= _right < size and 0 <= _up < size and line[_right + _up * size] == '0':
				cluster.append((_right, _up))
			# mid left
			if 0 <= _left < size and 0 <= y < size and line[_left + y * size] == '0':
				cluster.append((_left, y))
			# mid right
			if 0 <= _right < size and 0 <= y < size and line[_right + y * size] == '0':
				cluster.append((_right, y))
			# down left
			if 0 <= _left < size and 0 <= _down < size and line[_left + _down * size] == '0':
				cluster.append((_left, _down))
			# down mid
			if 0 <= x < size and 0 <= _down < size and line[x + _down * size] == '0':
				cluster.append((x, _down))
			# down right
			if 0 <= _right < size and 0 <= _down < size and line[_right + _down * size] == '0':
				cluster.append((_right, _down))
		i = i + 1
	if len(cluster) == 0:
		mid = size // 2
		cluster.append((mid, mid))
	return cluster
