#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/3/24, 6:44 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk
import numpy as np

rules = [
	gmk.five_to_win,
	gmk.double_three_forbidden,
	gmk.capture,
	gmk.ten_capture_to_win,
]

def test_col1():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 1, '2', rules)
	grid.add_rock(2, 2, '2', rules)
	grid.add_rock(4, 4, '2', rules)
	assert grid.add_rock(3, 3, '2', rules) == gmk.RuleStatus.WIN


def test_col11():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 1, '2', rules)
	grid.add_rock(2, 2, '2', rules)
	grid.add_rock(3, 3, '2', rules)
	grid.add_rock(5, 5, '2', rules)
	grid.add_rock(6, 6, '2', rules)
	assert grid.add_rock(4, 4, '2', rules) == gmk.RuleStatus.WIN


def test_col12():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 1, '2', rules)
	grid.add_rock(2, 2, '2', rules)
	grid.add_rock(3, 3, '2', rules)
	grid.add_rock(5, 5, '2', rules)
	assert grid.add_rock(4, 4, '2', rules) == gmk.RuleStatus.WIN


def test_col2():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(4, 0, '2', rules)
	grid.add_rock(3, 1, '2', rules)
	grid.add_rock(2, 2, '2', rules)
	grid.add_rock(1, 3, '2', rules)
	assert grid.add_rock(0, 4, '2', rules) == gmk.RuleStatus.WIN


def test_col21():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 4, '2', rules)
	grid.add_rock(3, 1, '2', rules)
	grid.add_rock(2, 2, '2', rules)
	grid.add_rock(1, 3, '2', rules)
	assert grid.add_rock(4, 0, '2', rules) == gmk.RuleStatus.WIN


def test_row():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 0, '2', rules)
	grid.add_rock(2, 0, '2', rules)
	grid.add_rock(4, 0, '2', rules)
	assert grid.add_rock(3, 0, '2', rules) == gmk.RuleStatus.WIN


def test_line():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(0, 1, '2', rules)
	grid.add_rock(0, 2, '2', rules)
	grid.add_rock(0, 3, '2', rules)
	assert grid.add_rock(0, 4, '2', rules) == gmk.RuleStatus.WIN


def test_row_f():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 0, '2', rules)
	grid.add_rock(2, 0, '2', rules)
	grid.add_rock(4, 0, '2', rules)
	assert grid.add_rock(5, 0, '2', rules) == gmk.RuleStatus.OK


def test_line_f():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 0, '2', rules)
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(0, 1, '2', rules)
	grid.add_rock(0, 2, '2', rules)
	grid.add_rock(0, 3, '2', rules)
	assert grid.add_rock(0, 5, '2', rules) == gmk.RuleStatus.OK


