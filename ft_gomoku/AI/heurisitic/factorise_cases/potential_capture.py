#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/25/24, 11:12 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku.AI.heurisitic.factorise_cases import get_start_end

capture1 = [('0112', 0.8), ('2110', 0.8)]
capture2 = [('0221', 0.8), ('1220', 0.8)]


def potential_capture(lines: [], x, y, player, size) -> float:
    """find the number of potential captures that can be done with the movement.
   :param lines: the extracted lines to analyse.
   :param x: last move played.
   :param y: last move played.
   :param player: player who played the move to evaluate.
   :param size: the grid size.
   :return: the evaluated rate of the move.
   """
    cnt = 0
    captures = []
    if player == '2':
        captures.extend(capture1)
    else:
        captures.extend(capture2)
    for line in lines:
        start, end = get_start_end(line[0], line[1], x, y, size, 4)
        _line = line[0][start:end]
        for capture in captures:
            cnt = cnt + _line.count(capture[0]) * capture[1]
    return cnt
