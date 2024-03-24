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

    grid.add_rock(1, 3, '1', [])
    grid.add_rock(2, 3, '1', [])
    grid.add_rock(3, 3, '1', [])

    grid.add_rock(1, 4, '1', [])
    grid.add_rock(2, 5, '1', [])
    grid.add_rock(3, 6, '1', [])

    grid.add_rock(0, 3, '1', [])
    assert ai.expend_to_victory(grid.line_grid, grid, 3, 0, '1', '2', 19, len(grid.line_grid)) == 0.375


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '2', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '2', [])
    assert ai.expend_to_victory(grid.line_grid, grid, 2, 0, '1', '2', 19, len(grid.line_grid)) == 1.5 / 4


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 3, '1', [])
    assert ai.expend_to_victory(grid.line_grid, grid, 3, 0, '1', '2', 19, len(grid.line_grid)) == 0.5
