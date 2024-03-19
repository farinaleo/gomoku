#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/19/24, 10:31 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import copy
import os
import math
from threading import Thread
from ft_gomoku.AI import next_generation, heuristic
from ft_gomoku import Grid
from ft_gomoku.AI.algorithm.alphabetaprunning import alpha_beta
from ft_gomoku.AI.algorithm.pvs import pvs


class AlphaBetaThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def get_result(self):
        return self._return


def alpha_beta_t(grid: Grid, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> float | None:
    """
    Alpha Beta pruning algorithm (fail-soft). Uses it to find the best move to play
    to win the game.
    :param grid: the game board.
    :param depth: the depth to explore.
    :param alpha: the alpha limit.
    :param beta:  the beta limit.
    :param rules: game rules
    :param ai_value: the value used to determine the AI.
    :param is_max: True if the turn is for the IA otherwise False.
    :return: The node evaluation or None in case of error.
    """
    if depth <= 0 or grid.winning:
        return heuristic(grid, ai_value if is_max else grid.player2 if ai_value != grid.player2 else grid.player1) + depth
    elif depth == 1:
        return alpha_beta_thread(grid, depth, alpha, beta, rules, ai_value, is_max)
    next_gen = next_generation(grid, rules, ai_value)
    if not next_generation:
        return None
    if is_max:
        max_val = float('-inf')
        for node in next_gen:
            _val = alpha_beta_t(node, depth - 1, alpha, beta, rules, ai_value, False)
            max_val = max(max_val, _val)
            alpha = max(alpha, max_val)
            if max_val >= beta:
                return max_val
    else:
        max_val = float('+inf')
        for node in next_gen:
            _val = alpha_beta_t(node, depth - 1, alpha, beta, rules, ai_value)
            max_val = min(max_val, _val)
            beta = min(beta, max_val)
            if max_val <= alpha:
                return max_val
    return max_val


def launch_alpha_beta_thread(grid: Grid, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> tuple | None:
    """
    Launch the alpha beta pruning (fail-soft) to find the best move to play.
    :param grid: the game board.
    :param depth: the depth to explore.
    :param alpha: the alpha limit.
    :param beta:  the beta limit.
    :param rules: game rules.
    :param ai_value: the value used to determine the AI.
    :param is_max: True if the turn is for the IA otherwise False.
    :return: the move (x, y) as tuple or None in case of error.
    """
    if depth <= 0:
        return None
    next_gen = next_generation(grid, rules, ai_value)
    max_val = float('-inf')
    move_selected = next_gen[0].get_last_move()[-2:]
    for node in next_gen:
        _val = alpha_beta_t(node, depth - 1, alpha, beta, rules, ai_value, is_max)
        if _val > max_val:
            max_val = _val
            move_selected = node.get_last_move()[-2:]
    return move_selected


def alpha_beta_thread(grid: Grid, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> tuple | None:
    """
    Launch the alpha beta pruning (fail-soft) with multi threading to find the best move to play.
    :param grid: the game board.
    :param depth: the depth to explore.
    :param alpha: the alpha limit.
    :param beta:  the beta limit.
    :param rules: game rules.
    :param ai_value: the value used to determine the AI.
    :param is_max: True if the turn is for the IA otherwise False.
    :return: the move (x, y) as tuple or None in case of error.
    """
    if depth <= 0:
        return None

    try:
        thread_nb = int(os.getenv('GOMOKU_THREAD'))
    except Exception:
        thread_nb = 1

    next_gen = next_generation(grid, rules, ai_value)
    gen_by_thread = math.ceil(len(next_gen) // thread_nb)

    tmp = []
    threads = []
    for node in next_gen:
        tmp.append(node)
        if len(tmp) >= gen_by_thread:
            _thread = AlphaBetaThread(target=launch_thread,args=(copy.deepcopy(tmp), depth, alpha, beta, rules, ai_value, is_max))
            threads.append(_thread)
            tmp.clear()
    if len(tmp) > 0:
        _thread = AlphaBetaThread(target=launch_thread, args=(tmp, depth, alpha, beta, rules, ai_value, is_max))
        threads.append(_thread)
        tmp.clear()

    for thread in threads:
        thread.start()

    max_val = float('-inf')
    move_selected = next_gen[0].get_last_move()[-2:]
    for thread in threads:
        thread.join()
        _result = thread.get_result()
        if _result[-1] > max_val:
            max_val = _result[-1]
            move_selected = _result[0]
    return max_val


def launch_thread(nodes, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> tuple | None:
    max_val = float('-inf')
    move_selected = nodes[0].get_last_move()[-2:]
    for node in nodes:
        if type(node) is Grid:
            _val = pvs(node, depth, alpha, beta, rules, ai_value, is_max)
            if _val > max_val:
                max_val = _val
                move_selected = node.get_last_move()[-2:]
    return move_selected, max_val
