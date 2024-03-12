#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 3:22 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.



goal2_4 = [('22220', 0.4), ('22202', 0.4), ('22022', 0.4), ('20222', 0.4), ('02222', 0.4)]
goal2_3 = [('22200', 0.3), ('22020', 0.3), ('22002', 0.3), ('20220', 0.3), ('20202', 0.3),
           ('20022', 0.3), ('02220', 0.3), ('02202', 0.3), ('02022', 0.3), ('00222', 0.3)]
goal2_2 = [('22000', 0.2), ('20200', 0.2), ('20020', 0.2), ('20002', 0.2), ('02200', 0.2),
           ('02020', 0.2), ('02002', 0.2), ('00220', 0.2), ('00202', 0.2), ('00022', 0.2)]

goal1_4 = [('11110', 0.4), ('11101', 0.4), ('11011', 0.4), ('10111', 0.4), ('01111', 0.4)]
goal1_3 = [('11100', 0.3), ('11010', 0.3), ('11001', 0.3), ('10110', 0.3), ('10101', 0.3),
           ('10011', 0.3), ('01110', 0.3), ('01101', 0.3), ('01011', 0.3), ('00111', 0.3)]
goal1_2 = [('11000', 0.2), ('10100', 0.2), ('10010', 0.2), ('10001', 0.2), ('01100', 0.2),
           ('01010', 0.2), ('01001', 0.2), ('00110', 0.2), ('00101', 0.2), ('00011', 0.2)]

block2_4 = [('22221', 0.8), ('22212', 0.8), ('22122', 0.8), ('21222', 0.8), ('12222', 0.8)]
block2_3 = [('22201', 0.6), ('22021', 0.6), ('22102', 0.6), ('20221', 0.6), ('20212', 0.6),
            ('21022', 0.6), ('12220', 0.6), ('12202', 0.6), ('12022', 0.6), ('10222', 0.6),
            ('22210', 0.6), ('22120', 0.6), ('22012', 0.6), ('21220', 0.6), ('21202', 0.6),
            ('20122', 0.6), ('02221', 0.6), ('02212', 0.6), ('02122', 0.6), ('01222', 0.6)]
block2_2 = [('22001', 0.4), ('20201', 0.4), ('20021', 0.4), ('20012', 0.4), ('02201', 0.4),
            ('02021', 0.4), ('02012', 0.4), ('00221', 0.4), ('00212', 0.4), ('00122', 0.4),
            ('22010', 0.4), ('20210', 0.4), ('20120', 0.4), ('20102', 0.4), ('02210', 0.4),
            ('02120', 0.4), ('02102', 0.4), ('01220', 0.4), ('01202', 0.4), ('01022', 0.4),
            ('22100', 0.4), ('21200', 0.4), ('21020', 0.4), ('21002', 0.4), ('12200', 0.4),
            ('12020', 0.4), ('12002', 0.4), ('10220', 0.4), ('10202', 0.4), ('10022', 0.4)]

block1_4 = [('11112', 0.8), ('11121', 0.8), ('11211', 0.8), ('12111', 0.8), ('21111', 0.8)]
block1_3 = [('11102', 0.6), ('11012', 0.6), ('11021', 0.6), ('10112', 0.6), ('10121', 0.6),
            ('10211', 0.6), ('01112', 0.6), ('01121', 0.6), ('01211', 0.6), ('02111', 0.6),
            ('11120', 0.6), ('11210', 0.6), ('11201', 0.6), ('12110', 0.6), ('12101', 0.6),
            ('12011', 0.6), ('21110', 0.6), ('21101', 0.6), ('21011', 0.6), ('20111', 0.6)]
block1_2 = [('11002', 0.4), ('10102', 0.4), ('10012', 0.4), ('10021', 0.4), ('01102', 0.4),
            ('01012', 0.4), ('01021', 0.4), ('00112', 0.4), ('00121', 0.4), ('00211', 0.4),
            ('11020', 0.4), ('10120', 0.4), ('10210', 0.4), ('10201', 0.4), ('01120', 0.4),
            ('01210', 0.4), ('01201', 0.4), ('02110', 0.4), ('02101', 0.4), ('02011', 0.4),
            ('11200', 0.4), ('12100', 0.4), ('12010', 0.4), ('12001', 0.4), ('21100', 0.4),
            ('21010', 0.4), ('21001', 0.4), ('20110', 0.4), ('20101', 0.4), ('20011', 0.4)]


def matching_cases(line, grid, x, y, player, opponent, size, line_size, lens=None, block=True) -> float:
    """find the number of matching cases can be done with the movement.
    :param line: the game as list.
    :param grid: the node.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :param line_size: the total lien size.
    :param lens: combinations to evaluate between 2, 3, and 4, by default [2, 3, 4].
    :param block: test the bocking combinations.
    :return: the evaluated rate of the move.
    """
    if lens is None:
        lens = [2, 3, 4]
    count = 0
    goals = []
    for n in lens:
        if n == 2:
            if player == '2':
                goals.extend(goal2_2)
                if block:
                    goals.extend(block1_2)
            else:
                goals.extend(goal1_2)
                goals.extend(block2_2)
        if n == 3:
            if player == '2':
                goals.extend(goal2_3)
                if block:
                    goals.extend(block1_3)
            else:
                goals.extend(goal1_3)
                if block:
                    goals.extend(block2_3)
        if n == 4:
            if player == '2':
                goals.extend(goal2_4)
                if block:
                    goals.extend(block1_4)
            else:
                goals.extend(goal1_4)
                if block:
                    goals.extend(block2_4)

    count = count + __check_row(y, x, goals, line, size)
    count = count + __check_column(y, x, goals, line, size)
    count = count + __check_diagonal1(y, x, goals, line, size)
    count = count + __check_diagonal2(y, x, goals, line, size)

    return count


def __check_column(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in column.
    :param col: column to analyse
    :param goal: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    col_g = ''.join([str(grid[col + i * size]) for i in range(size)])
    for goal in goals:
        if goal[0] in col_g:
            cnt = cnt + goal[1]
    return cnt


def __check_row(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in row.
    :param row:  row to analyse
    :param goal: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    row_g = ''.join([str(grid[i + (row * size)]) for i in range(size)])
    for goal in goals:
        if goal[0] in row_g:
            cnt = cnt + goal[1]
    return cnt


def __check_diagonal1(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in a diagonal.
    :param row:  y pos
    :param col:  x pos
    :param goal: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    while 0 <= row < size and 0 <= col < size:
        row = row - 1
        col = col - 1
    row = row + 1
    col = col + 1

    diag1_g = ''.join([str(grid[(row + i) * size + col + i]) for i in range(min(size - row, size - col))])
    for goal in goals:
        if goal[0] in diag1_g:
            cnt = cnt + goal[1]
    return cnt


def __check_diagonal2(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in a diagonal.
    :param row:  y pos
    :param col:  x pos
    :param goal: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    while 0 <= row < size and 0 <= col < size:
        row = row + 1
        col = col - 1
    row = row - 1
    col = col + 1

    diag2_g = ''.join([str(grid[(row - i) * size + col + i]) for i in range(min(row + 1, size - col))])
    for goal in goals:
        if goal[0] in diag2_g:
            cnt = cnt + goal[1]
    return cnt
