#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 3:17 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid


def near_to_border(line, grid, x, y, player, opponent, size, line_size) -> float:
	"""Evaluate if the move is to close to the border.
	:param line: the game as list.
	:param grid: the node.
	:param x: last move played.
	:param y: last move played.
	:param player: player who played the move to evaluate.
	:param opponent: the opponent.
	:param size: the grid size.
	:param line_size: the total lien size.
	:return: the evaluated rate of the move.
	"""
	count = 0
	if x < 5:
		count = count + (5 - x)
	if y < 5:
		count = count + (5 - y)
	if x > size - 5:
		count = count + (5 - size - x)
	if y > size - 5:
		count = count + (5 - size - y)
	return count