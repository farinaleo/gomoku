# from ft_gomoku import SettingsStruct
#
# settings = SettingsStruct()
# settings.load()
# settings.print()
# settings.set_fps(20)
# settings.save()
import heapq
import profile
import time
#
from colorama import Fore

import ft_gomoku as gmk

from ft_gomoku.AI import run_ia
#
pos = [(0, 0),
        (0, 1),
		(1, 0),
		(2, 0),
		(3, 0),
		(4, 0),
		(5, 0),
		(6, 0),
		(7, 0),
		(8, 0),
		(9, 0),
		(10, 0),
		(11, 0),
		(12, 0),
		(13, 0),
		(14, 0),
		(15, 0),
		(16, 0),
		(17, 0),
		(18, 0),
		(0, 1),
		(1, 1),
		(2, 1),
		(3, 1),
		(4, 1),
		(5, 1),
		(6, 1),
		(7, 1),
		(8, 1),
		(9, 1),
		(10, 1),
		(11, 1),
		(12, 1),
		(13, 1),
		(14, 1),
		(15, 1),
		(16, 1),
		(17, 1),
		(18, 1),
		(0, 2),
		(1, 2),
		(2, 2),
		(3, 2),
		(4, 2),
		(5, 2),
		(6, 2),
		(7, 2),
		(8, 2),
		(9, 2),
		(10, 2),
		(11, 2),
		(12, 2),
		(13, 2),
		(14, 2),
		(15, 2),
		(16, 2),
		(17, 2),
		(18, 2),
		(0, 3),
		(1, 3),
		(2, 3),
		(3, 3),
		(4, 3),
		(5, 3),
		(6, 3),
		(7, 3),
		(8, 3),
		(9, 3),
		(10, 3),
		(11, 3),
		(12, 3),
		(13, 3),
		(14, 3),
		(15, 3),
		(16, 3),
		(17, 3),
		(18, 3),
		(0, 4),
		(1, 4),
		(2, 4),
		(3, 4),
		(4, 4),
		(5, 4),
		(6, 4),
		(7, 4),
		(8, 4),
		(9, 4),
		(10, 4),
		(11, 4),
		(12, 4),
		(13, 4),
		(14, 4),
		(15, 4),
		(16, 4),
		(17, 4),
		(18, 4),
		(0, 5),
		(1, 5),
		(2, 5),
		(3, 5),
		(4, 5),
		(5, 5),
		(6, 5),
		(7, 5),
		(8, 5),
		(9, 5),
		(10, 5),
		(11, 5),
		(12, 5),
		(13, 5),
		(14, 5),
		(15, 5),
		(16, 5),
		(17, 5),
		(18, 5),
		(0, 6),
		(1, 6),
		(2, 6),
		(3, 6),
		(4, 6),
		(5, 6),
		(6, 6),
		(7, 6),
		(8, 6),
		(9, 6),
		(10, 6),
		(11, 6),
		(12, 6),
		(13, 6),
		(14, 6),
		(15, 6),
		(16, 6),
		(17, 6),
		(18, 6),
		(0, 7),
		(1, 7),
		(2, 7),
		(3, 7),
		(4, 7),
		(5, 7),
		(6, 7),
		(7, 7),
		(8, 7),
		(9, 7),
		(10, 7),
		(11, 7),
		(12, 7),
		(13, 7),
		(14, 7),
		(15, 7),
		(16, 7),
		(17, 7),
		(18, 7),
		(0, 8),
		(1, 8),
		(2, 8),
		(3, 8),
		(4, 8),
		(5, 8),
		(6, 8),
		(7, 8),
		(8, 8),
		(9, 8),
		(10, 8),
		(11, 8),
		(12, 8),
		(13, 8),
		(14, 8),
		(15, 8),
		(16, 8),
		(17, 8),
		(18, 8),
		(0, 9),
		(1, 9),
		(2, 9),
		(3, 9),
		(4, 9),
		(5, 9),
		(6, 9),
		(7, 9),
		(8, 9),
		(9, 9),
		(10, 9),
		(11, 9),
		(12, 9),
		(13, 9),
		(14, 9),
		(15, 9),
		(16, 9),
		(17, 9),
		(18, 9),
		(0, 10),
		(1, 10),
		(2, 10),
		(3, 10),
		(4, 10),
		(5, 10),
		(6, 10),
		(7, 10),
		(8, 10),
		(9, 10),
		(10, 10),
		(11, 10),
		(12, 10),
		(13, 10),
		(14, 10),
		(15, 10),
		(16, 10),
		(17, 10),
		(18, 10),
		(0, 11),
		(1, 11),
		(2, 11),
		(3, 11),
		(4, 11),
		(5, 11),
		(6, 11),
		(7, 11),
		(8, 11),
		(9, 11),
		(10, 11),
		(11, 11),
		(12, 11),
		(13, 11),
		(14, 11),
		(15, 11),
		(16, 11),
		(17, 11),
		(18, 11),
		(0, 12),
		(1, 12),
		(2, 12),
		(3, 12),
		(4, 12),
		(5, 12),
		(6, 12),
		(7, 12),
		(8, 12),
		(9, 12),
		(10, 12),
		(11, 12),
		(12, 12),
		(13, 12),
		(14, 12),
		(15, 12),
		(16, 12),
		(17, 12),
		(18, 12),
		(0, 13),
		(1, 13),
		(2, 13),
		(3, 13),
		(4, 13),
		(5, 13),
		(6, 13),
		(7, 13),
		(8, 13),
		(9, 13),
		(10, 13),
		(11, 13),
		(12, 13),
		(13, 13),
		(14, 13),
		(15, 13),
		(16, 13),
		(17, 13),
		(18, 13),
		(0, 14),
		(1, 14),
		(2, 14),
		(3, 14),
		(4, 14),
		(5, 14),
		(6, 14),
		(7, 14),
		(8, 14),
		(9, 14),
		(10, 14),
		(11, 14),
		(12, 14),
		(13, 14),
		(14, 14),
		(15, 14),
		(16, 14),
		(17, 14),
		(18, 14),
		(0, 15),
		(1, 15),
		(2, 15),
		(3, 15),
		(4, 15),
		(5, 15),
		(6, 15),
		(7, 15),
		(8, 15),
		(9, 15),
		(10, 15),
		(11, 15),
		(12, 15),
		(13, 15),
		(14, 15),
		(15, 15),
		(16, 15),
		(17, 15),
		(18, 15),
		(0, 16),
		(1, 16),
		(2, 16),
		(3, 16),
		(4, 16),
		(5, 16),
		(6, 16),
		(7, 16),
		(8, 16),
		(9, 16),
		(10, 16),
		(11, 16),
		(12, 16),
		(13, 16),
		(14, 16),
		(15, 16),
		(16, 16),
		(17, 16),
		(18, 16),
		(0, 17),
		(1, 17),
		(2, 17),
		(3, 17),
		(4, 17),
		(5, 17),
		(6, 17),
		(7, 17),
		(8, 17),
		(9, 17),
		(10, 17),
		(11, 17),
		(12, 17),
		(13, 17),
		(14, 17),
		(15, 17),
		(16, 17),
		(17, 17),
		(18, 17),
		(0, 18),
		(1, 18),
		(2, 18),
		(3, 18),
		(4, 18),
		(5, 18),
		(6, 18),
		(7, 18),
		(8, 18),
		(9, 18),
		(10, 18),
		(11, 18),
		(12, 18),
		(13, 18),
		(14, 18),
		(15, 18),
		(16, 18),
		(17, 18),
		(18, 18)]


