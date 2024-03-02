#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/2/24, 10:41 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk


def test_1():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], True)
	result = ['1', 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0]
	assert res[0].get_line() == result

def test_2():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], False)
	result = [0, '2', 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0]
	assert res[1].get_line() == result

def test_3():
	grid = gmk.Grid(5, '1', '2')
	res = gmk.next_generation(grid, [], True)
	result = [0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, '1']
	assert res[-1].get_line() == result

def test_4():
	grid = gmk.Grid(5, '1', '2')
	grid.add_rock(0, 0, '1', [])
	res = gmk.next_generation(grid, [], False)
	result = ['1', '2', 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0,
	          0, 0, 0, 0, 0]
	assert res[0].get_line() == result