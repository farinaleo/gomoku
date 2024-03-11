#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/2/24, 11:15 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.
import copy
import ctypes
import math
from ft_gomoku import Grid, RuleStatus

rules_nb = 5
open_lib = False
free_deg_c = None
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


def evaluate(grid: Grid) -> float:
    """
    Evaluate the node to have its interesting value.
    :param grid: the node to evaluate.
    :return: the score of the node.
    """
    global open_lib, free_deg_c
    score = 0

    if not open_lib:
        example_lib = ctypes.CDLL('./ft_gomoku/AI/ft_gomoku.so')
        free_deg_c = example_lib.free_deg
        open_lib = True

    player, x, y = grid.get_last_move()
    opponent = grid.player1 if player != grid.player1 else grid.player2
    line = grid.line_grid
    size = grid.size

    if grid.winning:
        return 100

    score = score - grid.get_captured_stones(player)
    score = score + grid.get_captured_stones(opponent)
    score = score - free_deg(line, x, y, opponent, size)
    score = score + __align_n(line, [2, 3, 4], player, y, x, size)
    op_last_move = grid.get_last_move(opponent)
    if op_last_move is not None:
        score = score - __align_n(line, [2, 3, 4], opponent, op_last_move[2], op_last_move[1], size, True)
        score = score + free_deg(line, op_last_move[1], op_last_move[2], player, size)

    # print(f"Score: {score} for {x} {y}")
    return score


# Each rules have to return a rate between 0 and 1.
# the more the rate is near to 1 to more the rule is interesting.


# def free_deg(line, x, y, opponent, size):
#     global free_deg_c
#
#     line_c = ctypes.c_char_p(''.join(line).encode('utf-8'))
#     x_c = ctypes.c_int(x)
#     y_c = ctypes.c_int(y)
#     opponent_c = ctypes.c_int(ord(opponent))
#     size_c = ctypes.c_int(size)
#     return free_deg_c(line_c, x_c, y_c, opponent_c, size_c)


def free_deg(line, x, y, opponent, size):
    count = 0
    if x < 5:
        count = count + (5 - x)
    if y < 5:
        count = count + (5 - y)
    if x > size - 5:
        count = count + (5 - size - x)
    if y > size - 5:
        count = count + (5 - size - y)
    return count


def __far_from_opponent_last_moves(opponent, x, y, grid, n=1):
    """Calculate the rate corresponding of the distance between the
    opponent and the last move of the player.
    :param opponent: the opponent type
    :param x: the coordinates of the last move
    :param y: the coordinates of the last move
    :param grid: the game
    :param n: the number of moves to select
    :return: a rate as 1/(dist op-pl)
    """
    cnt = 0
    sum_dist = 0
    i = 0
    while i < n:
        op_move = grid.get_last_move(opponent, i + 1)
        if op_move is None:
            break
        else:
            cnt = cnt + 1
            sum_dist = sum_dist + int((math.sqrt((x - op_move[1]) * (x - op_move[1]) + (y - op_move[2]) * (y - op_move[2]))))
        i = i + 1
    if cnt == 0:
        return 1
    if sum_dist == 0:
        return 0
    return sum_dist


def __far_from_allies_last_moves(allie, x, y, grid, n=1):
    """Calculate the rate corresponding of the distance between the
    allies and the last move of the player.
    :param allie: the allie type
    :param x: the coordinates of the last move
    :param y: the coordinates of the last move
    :param grid: the game
    :param n: the number of moves to select
    :return: a rate as 1/(dist op-pl)
    """
    i = 0
    cnt = 0
    sum_dist = 0
    while i < n:
        op_move = grid.get_last_move(allie, i + 2)
        if op_move is None:
            break
        else:
            cnt = cnt + 1
            sum_dist = sum_dist + (math.sqrt((x - op_move[1]) * (x - op_move[1]) + (y - op_move[2]) * (y - op_move[2])))
        i = i + 1
    if cnt == 0:
        return 1
    if sum_dist == 0:
        return 0
    return sum_dist


def __align_n(line, lens, player, row, col, size, first_call=False):
    """Count the n alignment of the player
    :param grid: the grid game
    :param player: the player type
    :return: the number of aligned possibilities.
    """
    count = 0
    goals = []
    for n in lens:
        if n == 2:
            if player == '2':
                goals.extend(goal2_2)
                goals.extend(block1_2)
                # goals.extend(block2_2)
            else:
                goals.extend(goal1_2)
                goals.extend(block2_2)
                # goals.extend(block1_2)

        if n == 3:
            if player == '2':
                goals.extend(goal2_3)
                goals.extend(block1_3)
                # goals.extend(block2_3)

            else:
                goals.extend(goal1_3)
                goals.extend(block2_3)
                # goals.extend(block1_3)
        if n == 4:
            if player == '2':
                goals.extend(goal2_4)
                goals.extend(block1_4)
                # goals.extend(block2_4)
            else:
                goals.extend(goal1_4)
                goals.extend(block2_4)
                # goals.extend(block1_4)

        # gen_pos(n, player, ['0'] * 5, goals)

    count = count + __check_row(row, col, goals, line, size)
    count = count + __check_column(row, col, goals, line, size)
    count = count + __check_diagonal1(row, col, goals, line, size)
    count = count + __check_diagonal2(row, col, goals, line, size)

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
