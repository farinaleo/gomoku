import copy
import math

import gomoku as gmk
import gomoku.game_rules as rules


def five_to_win(row: int, col: int, player, grid) -> rules.RuleStatus:
	"""Check if the next move is winning by aligning five stones or more
	:return: Rule status (WIN | OK | NO)
	"""
	goal = [player for _ in range(5)]
	goal = ''.join(goal)
	if __check_row(row, goal, grid) == rules.RuleStatus.WIN:
		print('WIN')
		return rules.RuleStatus.WIN
	elif __check_column(col, goal, grid) == rules.RuleStatus.WIN:
		print('WIN')
		return rules.RuleStatus.WIN
	elif __check_diagonal1(row, col, goal, grid) == rules.RuleStatus.WIN:
		print('WIN')
		return rules.RuleStatus.WIN
	elif __check_diagonal2(row, col, goal, grid) == rules.RuleStatus.WIN:
		print('WIN')
		return rules.RuleStatus.WIN

	print('LOOSE')
	return rules.RuleStatus.OK


def __check_column(col: int, goal, grid) -> rules.RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in column.
	:param col: column to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	col = ''.join(str(line[col]) for line in grid)
	if goal in col:
		return rules.RuleStatus.WIN
	else:
		return rules.RuleStatus.NO


def __check_row(row: int, goal, grid) -> rules.RuleStatus:
	"""Check if the next move is winning by aligning five stones or more in row.
	:param row:  row to analyse
	:param goal: goal line
	:param grid: grid to analyse
	:return: Rule status (WIN | NO)
	"""
	line = ''.join(str(char) for char in grid[row])
	if goal in line:
		return rules.RuleStatus.WIN
	else:
		return rules.RuleStatus.NO


def __check_diagonal1(row: int, col: int, goal, grid) -> rules.RuleStatus:
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
		return rules.RuleStatus.WIN
	return rules.RuleStatus.NO


def __check_diagonal2(row: int, col: int, goal, grid) -> rules.RuleStatus:
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
	print('goal')
	print(goal)
	print('diagonal')
	print(diagonal)
	if goal in diagonal:
		return rules.RuleStatus.WIN
	return rules.RuleStatus.NO
