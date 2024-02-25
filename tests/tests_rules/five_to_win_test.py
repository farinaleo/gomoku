#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import gomoku as gmk


def test_col1():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 0, 'q', [gmk.five_to_win])
	grid.add_rock(1, 1, 'q', [gmk.five_to_win])
	grid.add_rock(2, 2, 'q', [gmk.five_to_win])
	grid.add_rock(4, 4, 'q', [gmk.five_to_win])
	assert grid.add_rock(3, 3, 'q', [gmk.five_to_win]) == gmk.RuleStatus.WIN


def test_col2():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(4, 0, 'q', [gmk.five_to_win])
	grid.add_rock(3, 1, 'q', [gmk.five_to_win])
	grid.add_rock(2, 2, 'q', [gmk.five_to_win])
	grid.add_rock(1, 3, 'q', [gmk.five_to_win])
	assert grid.add_rock(0, 4, 'q', [gmk.five_to_win]) == gmk.RuleStatus.WIN


def test_row():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 0, 'q', [gmk.five_to_win])
	grid.add_rock(1, 0, 'q', [gmk.five_to_win])
	grid.add_rock(2, 0, 'q', [gmk.five_to_win])
	grid.add_rock(4, 0, 'q', [gmk.five_to_win])
	assert grid.add_rock(3, 0, 'q', [gmk.five_to_win]) == gmk.RuleStatus.WIN


def test_line():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 1, 'q', [gmk.five_to_win])
	grid.add_rock(0, 2, 'q', [gmk.five_to_win])
	grid.add_rock(0, 3, 'q', [gmk.five_to_win])
	assert grid.add_rock(0, 4, 'q', [gmk.five_to_win]) == gmk.RuleStatus.WIN


def test_row_f():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 0, 'q', [gmk.five_to_win])
	grid.add_rock(1, 0, 'q', [gmk.five_to_win])
	grid.add_rock(2, 0, 'q', [gmk.five_to_win])
	grid.add_rock(4, 0, 'q', [gmk.five_to_win])
	assert grid.add_rock(5, 0, 'q', [gmk.five_to_win]) == gmk.RuleStatus.OK


def test_line_f():
	grid = gmk.Grid(19)
	grid.add_rock(8, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 0, 'q', [gmk.five_to_win])
	grid.add_rock(0, 1, 'q', [gmk.five_to_win])
	grid.add_rock(0, 2, 'q', [gmk.five_to_win])
	grid.add_rock(0, 3, 'q', [gmk.five_to_win])
	assert grid.add_rock(0, 5, 'q', [gmk.five_to_win]) == gmk.RuleStatus.OK
