#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 11:13 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid, RuleStatus, evaluate


def next_generation(grid: Grid, rules, player1=True):
	"""Generate the next generation from the given grid by placing the player.
	:param grid: the grid to extend
	:param rules: the rules aplay to the game
	:param player1: True if the new generation is with the first player, otherwise False
	:return: a list of ft_gomoku.grid representing the next generation
	"""
	new_gen = []
	line = grid.get_line()
	size = grid.get_size()
	line_size = len(line)
	player, opponent = (grid.get_player1(), grid.get_player2()) if player1 else (grid.get_player2(), grid.get_player1())

	cluster = __cluster(line, size, line_size)
	for cell in cluster:
		if (line[cell[0] + cell[1] * size] == '0'
				and 0 <= cell[0] < size
				and 0 <= cell[1] < size):
			_next = grid.__copy__()
			if _next.add_rock(row=cell[1], col=cell[0], player=player, rules=rules) != RuleStatus.NO:
				_rate = evaluate(_next)
				new_gen.append((_next, _rate))
	return new_gen


def __cluster(line, size, line_size):
	cluster = []

	y = 0
	x = 0
	while y < size:
		x = 0
		while x < size:
			if line[x + y * size] != '0':
				_up = y - 1
				_down = y + 1
				_left = x - 1
				_right = x + 1
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
			x = x + 1
		y = y + 1
	if len(cluster) == 0:
		mid = size // 2
		cluster.append((mid, mid))
	return cluster
