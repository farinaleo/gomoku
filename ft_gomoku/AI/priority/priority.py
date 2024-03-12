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


def get_priority(grid: Grid) -> int:
	"""
	Evaluate the priority according to the IA and opponent last moves.
	:param grid: the game.
	:return: 2 if the IA has to block the opponent,
	1 if the IA can win with one move, 0 otherwise.
	"""
	# is in a four alignment (or three)
	# has captured 8 opponent stones and can capture 2 more.
	priority = max(ia_priority(grid), opponent_priority(grid))
	print(f'priority: {priority}')
	return priority


def ia_priority(grid: Grid) -> int:
	"""evaluate the IA priority according to its last move.
	:param grid: the game.
	:return: the priority rate.
	"""
	ia_last_move = grid.get_last_move()
	if not ia_last_move:
		return 0
	p_4 = matching_cases(grid.line_grid, grid, ia_last_move[1],
							ia_last_move[2], grid.player1, grid.player2,
							grid.size, grid.size ** 2, [3, 4], False)
	if p_4 > 0:
		return 1
	return 0


def opponent_priority(grid: Grid) -> int:
	"""evaluate the IA priority according to its last move.
	:param grid: the game.
	:return: the priority rate.
	"""
	opponent_last_move = grid.get_last_move()
	if not opponent_last_move:
		return 0
	p_4 = matching_cases(grid.line_grid, grid, opponent_last_move[1],
							opponent_last_move[2], grid.player2, grid.player1,
							grid.size, grid.size ** 2, [3, 4], False)
	if p_4 > 0:
		return 2
	return 0
