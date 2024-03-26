#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:52 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.AI.heurisitic.factorise_cases import get_start_end

bonus_4 = 2
bonus_3 = 1.6
bonus_2 = 1.3

bonus_block = 1.5

goal2_4 = [('22220', 10 * bonus_4), ('22202', 8 * bonus_4), ('22022', 8 * bonus_4), ('20222', 8 * bonus_4),
           ('02222', 10 * bonus_4)]
goal2_3 = [('22200', 7 * bonus_3), ('22020', 7 * bonus_3), ('22002', 5 * bonus_3), ('20220', 7 * bonus_3),
           ('20202', 5 * bonus_3),
           ('20022', 5 * bonus_3), ('02220', 7 * bonus_3), ('02202', 5 * bonus_3), ('02022', 5 * bonus_3),
           ('00222', 7 * bonus_3)]
goal2_2 = [('22000', 2 * bonus_2), ('20200', 1.5 * bonus_2), ('20020', 1 * bonus_2), ('20002', 1 * bonus_2),
           ('02200', 2 * bonus_2),
           ('02020', 1.5 * bonus_2), ('02002', 1 * bonus_2), ('00220', 2 * bonus_2), ('00202', 1.5 * bonus_2),
           ('00022', 2 * bonus_2)]

goal1_4 = [('11110', 10 * bonus_4), ('11101', 8 * bonus_4), ('11011', 8 * bonus_4), ('10111', 8 * bonus_4),
           ('01111', 10 * bonus_4)]
goal1_3 = [('11100', 8 * bonus_3), ('11010', 8 * bonus_3), ('11001', 8 * bonus_3), ('10110', 8 * bonus_3),
           ('10101', 8 * bonus_3),
           ('10011', 8 * bonus_3), ('01110', 8 * bonus_3), ('01101', 8 * bonus_3), ('01011', 8 * bonus_3),
           ('00111', 8 * bonus_3)]
goal1_2 = [('11000', 2 * bonus_2), ('10100', 1.5 * bonus_2), ('10010', 1 * bonus_2), ('10001', 1 * bonus_2),
           ('01100', 2 * bonus_2),
           ('01010', 1.5 * bonus_2), ('01001', 1 * bonus_2), ('00110', 2 * bonus_2), ('00101', 1.5 * bonus_2),
           ('00011', 2 * bonus_2)]

block2_4 = [('22221', 8 * bonus_block * bonus_4), ('22212', 10 * bonus_block * bonus_4), ('22122', 10 * bonus_block * bonus_4), ('21222', 10 * bonus_block * bonus_4),
            ('12222', 8 * bonus_block * bonus_4)]
block2_3 = [('22201', 5 * bonus_block * bonus_3), ('22021', 5 * bonus_block * bonus_3), ('22102', 7 * bonus_block * bonus_3), ('20221', 5 * bonus_block * bonus_3),
            ('20212', 7 * bonus_block * bonus_3),
            ('21022', 5 * bonus_block * bonus_3), ('12220', 5 * bonus_block * bonus_3), ('12202', 5 * bonus_block * bonus_3), ('12022', 5 * bonus_block * bonus_3),
            ('10222', 5 * bonus_block * bonus_3),
            ('22210', 5 * bonus_block * bonus_3), ('22120', 7 * bonus_block * bonus_3), ('22012', 7 * bonus_block * bonus_3), ('21220', 7 * bonus_block * bonus_3),
            ('21202', 7 * bonus_block * bonus_3),
            ('20122', 7 * bonus_block * bonus_3), ('02221', 5 * bonus_block * bonus_3), ('02212', 7 * bonus_block * bonus_3), ('02122', 7 * bonus_block * bonus_3),
            ('01222', 5 * bonus_block * bonus_3)]
block2_2 = [('22001', 1 * bonus_block * bonus_2), ('20201', 1 * bonus_block * bonus_2), ('20021', 1 * bonus_block * bonus_2), ('20012', 2 * bonus_block * bonus_2),
            ('02201', 1 * bonus_block * bonus_2),
            ('02021', 1 * bonus_block * bonus_2), ('02012', 2 * bonus_block * bonus_2), ('00221', 1 * bonus_block * bonus_2), ('00212', 2 * bonus_block * bonus_2),
            ('00122', 1 * bonus_block * bonus_2),
            ('22010', 1 * bonus_block * bonus_2), ('20210', 1 * bonus_block * bonus_2), ('20120', 2 * bonus_block * bonus_2), ('20102', 2 * bonus_block * bonus_2),
            ('02210', 1 * bonus_block * bonus_2),
            ('02120', 2 * bonus_block * bonus_2), ('02102', 2 * bonus_block * bonus_2), ('01220', 1 * bonus_block * bonus_2), ('01202', 1 * bonus_block * bonus_2),
            ('01022', 1 * bonus_block * bonus_2),
            ('22100', 1 * bonus_block * bonus_2), ('21200', 2 * bonus_block * bonus_2), ('21020', 2 * bonus_block * bonus_2), ('21002', 2 * bonus_block * bonus_2),
            ('12200', 1 * bonus_block * bonus_2),
            ('12020', 1 * bonus_block * bonus_2), ('12002', 1 * bonus_block * bonus_2), ('10220', 1 * bonus_block * bonus_2), ('10202', 1 * bonus_block * bonus_2),
            ('10022', 1 * bonus_block * bonus_2)]

