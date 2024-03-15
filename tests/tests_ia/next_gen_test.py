#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/2/24, 1'0':41 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2'0'24.

import ft_gomoku as gmk


def test_1():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], True)
	result = ['0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '1', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0']
	assert res[0].line_grid == result


def test_2():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], False)
	result = ['0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '2', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0']
	assert res[0].line_grid == result


def test_3():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], True)
	result = ['0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '1', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0']
	assert res[-1].line_grid == result


def test_4():
	grid = gmk.Grid(5, '1', '2')
	grid.add_rock(0, 0, '1', [])
	res = gmk.next_generation(grid, [], False)
	result = ['1', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '2', '0', '0',
	          '0', '0', '0', '0', '0',
	          '0', '0', '0', '0', '0']
	assert res[0].line_grid == result
