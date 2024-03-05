# # from ft_gomoku import SettingsStruct
# #
# # settings = SettingsStruct()
# # settings.load()
# # settings.print()
# # settings.set_fps(20)
# # settings.save()
import heapq
import profile
import time
#
from colorama import Fore

import ft_gomoku as gmk


def get_pos():
	try:
		x = int(input("choose x : "))
		y = int(input("choose y : "))
		return x, y
	except Exception:
		return get_pos()


def print_grid(grid):
	print()
	for line in grid.get_grid():
		for char in line:
			if char == '1':
				print(Fore.RED + str(char), end='\t')
			elif char == '2':
				print(Fore.BLUE + str(char), end='\t')
			else:
				print(Fore.WHITE + str(char), end='\t')
		print(Fore.WHITE)  # Saut de ligne après chaque ligne de la grille


def is_win(grid, rules):
	last_play = grid.get_last_move()
	for rule in rules:
		if rule == gmk.five_to_win or rule == gmk.ten_capture_to_win:
			if rule(last_play[2], last_play[1], last_play[0], grid) == gmk.RuleStatus.WIN:
				return True
	return False


def minmax(grid, depth, rules, alpha, beta, player1=True):
	saved_pos = grid.get_last_move()[-2:]  # pas sur du tout
	max_v = 0
	if depth == 0 or is_win(grid, rules):
		return grid, gmk.evaluate(grid)
	_sol = gmk.next_generation(grid, rules, player1)
	if not player1:
		max_v = float('-inf')
		for elem in _sol:
			_val = minmax(elem[0], depth - 1, rules, alpha, beta, True)[-1]
			if _val > max_v:
				max_v = _val
				saved_pos = elem[0].get_last_move()[-2:]
			if max_v > beta:
				break
			alpha = max(alpha, max_v)
	else:
		max_v = float('+inf')
		for elem in _sol:
			_val = minmax(elem[0], depth - 1, rules, alpha, beta, False)[-1]
			if _val < max_v:
				max_v = _val
				saved_pos = elem[0].get_last_move()[-2:]
			if max_v < alpha:
				break
			beta = min(beta, max_v)

	return saved_pos[0], saved_pos[1], max_v


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
			x, y, val = minmax(grid, 3, rules, float('-inf'), float('+inf'), AI)
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


profile.run('main()')