def get_pos():
	global pos
	try:
		x = int(input("choose x : "))
		y = int(input("choose y : "))
		return x, y
	except Exception:
		return get_pos()
	# _p = pos.pop(0)
	# return _p[0], _p[1]


def print_grid(grid):
	print()
	i = 0
	for char in grid.line_grid:
		if char == '1':
			print(Fore.RED + str(char), end='\t')
		elif char == '2':
			print(Fore.BLUE + str(char), end='\t')
		else:
			print(Fore.WHITE + str(char), end='\t')
		i = i + 1
		if i >= grid.size:
			i = 0
			print(Fore.WHITE)  # Saut de ligne après chaque ligne de la grille


def main():
	grid = gmk.Grid(19, '1', '2')

	rules = [
		gmk.double_three_forbidden,
		gmk.capture,
		gmk.ten_capture_to_win,
		gmk.five_to_win,
	]

	AI = False
	END = False
	while not END:
		if not AI:
			x, y = get_pos()
			return_value = grid.add_rock(y, x, '2', rules)
			if return_value == gmk.RuleStatus.NO:
				print(f'position ({x}, {y}) not allowed')
				continue
			elif return_value == gmk.RuleStatus.WIN:
				print(f'You win with the stone in ({x}, {y})')
				END = True
		else:
			start = time.time()
			# x, y, val = minmax(grid, 1, rules, float('-1'), float('1'), AI)
			# x, y = launch_alpha_beta(grid, 1, float('-inf'), float('inf'), rules, AI)
			x, y = run_ia(grid, rules)
			val = 'no val'
			# x, y, val = run_minmax(grid, 1, rules, float('-inf'), float('inf'), AI)
			# val, p = pvs(grid, 4, float('-inf'), float('inf'), 1, rules)
			# x, y, val = run_pvs(grid, 1, float('-inf'), float('inf'), 1, rules)
			# x, y = p[1], p[2]
			end = time.time()
			return_value = grid.add_rock(y, x, '1', rules)
			if return_value == gmk.RuleStatus.WIN:
				print(f'You lose with the stone in ({x}, {y})')
				END = True
			print()
			print(val)
			print(grid.get_last_move())
			print()
			print(f'time: {end - start}')
		AI = False if AI else True
		print_grid(grid)


