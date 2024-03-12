#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:20 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid
from ft_gomoku.AI import matching_cases, near_to_border, capture_stones, winning

# these global must be built as [(func, rate), ...] to be called correctly.
# each function must be built as func(line, grid, x, y, player, opponent, size, line_size) -> float.
g_func_player = [(matching_cases, 1),
					(near_to_border, 1),
					(capture_stones, 1),
					(winning, 1)]
g_func_opponent = [(matching_cases, -1),
					(near_to_border, -1),
					(capture_stones, -1),
					(winning, -1)]


def heuristic(node: Grid, player) -> float:
	"""Compute the heuristic value of the node according to the last move.
	:param node: the node to evaluate.
	:param player: the player who placed the last stone.
	:return: the heuristic value (h(node)).
	"""
	h_total = 0
	node_line = node.line_grid
	node_size = node.size
	opponent = node.player1 if player == node.player2 else node.player2
	node_line_size = node_size * node_size  # the grid is a square
	p_x, p_y = node.get_last_move()[-2:]
	func_player = g_func_player
	func_opponent = g_func_opponent

	for func in func_player:
		h_total = h_total + func[0](node_line, node, p_x, p_y, player, opponent, node_size, node_line_size) * func[1]

	op_mv = node.get_last_move(opponent)  # try to evaluate stone that could be captured
	if op_mv:
		op_x, op_y = op_mv[-2:]
		for func in func_opponent:
			h_total = h_total + func[0](node_line, node, op_x, op_y, opponent, player, node_size, node_line_size) * \
						func[1]

	return h_total
