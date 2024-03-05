#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import RuleStatus, rule


@rule()
def five_to_win(row: int, col: int, player, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more
	:param row: y pos
	:param col: x pos
	:param player: who played the move
	:param grid: the grid
	:return: Rule status (WIN | OK | NO)
	"""
	goal = f'{player}{player}{player}{player}{player}'
	grid_tab = grid.get_grid()
	if __check_row(row, goal, grid_tab) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_column(col, goal, grid_tab) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_diagonal1(row, col, goal, grid_tab) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_diagonal2(row, col, goal, grid_tab) == RuleStatus.WIN:
		return RuleStatus.WIN

	return RuleStatus.OK


def __check_column(col: int, goal, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in column.
	:param col: column to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	col = ''.join(str(line[col]) for line in grid)
	if goal in col:
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
	line = ''.join(str(char) for char in grid[row])
	if goal in line:
		return RuleStatus.WIN
	else:
		return RuleStatus.NO


def __check_diagonal1(row: int, col: int, goal, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in a diagonal.
	:param row:  y pos
	:param col:  x pos
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	x = col
	y = row
	size = len(grid)
	while 0 <= y < size and 0 <= x < size:
		y = y - 1
		x = x - 1
	y = y + 1
	x = x + 1

	diagonal = ''.join([str(grid[y + i][x + i]) for i in range(min(size - y, size - x))])

	if goal in diagonal:
		return RuleStatus.WIN
	return RuleStatus.NO


def __check_diagonal2(row: int, col: int, goal, grid) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in a diagonal.
	:param row:  y pos
	:param col:  x pos
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	x = col
	y = row
	size = len(grid)
	while 0 <= y < size and 0 <= x < size:
		y = y + 1
		x = x - 1
	y = y - 1
	x = x + 1

	diagonal = ''.join([str(grid[y - i][x + i]) for i in range(min(y + 1, size - x))])

	if goal in diagonal:
		return RuleStatus.WIN
	return RuleStatus.NO
