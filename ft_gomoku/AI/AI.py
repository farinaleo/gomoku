#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:17 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid


def run_ia(grid: Grid, ia, opponent) -> tuple | None:
	"""
	Main function for the IA.
	It runs the proper algorithm according to the situation.
	:param grid: The game.
	:param ia: The ia value form the grid.
	:param opponent: The opponent value from the grid.
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
