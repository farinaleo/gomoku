#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/15/24, 10:29 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk
import ft_gomoku.AI as ai


def test_1():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(0, 0, '1', [])
    assert ai.potential_capture(grid.line_grid, grid, 0, 0, '1', '2', 19, 361) == 1 / 8


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 1, '1', [])
    assert ai.potential_capture(grid.line_grid, grid, 1, 1, '1', '2', 19, 361) == 0 / 8


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 0, '2', [])
    grid.add_rock(2, 0, '2', [])
    grid.add_rock(0, 0, '1', [])
    assert ai.potential_capture(grid.line_grid, grid, 0, 0, '1', '2', 19, 361) == 2 / 8
