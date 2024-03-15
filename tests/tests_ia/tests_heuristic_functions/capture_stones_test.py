#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/15/24, 10:38 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk
import ft_gomoku.AI as ai


def test_1():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [gmk.capture])
    grid.add_rock(0, 1, '1', [gmk.capture])
    grid.add_rock(0, 2, '1', [gmk.capture])
    grid.add_rock(0, 3, '1', [gmk.capture])
    grid.add_rock(0, 4, '1', [gmk.capture])
    assert ai.capture_stones(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 0


def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [gmk.capture])
    grid.add_rock(0, 1, '2', [gmk.capture])
    grid.add_rock(0, 2, '2', [gmk.capture])
    grid.add_rock(0, 3, '1', [gmk.capture])
    grid.add_rock(0, 4, '1', [gmk.capture])
    grid.add_rock(0, 5, '2', [gmk.capture])
    grid.add_rock(0, 6, '2', [gmk.capture])
    grid.add_rock(0, 7, '1', [gmk.capture])
    grid.add_rock(0, 8, '1', [gmk.capture])
    grid.add_rock(0, 9, '2', [gmk.capture])
    grid.add_rock(0, 10, '2', [gmk.capture])
    grid.add_rock(0, 11, '1', [gmk.capture])
    assert ai.capture_stones(grid.line_grid, grid, 11, 0, '1', '2', 19, 361) == 6 / 10


def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [gmk.capture])
    grid.add_rock(0, 1, '2', [gmk.capture])
    grid.add_rock(0, 2, '2', [gmk.capture])
    grid.add_rock(0, 3, '1', [gmk.capture])
    grid.add_rock(0, 4, '1', [gmk.capture])
    grid.add_rock(0, 5, '2', [gmk.capture])
    grid.add_rock(0, 6, '2', [gmk.capture])
    grid.add_rock(0, 7, '1', [gmk.capture])
    grid.add_rock(0, 8, '1', [gmk.capture])
    grid.add_rock(0, 9, '2', [gmk.capture])
    grid.add_rock(0, 10, '2', [gmk.capture])
    grid.add_rock(0, 11, '1', [gmk.capture])
    grid.add_rock(0, 12, '1', [gmk.capture])
    grid.add_rock(0, 13, '2', [gmk.capture])
    grid.add_rock(0, 14, '2', [gmk.capture])
    grid.add_rock(0, 15, '1', [gmk.capture])
    grid.add_rock(1, 0, '1', [gmk.capture])
    grid.add_rock(1, 1, '2', [gmk.capture])
    grid.add_rock(1, 2, '2', [gmk.capture])
    grid.add_rock(1, 3, '1', [gmk.capture])
    assert ai.capture_stones(grid.line_grid, grid, 3, 1, '1', '2', 19, 361) == 1


