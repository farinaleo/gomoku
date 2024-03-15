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
    grid.add_rock(9, 9, '1', [])
    assert ai.near_to_border(grid.line_grid, grid, 9, 9, '1', '2', 19, 361) == 0


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(18, 18, '1', [])
    assert ai.near_to_border(grid.line_grid, grid, 18, 18, '1', '2', 19, 361) == 10


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(1, 1, '1', [])
    assert ai.near_to_border(grid.line_grid, grid, 1, 1, '1', '2', 19, 361) == 8



