#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:51 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku.AI.heurisitic.factorise_cases import *


def factorised_heuristics(line, grid, x, y, player, opponent, size, line_size) -> float:
    """Evaluate the point rate by combining multiple heuristics functions with the same extract process.
    :param line: the game board as list.
    :param grid: the game instance.
    :param x: the x coordinate of the point.
    :param y: the y coordinate of the point.
    :param player: the player to consider.
    :param opponent: the other player.
    :param size: the grid size.
    :param line_size: the total line size (size ** 2).
    :return: the sum of the heuristics.
    """
    cnt = 0
    lines = []

    lines.append((extract_row(y, x, line, size), 'row'))
    lines.append((extract_column(y, x, line, size), 'col'))
    lines.append((extract_diagonal1(y, x, line, size), 'diag1'))
    lines.append((extract_diagonal2(y, x, line, size), 'diag2'))

    cnt = cnt + matching_cases(lines, x, y, size, player) * 4
    cnt = cnt + freedom_alignment_rate(lines, x, y, player, opponent, size) * 2
    cnt = cnt + expend_to_victory(lines, x, y, player, opponent, size) * 1.5
    cnt = cnt + potential_capture(lines, x, y, player, size)

    return cnt