def test_1():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(0, 1, '1', rules)
	grid.add_rock(0, 2, '1', rules)
	grid.add_rock(0, 3, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_2():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 0, '1', rules)
	grid.add_rock(2, 0, '1', rules)
	grid.add_rock(3, 0, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_3():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(1, 1, '1', rules)
	grid.add_rock(2, 2, '1', rules)
	grid.add_rock(3, 3, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2'])
	assert np.array_equal(line, goal)


def test_4():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 3, '2', rules)
	grid.add_rock(1, 2, '1', rules)
	grid.add_rock(2, 1, '1', rules)
	grid.add_rock(3, 0, '2', rules)
	line = grid.line_grid
	goal = np.array(['0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_5():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 3, '2', rules)
	grid.add_rock(0, 2, '1', rules)
	grid.add_rock(0, 1, '1', rules)
	grid.add_rock(0, 0, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_6():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(3, 0, '2', rules)
	grid.add_rock(2, 0, '1', rules)
	grid.add_rock(1, 0, '1', rules)
	grid.add_rock(0, 0, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_7():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(3, 3, '2', rules)
	grid.add_rock(2, 2, '1', rules)
	grid.add_rock(1, 1, '1', rules)
	grid.add_rock(0, 0, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2'])
	assert np.array_equal(line, goal)


def test_8():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(3, 0, '2', rules)
	grid.add_rock(2, 1, '1', rules)
	grid.add_rock(1, 2, '1', rules)
	grid.add_rock(0, 3, '2', rules)
	line = grid.line_grid
	goal = np.array(['0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_9():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(3, 3, '2', rules)
	grid.add_rock(0, 1, '1', rules)
	grid.add_rock(0, 2, '1', rules)
	grid.add_rock(1, 3, '1', rules)
	grid.add_rock(2, 3, '1', rules)
	grid.add_rock(0, 3, '2', rules)
	line = grid.line_grid
	goal = np.array(['2', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2'])
	assert np.array_equal(line, goal)


def test_r1():
	grid = gmk.Grid(4, '1', '2')
	grid.add_rock(0, 0, '2', rules)
	grid.add_rock(0, 1, '1', rules)
	grid.add_rock(0, 3, '2', rules)
	grid.add_rock(0, 2, '1', rules)
	line = grid.line_grid
	goal = np.array(['2', '1', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
	assert np.array_equal(line, goal)


def test_1_1():  # double free three in an angle as angle
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(0, 1, '2', rules)
	grid.add_rock(0, 2, '2', rules)
	grid.add_rock(1, 0, '2', rules)
	grid.add_rock(2, 0, '2', rules)

	assert grid.add_rock(0, 0, '2', rules) == gmk.RuleStatus.OK


def test_1_2():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(0, 1, '2', rules)
	grid.add_rock(0, 2, '2', rules)
	grid.add_rock(1, 0, '2', rules)
	grid.add_rock(2, 0, '2', rules)
	grid.add_rock(3, 0, '1', rules)  # same as test 1 but with a free three blocked

	assert grid.add_rock(0, 0, '2', rules) == gmk.RuleStatus.OK


def test_1_3():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(0, 1, '2', rules)
	grid.add_rock(0, 2, '2', rules)
	grid.add_rock(1, 0, '2', rules)
	grid.add_rock(2, 0, '2', rules)
	grid.add_rock(1, 1, '1', rules)  # same as test 1.1 but with a capture
	grid.add_rock(2, 2, '1', rules)
	grid.add_rock(3, 3, '2', rules)

	assert grid.add_rock(0, 0, '2', rules) == gmk.RuleStatus.OK


def test_2_1():  # double free three in the middle as angle
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 7, '2', rules)
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(6, 8, '2', rules)
	grid.add_rock(9, 8, '2', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.NO


def test_2_2():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 7, '2', rules)
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(6, 8, '2', rules)
	grid.add_rock(9, 8, '2', rules)
	grid.add_rock(8, 9, '1', rules)  # same as test 2.1 but with a free three blocked
	grid.add_rock(8, 5, '1', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_2_3():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 7, '2', rules)
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(6, 8, '2', rules)
	grid.add_rock(9, 8, '2', rules)
	grid.add_rock(9, 9, '1', rules)  # same as test 2.1 but with a capture
	grid.add_rock(10, 10, '1', rules)
	grid.add_rock(11, 11, '2', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_3_1():  # double free three in the middle as line
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 5, '2', rules)
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(8, 10, '2', rules)
	grid.add_rock(8, 11, '2', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_3_2():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 5, '2', rules)
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(8, 10, '2', rules)
	grid.add_rock(8, 11, '2', rules)
	grid.add_rock(8, 9, '1', rules)  # same as test 3.1 but with a free three blocked

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_3_3():
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 6, '2', rules)
	grid.add_rock(8, 10, '2', rules)
	grid.add_rock(8, 11, '2', rules)
	grid.add_rock(9, 9, '1', rules)  # same as test 3.1 but with a capture
	grid.add_rock(10, 10, '1', rules)
	grid.add_rock(11, 11, '2', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_4_1():  # one three
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(8, 5, '2', rules)
	grid.add_rock(8, 6, '2', rules)

	assert grid.add_rock(8, 8, '2', rules) == gmk.RuleStatus.OK


def test_game_1():  # from game bug
	grid = gmk.Grid(19, '1', '2')
	grid.add_rock(0, 0, '1', rules)
	grid.add_rock(1, 0, '1', rules)
	grid.add_rock(1, 2, '1', rules)
	grid.add_rock(3, 2, '1', rules)
	grid.add_rock(2, 4, '1', rules)
	grid.add_rock(3, 4, '1', rules)
	grid.add_rock(4, 4, '1', rules)
	grid.add_rock(6, 4, '1', rules)

	grid.add_rock(5, 4, '2', rules)
	grid.add_rock(4, 5, '2', rules)
	grid.add_rock(5, 5, '2', rules)
	grid.add_rock(6, 5, '2', rules)
	grid.add_rock(6, 6, '2', rules)
	grid.add_rock(7, 6, '2', rules)
	grid.add_rock(8, 7, '2', rules)

	assert grid.add_rock(9, 8, '2', rules) == gmk.RuleStatus.WIN