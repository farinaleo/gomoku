import time

from ft_gomoku.AI.AI import run_ai
from ft_gomoku.grid.grid import Grid
from ft_gomoku import RuleStatus
from ft_gomoku import RuleStatus, five_to_win, double_three_forbidden, capture, ten_capture_to_win


def practice_server(value_weight, value_func_player, value_func_opponent):
	game_grid = Grid(19, '1', '2')
	ai_1_reflection = 0
	ai_2_reflection = 0
	ai_1_warning = 0
	ai_2_warning = 0
	start_time = time.time()
	running = True
	while running:
		ai_1_start_time = time.time()
		if not ai_1_turn(game_grid, start_time):
			result_time = (time.time() - ai_1_start_time) * 1000
			if result_time > 500:
				ai_1_warning += 1
			ai_1_reflection += result_time
		else:
			running = False
			continue
		ai_2_start_time = time.time()
		if not ai_2_turn(game_grid, start_time):
			result_time = (time.time() - ai_2_start_time) * 1000
			if result_time > 500:
				ai_2_warning += 1
			ai_2_reflection += result_time
		else:
			running = False
			continue
	print_informations(game_grid, ai_1_reflection, ai_2_reflection, ai_1_warning, ai_2_warning, value_weight, value_func_player, value_func_opponent)
	exit(0)


def ai_1_turn(game_grid: Grid, start_time: float):
	ai_return_1 = run_ai(game_grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win], '1', '2', depth=11)
	if ai_return_1 is None:
		print('ERROR: AI 1 RETURN NONE')
		print('Actual grid :', game_grid.line_grid)
		exit(0)
	coord_ai_1 = game_grid.add_rock(ai_return_1[1], ai_return_1[0], '1', [double_three_forbidden, capture, ten_capture_to_win, five_to_win])
	if coord_ai_1 == RuleStatus.NO:
		print('ERROR: AI 1 CANNOT PLACE A ROCK HERE')
		print('Rock try to place :', ai_return_1)
		print('Actual grid :', game_grid.line_grid)
		exit(0)
	if coord_ai_1 == RuleStatus.WIN:
		print('AI 1 WIN')
		return True
	return False


def ai_2_turn(game_grid: Grid, start_time: float):
	ai_return_2 = run_ai(game_grid, [double_three_forbidden, capture, ten_capture_to_win, five_to_win], '2', '1', 10)
	if ai_return_2 is None:
		print('ERROR: AI 2 RETURN NONE')
		print('Actual grid :', game_grid.line_grid)
		exit(0)
	coord_ai_1 = game_grid.add_rock(ai_return_2[1], ai_return_2[0], '2', [double_three_forbidden, capture, ten_capture_to_win, five_to_win])
	if coord_ai_1 == RuleStatus.NO:
		print('ERROR: AI 1 CANNOT PLACE A ROCK HERE')
		print('Rock try to place :', ai_return_2)
		print('Actual grid :', game_grid.line_grid)
		exit(0)
	if coord_ai_1 == RuleStatus.WIN:
		print('AI 2 WIN')
		return True
	return False


from datetime import datetime
# f.write('total_rocks,total_turn,ai_1_reflection,ai_2_reflection,ai_1_warning,ai_2_warning,player_1_capture,player_2_capture\n')
def print_informations(game_grid: Grid, ai_1_reflection: int, ai_2_reflection: int, ai_1_warning: int, ai_2_warning: int, value_weight, value_func_player, value_func_opponent):
	total_rocks = 0
	for i in range(19 * 19):
		if game_grid.line_grid[i] != '0':
			total_rocks += 1
	player_1_capture = game_grid.get_captured_stones('1')
	player_2_capture = game_grid.get_captured_stones('2')
	total_rocks += player_1_capture
	total_rocks += player_2_capture
	total_turn = total_rocks // 2

	filename = "evaluate_node" + '.csv'

	with open(filename, 'a') as f:
		f.write(f'{total_rocks},{total_turn},{ai_1_reflection},{ai_2_reflection},{ai_1_warning},{ai_2_warning},{player_1_capture},{player_2_capture},{value_weight},{value_func_player},{value_func_opponent}\n')