block1_4 = [('11112', 8 * bonus_block * bonus_4), ('11121', 10 * bonus_block * bonus_4), ('11211', 10 * bonus_block * bonus_4), ('12111', 10 * bonus_block * bonus_4),
            ('21111', 8 * bonus_block * bonus_4)]
block1_3 = [('11102', 5 * bonus_block * bonus_3), ('11012', 5 * bonus_block * bonus_3), ('11021', 7 * bonus_block * bonus_3), ('10112', 5 * bonus_block * bonus_3),
            ('10121', 7 * bonus_block * bonus_3),
            ('10211', 5 * bonus_block * bonus_3), ('01112', 5 * bonus_block * bonus_3), ('01121', 5 * bonus_block * bonus_3), ('01211', 5 * bonus_block * bonus_3),
            ('02111', 5 * bonus_block * bonus_3),
            ('11120', 5 * bonus_block * bonus_3), ('11210', 7 * bonus_block * bonus_3), ('11201', 5 * bonus_block * bonus_3), ('12110', 7 * bonus_block * bonus_3),
            ('12101', 7 * bonus_block * bonus_3),
            ('12011', 7 * bonus_block * bonus_3), ('21110', 5 * bonus_block * bonus_3), ('21101', 5 * bonus_block * bonus_3), ('21011', 7 * bonus_block * bonus_3),
            ('20111', 5 * bonus_block * bonus_3)]
block1_2 = [('11002', 1 * bonus_block * bonus_2), ('10102', 1 * bonus_block * bonus_2), ('10012', 1 * bonus_block * bonus_2), ('10021', 2 * bonus_block * bonus_2),
            ('01102', 1 * bonus_block * bonus_2),
            ('01012', 1 * bonus_block * bonus_2), ('01021', 2 * bonus_block * bonus_2), ('00112', 1 * bonus_block * bonus_2), ('00121', 2 * bonus_block * bonus_2),
            ('00211', 1 * bonus_block * bonus_2),
            ('11020', 1 * bonus_block * bonus_2), ('10120', 1 * bonus_block * bonus_2), ('10210', 2 * bonus_block * bonus_2), ('10201', 2 * bonus_block * bonus_2),
            ('01120', 1 * bonus_block * bonus_2),
            ('01210', 2 * bonus_block * bonus_2), ('01201', 2 * bonus_block * bonus_2), ('02110', 1 * bonus_block * bonus_2), ('02101', 1 * bonus_block * bonus_2),
            ('02011', 1 * bonus_block * bonus_2),
            ('11200', 1 * bonus_block * bonus_2), ('12100', 2 * bonus_block * bonus_2), ('12010', 2 * bonus_block * bonus_2), ('12001', 2 * bonus_block * bonus_2),
            ('21100', 1 * bonus_block * bonus_2),
            ('21010', 1 * bonus_block * bonus_2), ('21001', 1 * bonus_block * bonus_2), ('20110', 1 * bonus_block * bonus_2), ('20101', 1 * bonus_block * bonus_2),
            ('20011', 1 * bonus_block * bonus_2)]


def matching_cases(lines: [], x, y, size, player) -> float:
    """find the number of matching cases that can be done with the movement.
    :param lines: the extracted lines.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param size: the grid size.
    :return: the evaluated rate of the move.
    """
    cnt = 0
    cases = []
    if player == '1':
        cases.extend(goal1_2)
        cases.extend(goal1_3)
        cases.extend(goal1_4)
        cases.extend(block2_2)
        cases.extend(block2_3)
        cases.extend(block2_4)
    else:
        cases.extend(goal2_2)
        cases.extend(goal2_3)
        cases.extend(goal2_4)
        cases.extend(block1_2)
        cases.extend(block1_3)
        cases.extend(block1_4)

    for line in lines:
        start, end = get_start_end(line[0], line[1], x, y, size, 6)
        _line = line[0][start:end]
        for case in cases:
            # if case[0] in _line:
            #     cnt = cnt * case[1]
            cnt = cnt + _line.count(case[0]) * case[1]
    return cnt
