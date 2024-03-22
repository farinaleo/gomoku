#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:17 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import os
from ft_gomoku import Grid
from ft_gomoku.AI import get_priority, launch_alpha_beta, launch_alpha_beta_hard, launch_pvs, launch_alpha_beta_thread


def run_ai(grid: Grid, rules, ai_value='1', opponent_value='2', depth=10) -> tuple | None:
	"""
	Main function for the IA.
	It runs the proper algorithm according to the situation.
	:param grid: The game.
	:param rules: The game rules set.
	:param ai_value: The value associated with the AI (default '1').
	:param opponent_value: The value associated with the opponent (default '2').
	:param depth: depth of analysis.
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
	# depth = 10   # %2=1 to target IA

	algo = os.getenv('GOMOKU_ALGO')

	priority = get_priority(grid, ai_value, opponent_value)
	if priority != 0:
		depth = 11
	if algo == 'PVS':
		return launch_pvs(grid, depth, float('-inf'), float('inf'), rules, ai_value=ai_value)
	elif algo == 'ALPHA_HARD':
		return launch_alpha_beta_hard(grid, depth, float('-inf'), float('inf'), rules, ai_value=ai_value)
	elif algo == 'ALPHA_THREAD':
		return launch_alpha_beta_thread(grid, depth, float('-inf'), float('inf'), rules, ai_value=ai_value)
	else:
		return launch_alpha_beta(grid, depth, float('-inf'), float('inf'), rules, ai_value=ai_value)
