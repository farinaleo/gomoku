#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/15/24, 10:30 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk
import ft_gomoku.AI as ai


def test_1():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.matching_cases(grid.line_grid, grid, 4, 0, '1', '2', 19, 361, [2, 3, 4]) == 0.9


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.matching_cases(grid.line_grid, grid, 4, 0, '1', '2', 19, 361, [3, 4]) == 0.7


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.matching_cases(grid.line_grid, grid, 4, 0, '1', '2', 19, 361, [4]) == 0.4


def test_4():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])

    grid.add_rock(1, 4, '2', [])
    grid.add_rock(2, 4, '2', [])
    grid.add_rock(3, 4, '2', [])

    grid.add_rock(0, 4, '1', [])

    assert ai.matching_cases(grid.line_grid, grid, 4, 0, '1', '2', 19, 361, [2, 3, 4]) == 0.9 + 2.6


def test_5():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])

    grid.add_rock(1, 4, '2', [])
    grid.add_rock(2, 4, '2', [])
    grid.add_rock(3, 4, '2', [])

    grid.add_rock(0, 4, '1', [])
    assert ai.matching_cases(grid.line_grid, grid, 4, 0, '1', '2', 19, 361, [3, 4], False) == 0.7

