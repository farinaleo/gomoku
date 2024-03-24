# from ft_gomoku import SettingsStruct
# from ft_gomoku import Engine
# from ft_gomoku import main_menu, game_screen, tutorial_screen
import random

from ft_gomoku.practice.practice_server import practice_server
from ft_gomoku.AI import matching_cases, near_to_border, capture_stones, \
    winning, potential_capture, freedom_rate, expend_to_victory, \
    freedom_alignment_rate, factorised_heuristics
from ft_gomoku.AI.heurisitic.evaluate_node import set_g_func_player, set_g_func_opponent, set_opponent_weight

global g_func_player, g_func_opponent, opponent_weight


def main():
	it = 0
	while it < 100000:
		value_weight = round(random.uniform(0, 1), 1)
		value_func_player = [round(random.uniform(0, 5), 1) for _ in range(5)]
		value_func_opponent = [round(random.uniform(0, -5), 1) for _ in range(5)]
		g_func_player = [(factorised_heuristics, value_func_player[0]),
		                 (capture_stones, value_func_player[1]),
		                 (winning, value_func_player[2]),
		                 (potential_capture, value_func_player[3]),
		                 (freedom_rate, value_func_player[4])]
		g_func_opponent = [(factorised_heuristics, value_func_opponent[0]),
		                   (capture_stones, value_func_opponent[1]),
		                   (winning, value_func_opponent[2]),
		                   (potential_capture, value_func_opponent[3]),
		                   (freedom_rate, value_func_opponent[4])]

		opponent_weight = 0.0 + (value_weight * 0.1)

		set_g_func_player(g_func_player)
		set_g_func_opponent(g_func_opponent)
		set_opponent_weight(opponent_weight)
		practice_server(value_weight, value_func_player, value_func_opponent)
		it += 1


if __name__ == '__main__':
	main()
