#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:19 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import log
from ft_gomoku.grid.grid import Grid
from ft_gomoku.AI import heuristic, next_generation

@log()
def alpha_beta(grid: Grid, depth: int, alpha: float, beta: float, rules, is_max=True) -> float | None:
	"""
	Alpha Beta pruning algorithm. Uses it to find the best move to play
	to win the game.
	:param grid: the game board.
	:param depth: the depth to explore.
	:param alpha: the alpha limit.
	:param beta:  the beta limit.
	:param rules: game rules
	:param is_max: True if the turn is for the IA otherwise False.
	:return: The node evaluation or None in case of error.
	"""
	if depth == 0 or grid.winning:
		return heuristic(grid, grid.player1 if is_max else grid.player2)
	next_gen = next_generation(grid, rules, grid.player1 if is_max else grid.player2)
	if not next_generation:
		return None
	if is_max:
		max_val = float('-inf')
		for node in next_gen:
			_val = alpha_beta(node, depth - 1, alpha, beta, rules, False)
			max_val = max(max_val, _val)
			alpha = max(alpha, max_val)
			if max_val >= beta:
				break
	else:
		max_val = float('+inf')
		for node in next_gen:
			_val = alpha_beta(node, depth - 1, alpha, beta, rules)
			max_val = min(max_val, _val)
			beta = min(beta, max_val)
			if max_val <= alpha:
				break
	return max_val


def launch_alpha_beta(grid: Grid, depth: int, alpha: float, beta: float, rules, is_max=True) -> tuple | None:
	"""
	Launch the alpha beta pruning to find the best move to play.
	:param grid: the game board.
	:param depth: the depth to explore.
	:param alpha: the alpha limit.
	:param beta:  the beta limit.
	:param rules: game rules.
	:param is_max: True if the turn is for the IA otherwise False.
	:return: the move (x, y) as tuple or None in case of error.
	"""
	if depth <= 0:
		return None
	next_gen = next_generation(grid, rules, grid.player1 if is_max else grid.player2)
	max_val = float('-inf')
	move_selected = next_gen[0].get_last_move()[-2:]
	for node in next_gen:
		_val = alpha_beta(node, depth - 1, alpha, beta, rules, is_max)
		if _val > max_val:
			max_val = _val
			move_selected = node.get_last_move()[-2:]
	return move_selected
