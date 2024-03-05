#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 9:03 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk


def test_1_1(): # double free three in an angle as angle
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(0, 1, 'q', [])
	grid.add_rock(0, 2, 'q', [])
	grid.add_rock(1, 0, 'q', [])
	grid.add_rock(2, 0, 'q', [])
	
	assert grid.add_rock(0, 0, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.NO


def test_1_2():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(0, 1, 'q', [])
	grid.add_rock(0, 2, 'q', [])
	grid.add_rock(1, 0, 'q', [])
	grid.add_rock(2, 0, 'q', [])
	grid.add_rock(3, 0, 'a', [])    # same as test 1 but with a free three blocked

	assert grid.add_rock(0, 0, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_1_3():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(0, 1, 'q', [])
	grid.add_rock(0, 2, 'q', [])
	grid.add_rock(1, 0, 'q', [])
	grid.add_rock(2, 0, 'q', [])
	grid.add_rock(1, 1, 'a', [])    # same as test 1.1 but with a capture
	grid.add_rock(2, 2, 'a', [])
	grid.add_rock(3, 3, 'q', [])

	assert grid.add_rock(0, 0, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_2_1(): # double free three in the middle as angle
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 7, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(6, 8, 'q', [])
	grid.add_rock(9, 8, 'q', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.NO


def test_2_2():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 7, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(6, 8, 'q', [])
	grid.add_rock(9, 8, 'q', [])
	grid.add_rock(8, 9, 'a', [])  # same as test 2.1 but with a free three blocked
	grid.add_rock(8, 5, 'a', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_2_3():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 7, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(6, 8, 'q', [])
	grid.add_rock(9, 8, 'q', [])
	grid.add_rock(9, 9, 'a', [])    # same as test 2.1 but with a capture
	grid.add_rock(10, 10, 'a', [])
	grid.add_rock(11, 11, 'q', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK

def test_3_1(): # double free three in the middle as line
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 5, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(8, 10, 'q', [])
	grid.add_rock(8, 11, 'q', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.NO

def test_3_2():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 5, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(8, 10, 'q', [])
	grid.add_rock(8, 11, 'q', [])
	grid.add_rock(8, 9, 'a', [])  # same as test 3.1 but with a free three blocked

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK

def test_3_3():
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 5, 'q', [])
	grid.add_rock(8, 6, 'q', [])
	grid.add_rock(8, 10, 'q', [])
	grid.add_rock(8, 11, 'q', [])
	grid.add_rock(9, 9, 'a', [])  # same as test 3.1 but with a capture
	grid.add_rock(10, 10, 'a', [])
	grid.add_rock(11, 11, 'q', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK

def test_4_1(): # one three
	grid = gmk.Grid(19, 'a', 'q')
	grid.add_rock(8, 5, 'q', [])
	grid.add_rock(8, 6, 'q', [])

	assert grid.add_rock(8, 8, 'q', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK