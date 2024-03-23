#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:52 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.AI.heurisitic.factorise_cases import get_start_end


free2_4 = [('022220', 2)]
free2_3 = [('0022200', 2), ('0202200', 2), ('0022020', 2)]
free2_2 = [('00022000', 2), ('0020200', 2), ('020020', 2)]

free1_4 = [('011110', 2)]
free1_3 = [('0011100', 2), ('0101100', 2), ('0011010', 2)]
free1_2 = [('00011000', 2), ('0010100', 2), ('010010', 2)]

half_free2_4 = [('22220', 1), ('22202', 1), ('22022', 1), ('20222', 1), ('02222', 1)]
half_free2_3 = [('22200', 1), ('22020', 1), ('22002', 1), ('20220', 1), ('20202', 1),
                ('20022', 1), ('02220', 1), ('02202', 1), ('02022', 1), ('00222', 1)]
half_free2_2 = [('22000', 1), ('20200', 1), ('20020', 1), ('20002', 1), ('02200', 1),
                ('02020', 1), ('02002', 1), ('00220', 1), ('00202', 1), ('00022', 1)]

half_free1_4 = [('11110', 1), ('11101', 1), ('11011', 1), ('10111', 1), ('01111', 1)]
half_free1_3 = [('11100', 1), ('11010', 1), ('11001', 1), ('10110', 1), ('10101', 1),
                ('10011', 1), ('01110', 1), ('01101', 1), ('01011', 1), ('00111', 1)]
half_free1_2 = [('11000', 1), ('10100', 1), ('10010', 1), ('10001', 1), ('01100', 1),
                ('01010', 1), ('01001', 1), ('00110', 1), ('00101', 1), ('00011', 1)]


def freedom_alignment_rate(lines: [], x, y, player, opponent, size) -> float:
    """Evaluate the alignment freedom rate.
    :param lines: the extracted lines.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :return: 0 for flanked  or no alignment, 2 for free, 1 for half-free.
    """
    cnt = 0
    freedom_possibilities = []
    if player == '1':
        freedom_possibilities.extend(free1_2)
        freedom_possibilities.extend(free1_3)
        freedom_possibilities.extend(free1_4)
        freedom_possibilities.extend(half_free1_4)
        freedom_possibilities.extend(half_free1_3)
        freedom_possibilities.extend(half_free1_2)
    else:
        freedom_possibilities.extend(free2_2)
        freedom_possibilities.extend(free2_3)
        freedom_possibilities.extend(free2_4)
        freedom_possibilities.extend(half_free2_4)
        freedom_possibilities.extend(half_free2_3)
        freedom_possibilities.extend(half_free2_2)

    for line in lines:
        start, end = get_start_end(line[0], line[1], x, y, size, 5)
        _line = line[0][start:end]
        cnt = cnt + freedom_rate(_line, player, opponent, freedom_possibilities)

    return cnt


def freedom_rate(line, player, opponent, cases):
    """Evaluate the alignment freedom.
    :param line: the extracted line
    :param player: the player value
    :param opponent: the opponent value
    :param cases: all possible alignments cases.
    :return: 0 for flanked, 2 for free, 1 for half-free or no alignment.
    """
    if line.count(player) < 2:
        return 0
    friends = 0
    for c in line:
        if c == player:
            friends = friends + 1
            if friends >= 2:
                break
        if c == opponent:
            friends = 0
    if friends < 2:
        return 0
    for case in cases:
        if case[0] in line:
            return case[1]
    return 0
