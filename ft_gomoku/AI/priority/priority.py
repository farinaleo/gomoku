#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:19 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku import Grid
from ft_gomoku.AI import matching_cases


def get_priority(grid: Grid, ai_value, opponent_value) -> int:
	"""
	Evaluate the priority according to the IA and opponent last moves.
	:param grid: the game.
	:param ai_value: the value associated with the AI.
	:param opponent_value: the value associated with the opponent.
	:return: 2 if the IA has to block the opponent,
	1 if the IA can win with one move, 0 otherwise.
	"""
	# is in a four alignment (or three)
	# has captured 8 opponent stones and can capture 2 more.
	print("PY IA", ia_priority(grid, ai_value, opponent_value), "OPPONENT", opponent_priority(grid, ai_value, opponent_value))
	priority = max(ia_priority(grid, ai_value, opponent_value), opponent_priority(grid, ai_value, opponent_value))
	return priority


def ia_priority(grid: Grid, ai_value, opponent_value) -> int:
	"""evaluate the IA priority according to its last move.
	:param grid: the game.
	:param ai_value: the value associated with the AI.
	:param opponent_value: the value associated with the opponent.
	:return: the priority rate.
	"""
	ia_last_move = grid.get_last_move(ai_value)
	if not ia_last_move:
		return 0
	p_4 = matching_cases(grid.line_grid, grid, ia_last_move[1],
							ia_last_move[2], ai_value, opponent_value,
							grid.size, grid.size ** 2, [3, 4], False)

	print("! -- py P4", p_4)
	if p_4 > 0:
		return 1
	return 0


def opponent_priority(grid: Grid, ai_value, opponent_value) -> int:
	"""evaluate the IA priority according to its last move.
	:param grid: the game.
	:param ai_value: the value associated with the AI.
	:param opponent_value: the value associated with the opponent.
	:return: the priority rate.
	"""
	opponent_last_move = grid.get_last_move(opponent_value)
	if not opponent_last_move:
		return 0
	p_4 = matching_cases(grid.line_grid, grid, opponent_last_move[1],
							opponent_last_move[2], opponent_value, ai_value,
							grid.size, grid.size ** 2, [3, 4], False)
	if p_4 > 0:
		return 2
	return 0
