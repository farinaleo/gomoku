#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import copy
import math

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
	goal = [player for _ in range(5)]
	goal = ''.join(goal)
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
	max_v = max(row, col)
	y = row - max_v
	x = col - max_v
	size = len(grid)
	diagonal = ''
	if y < 0:
		y += int(math.fabs(y))
		x += int(math.fabs(y))
	elif x < 0:
		x += int(math.fabs(x))
		y += int(math.fabs(x))

	while y < size and x < size:
		diagonal += str(grid[y][x])
		y += 1
		x += 1
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
	diagonal = ''
	while 0 <= y < size and 0 <= x < size:
		y += 1
		x -= 1
	y -= 1
	x += 1
	while 0 <= y < size and 0 <= x < size:
		diagonal += str(grid[y][x])
		y -= 1
		x += 1
	if goal in diagonal:
		return RuleStatus.WIN
	return RuleStatus.NO
