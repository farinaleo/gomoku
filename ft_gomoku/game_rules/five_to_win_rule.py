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
	grid_tab = grid.line_grid
	size = grid.size
	if __check_row(row, col, goal, grid_tab, size) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_column(row, col, goal, grid_tab, size) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_diagonal1(row, col, goal, grid_tab, size) == RuleStatus.WIN:
		return RuleStatus.WIN
	elif __check_diagonal2(row, col, goal, grid_tab, size) == RuleStatus.WIN:
		return RuleStatus.WIN

	return RuleStatus.OK


def __check_column(row: int, col: int, goal, grid, size) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in column.
	:param col: column to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	line = ''.join([str(grid[col + i * size]) for i in range(size)])
	if goal in line:
		return RuleStatus.WIN
	else:
		return RuleStatus.NO


def __check_row(row: int, col: int, goal, grid, size) -> RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in row.
	:param row:  row to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	line = ''.join([str(grid[i + (row * size)]) for i in range(size)])
	if goal in line:
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
	while 0 <= row < size and 0 <= col < size:
		row = row - 1
		col = col - 1
	row = row + 1
	col = col + 1

	diagonal = ''.join([str(grid[(col + i) + (row + i) * size]) for i in range(min(size - row, size - col))])
	if goal in diagonal:
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
	while 0 <= row < size and 0 <= col < size:
		row = row + 1
		col = col - 1
	row = row - 1
	col = col + 1

	diagonal = ''.join([str(grid[(col + i) + (row - i) * size]) for i in range(min(row + 1, size - col))])
	if goal in diagonal:
		return RuleStatus.WIN
	return RuleStatus.NO
