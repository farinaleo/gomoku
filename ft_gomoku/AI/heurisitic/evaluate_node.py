#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:20 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid
from ft_gomoku.AI import capture_stones, winning, freedom_rate, factorised_heuristics

# these global must be built as [(func, rate), ...] to be called correctly.
# each function must be built as func(line, grid, x, y, player, opponent, size, line_size) -> float.
g_func_player = [(factorised_heuristics, 2),
                 (capture_stones, 100),
                 (winning, 1000000000000000),
                 (freedom_rate, 1)]
g_func_opponent = [(factorised_heuristics, -1),
                   (capture_stones, -100),
                   (winning, -1),
                   (freedom_rate, -1)]

opponent_weight = 0.5


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
    node_line_size = node_size * node_size
    func_player = g_func_player
    func_opponent = g_func_opponent

    history = node.history[min(0, len(node.history) // 2):]
    for move in history:
        if node.line_grid[move[1] + move[2] * node_size] != '0':
            if move[0] == player:
                for func in func_player:
                    h_total = h_total + func[0](node_line, node, move[1], move[2], player, opponent, node_size,
                                                node_line_size) * func[1]
            elif move[0] == opponent:
                for func in func_opponent:
                    h_total = h_total + func[0](node_line, node, move[1], move[2], opponent, player, node_size,
                                                node_line_size) * func[1] + opponent_weight

    return h_total
