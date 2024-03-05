#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/2/24, 11:15 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import math
import numpy as np
from ft_gomoku import Grid, RuleStatus

rules_nb = 3
col_g = None
row_g = None
diag1_g = None
diag2_g = None


def evaluate(grid: Grid) -> float:
	"""
	Evaluate the node to have its interesting value.
	:param grid: the node to evaluate.
	:return: the score of the node.
	"""
	score = 0

	player, x, y = grid.get_last_move()
	opponent = grid.get_player1() if player != grid.get_player1() else grid.get_player2()
	line = grid.get_line()
	tab = grid.get_grid()
	size = grid.get_size()
	# mid = (size // 2, size // 2)

	score += __count_player(line, player, opponent)
	score += __allies_captured(grid.get_captured_stones(player))
	score += __opponents_captured(grid.get_captured_stones(opponent))
	score += __far_from_allies_last_moves(player, x, y, grid, 3)
	score += __far_from_opponent_last_moves(opponent, x, y, grid, 3)
	score += __align_n(tab, line, 4, player, y, x, size, True)
	score += __align_n(tab, line, 3, player, y, x, size)
	score += __align_n(tab, line, 2, player, y, x, size)

	return score


# Each rules have to return a rate between 0 and 1.
# the more the rate is near to 1 to more the rule is interesting.

def __count_player(line: np.ndarray, player, opponent) -> float:
	"""Count the number of player in the grid.
	:param line: the grid as line
	:param player: the player to search
	:return: the rate of the player among the players.
	"""
	count_p = np.sum(np.char.count(line, player))
	count_o = np.sum(np.char.count(line, opponent))
	if count_p + count_o == 0:
		return 0

	return (count_o + count_p) ** float(-1 * count_p)


def __allies_captured(captured) -> float:
	"""Count the number of allies captured during the game.
	:param captured: the number of allies captured.
	:return: (10 - (allies captured)) / 10
	"""
	return 10 ** float(-1 * (10 - captured))


def __opponents_captured(captured) -> float:
	"""Count the number of opponents captured during the game.
	:param captured: the number of opponents captured.
	return: (opponents captured) / 10
	"""
	if captured == 10:
		return rules_nb
	return 10 ** float(-1 * captured)


def __far_from_opponent_last_moves(opponent, x, y, grid, n=1):
	"""Calculate the rate corresponding of the distance between the
	opponent and the last move of the player.
	:param opponent: the opponent type
	:param x: the coordinates of the last move
	:param y: the coordinates of the last move
	:param grid: the game
	:param n: the number of moves to select
	:return: a rate as 1/(dist op-pl)
	"""
	cnt = 0
	sum_dist = 0
	i = 0
	while i < n:
		op_move = grid.get_last_move(opponent, i + 1)
		if op_move is None:
			break
		else:
			cnt = cnt + 1
			sum_dist = sum_dist + int((math.sqrt((x - op_move[1]) ** 2 + (y - op_move[2]) ** 2)))
		i = i + 1
	if cnt == 0:
		return 1
	return sum_dist ** float(-1 * cnt)


def __far_from_allies_last_moves(allie, x, y, grid, n=1):
	"""Calculate the rate corresponding of the distance between the
	allies and the last move of the player.
	:param allie: the allie type
	:param x: the coordinates of the last move
	:param y: the coordinates of the last move
	:param grid: the game
	:param n: the number of moves to select
	:return: a rate as 1/(dist op-pl)
	"""
	cnt = 0
	sum_dist = 0
	for i in range(n):
		op_move = grid.get_last_move(allie, i + 2)
		if op_move is None:
			break
		else:
			cnt = cnt + 1
			sum_dist = sum_dist + (math.sqrt((x - op_move[1]) ** 2 + (y - op_move[2]) ** 2))
	if cnt == 0:
		return 1
	return sum_dist ** float(-1 * cnt)


def __align_n(tab, line, n, player, row, col, size, first_call=False):
	"""Count the n alignment of the player
	:param grid: the grid game
	:param player: the player type
	:return: the number of aligned possibilities.
	"""
	global col_g, row_g, diag1_g, diag2_g
	if first_call:
		col_g, row_g, diag1_g, diag2_g = None, None, None, None
	count = 0
	goal = ''.join([str(player) for i in range(n)])
	if __check_row(row, goal, tab) == RuleStatus.WIN:
		count = count + 1
	elif __check_column(col, goal, tab) == RuleStatus.WIN:
		count = count + 1
	elif __check_diagonal1(row, col, goal, line, size) == RuleStatus.WIN:
		count = count + 1
	elif __check_diagonal2(row, col, goal, line, size) == RuleStatus.WIN:
		count = count + 1
	if n == 5 and count > 0:
		return 10000
	return count ** -1 if count else count


def __check_column(col: int, goal, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in column.
	:param col: column to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	global col_g
	if col_g is None:
		col_g = ''.join(str(line[col]) for line in grid)
	if goal in col_g:
		return RuleStatus.WIN
	else:
		return RuleStatus.NO


def __check_row(row: int, goal, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in row.
	:param row:  row to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	global row_g
	if row_g is None:
		row_g = ''.join(str(char) for char in grid[row])
	if goal in row_g:
		return RuleStatus.WIN
	else:
		return RuleStatus.NO


def __check_diagonal1(row: int, col: int, goal, grid, size) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in a diagonal.
	:param row:  y pos
	:param col:  x pos
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	global diag1_g
	max_v = max(row, col)
	y = row - max_v
	x = col - max_v

	if y < 0:
		y = y + int(math.fabs(y))
		x = x + int(math.fabs(y))
	elif x < 0:
		x = x + int(math.fabs(x))
		y = y + int(math.fabs(x))

	if diag1_g is None:
		diag1_g = ''.join([str(grid[(y + i) * size + x + i]) for i in range(min(size - y, size - x))])
	if goal in diag1_g:
		return RuleStatus.WIN
	return RuleStatus.NO


def __check_diagonal2(row: int, col: int, goal, grid, size) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in a diagonal.
	:param row:  y pos
	:param col:  x pos
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	global diag2_g
	x = col
	y = row

	while 0 <= y < size and 0 <= x < size:
		y = y + 1
		x = x - 1
	y = y - 1
	x = x + 1

	if diag2_g is None:
		diag2_g = ''.join([str(grid[(y - i) * size + x + i]) for i in range(min(y + 1, size - x))])
	if goal in diag2_g:
		return RuleStatus.WIN
	return RuleStatus.NO
