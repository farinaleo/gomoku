#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/26/24, 12:34 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import ft_gomoku as gmk

def test_1():
	grid = gmk.Grid(5, 'a', 'q')
	grid.add_rock(0, 0, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(0, 1, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(0, 2, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(0, 3, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(1, 0, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(1, 1, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(1, 2, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(1, 3, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(2, 0, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(2, 1, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(2, 2, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(2, 3, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(3, 0, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(3, 1, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(3, 2, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(3, 3, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(4, 0, 'q', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(4, 1, 'a', [gmk.capture, gmk.ten_capture_to_win])
	grid.add_rock(4, 2, 'a', [gmk.capture, gmk.ten_capture_to_win])
	assert grid.add_rock(4, 3, 'q', [gmk.capture, gmk.ten_capture_to_win]) == gmk.RuleStatus.WIN
