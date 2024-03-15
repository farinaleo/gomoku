#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/15/24, 10:32 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk
import ft_gomoku.AI as ai


def test_1():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.freedom_alignment_rate(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 2


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])

    grid.add_rock(1, 3, '1', [])
    grid.add_rock(2, 3, '1', [])
    grid.add_rock(3, 3, '1', [])

    grid.add_rock(0, 3, '1', [])
    assert ai.freedom_alignment_rate(grid.line_grid, grid, 3, 0, '1', '2', 19, 361) == 2


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 4, '1', [])
    assert ai.freedom_alignment_rate(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 0


def test_4():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.freedom_alignment_rate(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 1


def test_5():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 1, '2', [])
    grid.add_rock(0, 5, '2', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.freedom_alignment_rate(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 0
