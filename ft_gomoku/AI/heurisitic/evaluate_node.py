#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:20 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid
from ft_gomoku.AI import matching_cases, near_to_border, capture_stones, \
    winning, potential_capture, freedom_rate, expend_to_victory, \
    freedom_alignment_rate

# these global must be built as [(func, rate), ...] to be called correctly.
# each function must be built as func(line, grid, x, y, player, opponent, size, line_size) -> float.
g_func_player = [(matching_cases, 1),
                 (near_to_border, 1),
                 (capture_stones, 1),
                 (winning, 3),
                 (potential_capture, 0.8),
                 (freedom_rate, 1),
                 (expend_to_victory, 1),
                 (freedom_alignment_rate, 1)]
g_func_opponent = [(matching_cases, -10),
                   (near_to_border, -10),
                   (capture_stones, -10),
                   (winning, -10000),
                   (potential_capture, -20.8),
                   (freedom_rate, -10),
                   (expend_to_victory, -10),
                   (freedom_alignment_rate, -10)]

opponent_weight = 2.03


def heuristic(node: Grid, player) -> float:
    """Compute the heuristic value of the node according to the last move.
    :param node: the node to evaluate.
    :param player: the player who placed the last stone.
    :return: the heuristic value (h(node)).
    """
    h_total = 0
    node_line = node.line_grid
    node_size = node.size
    opponent = node.player1 if player == node.player2 else node.player2
    node_line_size = node_size * node_size  # the grid is a square
    func_player = g_func_player
    func_opponent = g_func_opponent

    history = node.history
    for move in history:
        if node.line_grid[move[1] + move[2] * node_size] != '0':
            if move[0] == player:
                for func in func_player:
                    h_total = h_total + func[0](node_line, node, move[1], move[2], player, opponent, node_size,
                                                node_line_size) * func[1]
            elif move[0] == opponent:
                for func in func_opponent:
                    h_total = h_total + func[0](node_line, node, move[1], move[2], opponent, player, node_size,
                                                node_line_size) * func[1]

    return h_total
