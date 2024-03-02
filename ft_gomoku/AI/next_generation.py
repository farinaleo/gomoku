#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 11:13 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import copy
from ft_gomoku import Grid, RuleStatus


def next_generation(grid: Grid, rules, player1=True):
	"""Generate the next generation from the given grid by placing the player.
	:param grid: the grid to extend
	:param rules: the rules aplay to the game
	:param player1: True if the new generation is with the first player, otherwise False
	:return: a list of ft_gomoku.grid representing the next generation
	"""
	i = 0
	new_gen = []
	line = grid.get_line()
	size = grid.get_size()
	line_size = len(line)
	player, opponent = (grid.get_player1(), grid.get_player2()) if player1 else (grid.get_player2(), grid.get_player1())

	while i < line_size:
		if line[i] != player and line[i] != opponent:
			_next = copy.deepcopy(grid)
			if _next.add_rock(i // size, i % size, player, rules) != RuleStatus.NO:
				new_gen.append(_next)
		i += 1

	return new_gen
