#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/12/24, 8:21 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid

def winning(line, grid, x, y, player, opponent, size, line_size) -> float:
	"""Evaluate if the move is winning.
	:param line: the game as list.
	:param grid: the node.
	:param x: last move played.
	:param y: last move played.
	:param player: player who played the move to evaluate.
	:param opponent: the opponent.
	:param size: the grid size.
	:param line_size: the total lien size.
	:return: return 10 if the move is winning otherwise 0.
	"""
	if grid.winning:
		return 100000000
	return 0
