#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/16/24, 4:25 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid, log
from ft_gomoku.AI import next_generation


@log()
def pvs(grid: Grid, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> float | None:
    """
    Principal Variation Search. Uses it to find the best move to play
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
        return grid.heuristic * (depth + 1)
    next_gen = next_generation(grid, rules, ai_value if is_max else grid.player2)
    if next_gen is None or len(next_gen) == 0:
        return float('-inf') if is_max else float('inf')
    for node in next_gen:
        if node == next_gen[0]:
            _val = -pvs(node, depth - 1, - beta, - alpha, rules, ai_value, not is_max)
        else:
            _val = -pvs(node, depth - 1, (- alpha) - 1, (- alpha), rules, ai_value, not is_max)
            if alpha < _val < beta:
                _val = -pvs(node, depth - 1, - beta, (- alpha), rules, ai_value, not is_max)
        alpha = max(alpha, _val)
        if alpha >= beta:
            break
    return alpha


def launch_pvs(grid: Grid, depth: int, alpha: float, beta: float, rules, ai_value, is_max=True) -> tuple | None:
    """
    Launch the Principal Variation Search to find the best move to play.
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
    next_gen = next_generation(grid, rules, ai_value if is_max else grid.player2, first_call=True)
    if next_gen is None or len(next_gen) == 0:
        return None
    max_val = float('-inf')
    move_selected = next_gen[0].get_last_move()[-2:]
    if len(next_gen) > 1:
        for node in next_gen:
            _val = pvs(node, depth - 1, alpha, beta, rules, ai_value, is_max)
            if _val > max_val:
                max_val = _val
                move_selected = node.get_last_move()[-2:]
    return move_selected
