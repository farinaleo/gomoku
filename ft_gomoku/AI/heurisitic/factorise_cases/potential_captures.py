#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/26/24, 12:04 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.AI.heurisitic.factorise_cases import get_start_end


capture1 = [('0112', 1), ('2110', 1)]
capture2 = [('0221', 1), ('1220', 1)]


def potential_captures(lines: [], x, y, size, player) -> float:
    """find the number of potential captures.
    :param lines: the extracted lines.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param size: the grid size.
    :return: the evaluated rate of the move.
    """
    count = 0
    captures = []
    if player == '2':
        captures.extend(capture1)
    else:
        captures.extend(capture2)

    for line in lines:
        start, end = get_start_end(line[0], line[1], x, y, size, 4)
        _line = line[0][start:end]
        for case in captures:
            count = count + _line.count(case[0]) * case[1]
    return count
