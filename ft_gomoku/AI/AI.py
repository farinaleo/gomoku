#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:17 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.grid.grid import Grid
from ft_gomoku.AI import get_priority, launch_alpha_beta


def run_ia(grid: Grid, rules) -> tuple | None:
	"""
	Main function for the IA.
	It runs the proper algorithm according to the situation.
	:param grid: The game.
	:param rules: The game rules set.
	:return: a tuple as (x, y) for the move to player or None in case of error.
	"""
	# get the opponent last move mvOp
	# get the ia last move mvAi
	#
	# if is_critical(mvOp):
	#   return algo(depth 1) // defend
	# if is_critical(mvAi):
	#   return algo(depth 1) // win
	# else :
	#   return algo(depth > 1) // attack
	depth = 3
	priority = get_priority(grid)
	if priority != 0:
		depth = 1
	return launch_alpha_beta(grid, depth, float('-inf'), float('inf'), rules)