profile.run('main()', sort='ncalls')
# # main()
# # import ctypes
# #
# # import ft_gomoku as gmk
# #
# # class Point(ctypes.Structure):
# #     _fields_ = [("x", ctypes.c_int),
# #                 ("y", ctypes.c_int)]
# #
# #
# # grid = gmk.Grid(19, '1', '2')
# # grid.add_rock(2, 2, '1', [])
# # grid.add_rock(19, 19, '1', [])
# # grid.add_rock(12, 12, '1', [])
# # grid.add_rock(2, 2, '1', [])
# # grid.add_rock(2, 14, '1', [])
# # grid.add_rock(17, 2, '1', [])
# # grid.add_rock(0, 2, '1', [])
# #
# # lib = ctypes.CDLL('./ft_gomoku/AI/ft_gomoku.so')
# # lib.possible_mvt.restype = ctypes.POINTER(Point)
# #
# #
# # line_c = ctypes.c_char_p(''.join(grid.line_grid).encode('utf-8'))
# # size_c = ctypes.c_int(grid.size)
# # i_c = ctypes.c_int(0)
# # end_c = ctypes.c_int(19*19-1)
# # p = lib.possible_mvt(line_c, size_c, i_c, end_c)
# # for i in range(361):
# # 	point = p[i]
# # 	print(f'x: {point.x}, y: {point.y}')
# # 	# print(f'{p[i].x} {p[i].y}')

# import ft_gomoku as gmk
# from colorama import Fore
#
#
# def print_grid(line, cluster):
#     print()
#     x = 0
#     for char in line:
#         if (x % 19, x // 19) in cluster:
#             print("\033[33;5m", end='')
#         if char == '1':
#             print(Fore.RED + str(char), end='\t')
#         elif char == '2':
#             print(Fore.BLUE + str(char), end='\t')
#         else:
#             print(Fore.WHITE + str(char), end='\t')
#         print("\033[0m", end='')
#         x = x + 1
#         if x % 19 == 0:
# 	        print()
#     print(Fore.WHITE)  # Saut de ligne après chaque ligne de la grille
#     return 1
#
# from ft_gomoku.AI.next_generation import __cluster
#
# grid = gmk.Grid(19, '1', '2')
#
# T = False
# while 1:
#     x, y = get_pos()
#     grid.add_rock(y, x, '1' if T else '2', [])
#     T = False if T else True
#     cluster = __cluster(grid.line_grid, 19,19*19, '1', '2')
#     print_grid(grid.line_grid, cluster)