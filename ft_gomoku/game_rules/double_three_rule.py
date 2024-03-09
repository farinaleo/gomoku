#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku import RuleStatus, rule, capture

extract_size = 6
goal_32 = ''
goal_33 = ''
goal_211 = ''
goal_212 = ''
goal_121 = ''
goal_122 = ''
skip = ''
goal_31 = ''
goal_213 = ''
goal_123 = ''


@rule()
def double_three_forbidden(row: int, col: int, player, grid) -> RuleStatus:
	"""Check if the next move is making a double three or more
	:param row: y pos
	:param col: x pos
	:param player: who played the move
	:param grid: the grid
	:return: Rule status (WIN | OK | NO)
	"""
	cnt = 0
	lines = []
	parts = []
	size = grid.size
	grid_tab = grid.line_grid
	if capture(row, col, player, grid) == RuleStatus.CAPTURE:
		return RuleStatus.OK

	row_l = __extract_row(col, row, size, grid_tab, player)
	col_l = __extract_column(col, row, size, grid_tab, player)
	diag1_l = __extract_diagonal1(col, row, size, grid_tab, player)
	diag2_l = __extract_diagonal2(col, row, size, grid_tab, player)

	parts.extend(row_l[:2])
	parts.extend(col_l[:2])
	parts.extend(diag1_l[:2])
	parts.extend(diag2_l[:2])

	lines.extend([row_l[2], col_l[2], diag1_l[2], diag2_l[2]])

	i = 0
	while i < 8:
		cnt = cnt + __count_stone_trio_player_start(parts[i], player, True if i == 0 else False)
		i = i + 1
	i = 0
	while i < 4:
		cnt = cnt + __count_stone_trio_player_mid(lines[i], player, True if i == 0 else False)
		i = i + 1

	if cnt >= 2:
		return RuleStatus.NO
	else:
		return RuleStatus.OK


def __extract_column(col: int, row: int, size: int, grid, player):
	"""extract the line from the column and return it as a string
	:param col: column
	:param row: row
	:param size: size of the grid
	:param grid: the grind
	:param player: the player to keep
	:return: strings
	"""
	x = col
	y = row
	total = ''
	before = ''
	after = ''
	i = 0
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = str(grid[x + y * size]) + total
		before = str(grid[x + y * size]) + before
		x = x - 1
		i = i + 1
	after = after + str(player)
	x = col + 1
	i = 1
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = total + str(grid[x + y * size])
		after = after + str(grid[x + y * size])
		x = x + 1
		i = i + 1
	if before.count(player) < 2 or after.count(player) < 2:
		total = ''
	return before, after, total


def __extract_row(col: int, row: int, size: int, grid, player):
	"""extract the line from the row and return it as a string
	:param col: column
	:param row: row
	:param size: size of the grid
	:param grid: the grind
	:param player: the player to keep
	:return: strings
	"""
	x = col
	y = row
	total = ''
	before = ''
	after = ''
	i = 0
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = str(grid[x + y * size]) + total
		before = str(grid[x + y * size]) + before
		y = y - 1
		i = i + 1
	after = after + str(player)
	y = row + 1
	i = 1
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = total + str(grid[x + y * size])
		after = after + str(grid[x + y * size])
		y = y + 1
		i = i + 1
	if before.count(player) < 2 or after.count(player) < 2:
		total = ''
	return before, after, total


def __extract_diagonal1(col: int, row: int, size: int, grid, player):
	"""extract the line from the first diagonal and return it as a string
	:param col: column
	:param row: row
	:param size: size of the grid
	:param grid: the grind
	:param player: the player to keep
	:return: strings
	"""
	x = col
	y = row
	total = ''
	before = ''
	after = ''
	i = 0
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = str(grid[x + y * size]) + total
		before = str(grid[x + y * size]) + before
		y = y - 1
		x = x - 1
		i = i + 1
	after = after + str(player)
	x = col + 1
	y = row + 1
	i = 1
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == '0' or grid[x + y * size] == player):
		total = total + str(grid[x + y * size])
		after = after + str(grid[x + y * size])
		y = y + 1
		x = x + 1
		i = i + 1
	if before.count(player) < 2 or after.count(player) < 2:
		total = ''
	return before, after, total


def __extract_diagonal2(col: int, row: int, size: int, grid, player):
	"""extract the line from the second diagonal and return it as a string
	:param col: column
	:param row: row
	:param size: size of the grid
	:param grid: the grind
	:param player: the player to keep
	:return: strings
	"""
	x = col
	y = row
	total = ''
	before = ''
	after = ''
	i = 0
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == 0 or grid[x + y * size] == player):
		total = str(grid[x + y * size]) + total
		before = str(grid[x + y * size]) + before
		y = y + 1
		x = x - 1
		i = i + 1
	after = after + str(player)
	x = col + 1
	y = row - 1
	i = 1
	while 0 <= y < size and 0 <= x < size and i < extract_size and (grid[x + y * size] == 0 or grid[x + y * size] == player):
		total = total + str(grid[x + y * size])
		after = after + str(grid[x + y * size])
		y = y - 1
		x = x + 1
		i = i + 1
	if before.count(player) < 2 or after.count(player) < 2:
		total = ''
	return before, after, total


def __count_stone_trio_player_start(line: str, player, first_call=False) -> int:
	"""count the number of trio on the line.
	:param line: the line to explore
	:param player: the player
	:return: the count
	"""
	global goal_32, goal_33, goal_212, goal_211, goal_121, goal_122, skip
	size = len(line)

	if first_call:
		goal_32 = f'{player}{player}{player}00'
		goal_33 = f'00{player}{player}{player}'
		goal_211 = f'{player}{player}0{player}0'
		goal_212 = f'0{player}{player}0{player}'
		goal_121 = f'{player}0{player}{player}0'
		goal_122 = f'0{player}0{player}{player}'
		skip = f'{player}{player}{player}{player}'

	if size <= 3:
		return 0
	if skip in line:
		return 0

	if goal_32 in line or goal_33 in line:
		return 1
	elif goal_211 in line or goal_212 in line:
		return 1
	elif goal_121 in line or goal_122 in line:
		return 1
	return 0


def __count_stone_trio_player_mid(line: str, player, first_call=True) -> int:
	"""count the number of trio on the line.
	:param line: the line to explore
	:param player: the player
	:return: the count
	"""
	global goal_31, goal_213, goal_123, skip
	size = len(line)

	if first_call:
		goal_31 = f'0{player}{player}{player}0'
		goal_213 = f'0{player}{player}0{player}0'
		goal_123 = f'0{player}0{player}{player}0'
		skip = f'{player}{player}{player}{player}'

	if size <= 3:
		return 0
	if skip in line:
		return 0

	if goal_31 in line or goal_213 in line or goal_123 in line:
		return 1
	return 0

