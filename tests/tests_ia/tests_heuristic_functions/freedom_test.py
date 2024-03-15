#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/15/24, 10:31 AM                                                                           ▀▀███►           |
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
    assert ai.freedom_rate(grid.line_grid, grid, 0, 0, '1', '2', 19, 361) == 12 / 8


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(1, 1, '1', [])
    grid.add_rock(2, 2, '1', [])
    grid.add_rock(3, 3, '1', [])
    grid.add_rock(4, 4, '1', [])
    assert ai.freedom_rate(grid.line_grid, grid, 4, 4, '1', '2', 19, 361) == (4 * 8) / 8


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '2', [])
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '2', [])
    grid.add_rock(1, 0, '2', [])
    grid.add_rock(1, 2, '2', [])
    grid.add_rock(2, 0, '2', [])
    grid.add_rock(2, 1, '2', [])
    grid.add_rock(2, 2, '2', [])
    grid.add_rock(1, 1, '2', [])
    assert ai.freedom_rate(grid.line_grid, grid, 1, 1, '1', '2', 19, 361) == 0 / 8
