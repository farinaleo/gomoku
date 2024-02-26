#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 7:35 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk


def test_1():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 0, 'q', [gmk.capture])
	grid.add_rock(0, 1, 'a', [gmk.capture])
	grid.add_rock(0, 2, 'a', [gmk.capture])
	grid.add_rock(0, 3, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 'q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	assert line == goal


def test_2():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 0, 'q', [gmk.capture])
	grid.add_rock(1, 0, 'a', [gmk.capture])
	grid.add_rock(2, 0, 'a', [gmk.capture])
	grid.add_rock(3, 0, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'q', 0, 0, 0]
	assert line == goal
	
	
def test_3():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 0, 'q', [gmk.capture])
	grid.add_rock(1, 1, 'a', [gmk.capture])
	grid.add_rock(2, 2, 'a', [gmk.capture])
	grid.add_rock(3, 3, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'q']
	assert line == goal
	
	
def test_4():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 3, 'q', [gmk.capture])
	grid.add_rock(1, 2, 'a', [gmk.capture])
	grid.add_rock(2, 1, 'a', [gmk.capture])
	grid.add_rock(3, 0, 'q', [gmk.capture])
	line = grid.get_line()
	goal = [0, 0, 0, 'q', 0, 0, 0, 0, 0, 0, 0, 0, 'q', 0, 0, 0]
	assert line == goal


def test_5():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 3, 'q', [gmk.capture])
	grid.add_rock(0, 2, 'a', [gmk.capture])
	grid.add_rock(0, 1, 'a', [gmk.capture])
	grid.add_rock(0, 0, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 'q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	assert line == goal


def test_6():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(3, 0, 'q', [gmk.capture])
	grid.add_rock(2, 0, 'a', [gmk.capture])
	grid.add_rock(1, 0, 'a', [gmk.capture])
	grid.add_rock(0, 0, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'q', 0, 0, 0]
	assert line == goal


def test_7():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(3, 3, 'q', [gmk.capture])
	grid.add_rock(2, 2, 'a', [gmk.capture])
	grid.add_rock(1, 1, 'a', [gmk.capture])
	grid.add_rock(0, 0, 'q', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'q']
	assert line == goal


def test_8():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(3, 0, 'q', [gmk.capture])
	grid.add_rock(2, 1, 'a', [gmk.capture])
	grid.add_rock(1, 2, 'a', [gmk.capture])
	grid.add_rock(0, 3, 'q', [gmk.capture])
	line = grid.get_line()
	goal = [0, 0, 0, 'q', 0, 0, 0, 0, 0, 0, 0, 0, 'q', 0, 0, 0]
	assert line == goal


def test_r1():
	grid = gmk.Grid(4, 'a', 'q')
	grid.add_rock(0, 0, 'q', [gmk.capture])
	grid.add_rock(0, 1, 'a', [gmk.capture])
	grid.add_rock(0, 3, 'q', [gmk.capture])
	grid.add_rock(0, 2, 'a', [gmk.capture])
	line = grid.get_line()
	goal = ['q', 'a', 'a', 'q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	assert line == goal

