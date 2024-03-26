#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:51 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku.AI.heurisitic.factorise_cases import *


def factorised_heuristics(line, grid, x, y, player, opponent, size, line_size, lens=None, block=True) -> float:
    """

    :param line:
    :param grid:
    :param x:
    :param y:
    :param player:
    :param opponent:
    :param size:
    :param line_size:
    :param lens:
    :param block:
    :return:
    """
    cnt = 0
    lines = []

    lines.append((extract_row(y, x, line, size), 'row'))
    lines.append((extract_column(y, x, line, size), 'col'))
    lines.append((extract_diagonal1(y, x, line, size), 'diag1'))
    lines.append((extract_diagonal2(y, x, line, size), 'diag2'))

    cnt = cnt + matching_cases(lines, x, y, size, player) * 4
    if player == '2':
        cnt = cnt + freedom_alignment_rate(lines, x, y, player, opponent, size) * 2
        cnt = cnt + expend_to_victory(lines, x, y, player, opponent, size) * 1

    return cnt
