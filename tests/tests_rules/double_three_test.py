#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 9:03 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk


def test_1_1():  # double free three in an angle as angle
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 0, '2', [])
    grid.add_rock(2, 0, '2', [])

    assert grid.add_rock(0, 0, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_1_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 0, '2', [])
    grid.add_rock(2, 0, '2', [])
    grid.add_rock(3, 0, '1', [])  # same as test 1 but with a free three blocked

    assert grid.add_rock(0, 0, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_1_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 0, '2', [])
    grid.add_rock(2, 0, '2', [])
    grid.add_rock(1, 1, '1', [])  # same as test 1.1 but with a capture
    grid.add_rock(2, 2, '1', [])
    grid.add_rock(3, 3, '2', [])

    assert grid.add_rock(0, 0, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_2_1():  # double free three in the middle as angle
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 7, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(6, 8, '2', [])
    grid.add_rock(9, 8, '2', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.NO


def test_2_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 7, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(6, 8, '2', [])
    grid.add_rock(9, 8, '2', [])
    grid.add_rock(8, 9, '1', [])  # same as test 2.1 but with a free three blocked
    grid.add_rock(8, 5, '1', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_2_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 7, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(6, 8, '2', [])
    grid.add_rock(9, 8, '2', [])
    grid.add_rock(9, 9, '1', [])  # same as test 2.1 but with a capture
    grid.add_rock(10, 10, '1', [])
    grid.add_rock(11, 11, '2', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_3_1():  # double free three in the middle as line
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 5, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(8, 10, '2', [])
    grid.add_rock(8, 11, '2', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.NO


def test_3_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 5, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(8, 10, '2', [])
    grid.add_rock(8, 11, '2', [])
    grid.add_rock(8, 9, '1', [])  # same as test 3.1 but with a free three blocked

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_3_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 5, '2', [])
    grid.add_rock(8, 6, '2', [])
    grid.add_rock(8, 10, '2', [])
    grid.add_rock(8, 11, '2', [])
    grid.add_rock(9, 9, '1', [])  # same as test 3.1 but with a capture
    grid.add_rock(10, 10, '1', [])
    grid.add_rock(11, 11, '2', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_3_4():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '1', [])  # same as test 3.1 but with a capture
    grid.add_rock(1, 0, '1', [])
    grid.add_rock(1, 2, '2', [])
    grid.add_rock(1, 3, '2', [])
    grid.add_rock(2, 1, '2', [])
    grid.add_rock(3, 1, '2', [])

    assert grid.add_rock(1, 1, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK


def test_4_1():  # one three
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(8, 5, '2', [])
    grid.add_rock(8, 6, '2', [])

    assert grid.add_rock(8, 8, '2', [gmk.double_three_forbidden]) == gmk.RuleStatus.OK
