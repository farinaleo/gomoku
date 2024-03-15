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
    grid.add_rock(0, 0, '1', [])
    grid.add_rock(0, 1, '1', [])
    grid.add_rock(0, 2, '1', [])
    grid.add_rock(0, 3, '1', [])
    grid.add_rock(0, 4, '1', [])
    assert ai.winning(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 0

def test_2():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(0, 1, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(0, 2, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(0, 3, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(1, 0, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(1, 1, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(1, 2, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(1, 3, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(2, 0, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(2, 1, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(2, 2, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(2, 3, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(3, 0, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(3, 1, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(3, 2, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(3, 3, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(4, 0, '1', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(4, 1, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(4, 2, '2', [gmk.capture, gmk.ten_capture_to_win])
    grid.add_rock(4, 3, '1', [gmk.capture, gmk.ten_capture_to_win])

    assert ai.winning(grid.line_grid, grid, 3, 4, '1', '2', 19, 361) == 100

def test_3():
    grid = gmk.Grid(19, '1', '2')
    grid.add_rock(0, 0, '1', [gmk.five_to_win])
    grid.add_rock(0, 1, '1', [gmk.five_to_win])
    grid.add_rock(0, 2, '1', [gmk.five_to_win])
    grid.add_rock(0, 3, '1', [gmk.five_to_win])
    grid.add_rock(0, 4, '1', [gmk.five_to_win])
    assert ai.winning(grid.line_grid, grid, 4, 0, '1', '2', 19, 361) == 100

