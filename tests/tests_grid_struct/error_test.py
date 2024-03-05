#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid, RuleStatus


def test_1():
	grid = Grid(3, 'a', 'q')
	grid.add_rock(0, 0, 'a', None)
	assert grid.add_rock(0, 0, 'a', None) is RuleStatus.NO


def test_2():
	grid = Grid(3, 'a', 'q')
	res_tab = [['a', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
	grid.add_rock(0, 0, 'a', None)
	grid.add_rock(0, 0, 'q', None)
	assert grid.get_grid() == res_tab


def test_3():
	grid = Grid(3, 'a', 'q')
	assert grid.add_rock(3, 2, 'q', None) is RuleStatus.NO


def test_4():
	grid = Grid(3, 'a', 'q')
	assert grid.add_rock(2, -1, 'q', None) is RuleStatus.NO
	