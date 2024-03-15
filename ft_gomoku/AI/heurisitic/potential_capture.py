#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/13/24, 9:51 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.grid.grid import Grid
capture1 = [('0112', 1), ('2110', 1)]
capture2 = [('0221', 1), ('1220', 1)]


def potential_capture(line, grid, x, y, player, opponent, size, line_size) -> float:
    """find the number of potential captures that can be done with the movement.
    :param line: the game as list.
    :param grid: the node.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :param line_size: the total lien size.
    :return: the evaluated rate of the move.
    """
    count = 0
    captures = []
    if player == '2':
        captures.extend(capture1)
    else:
        captures.extend(capture2)

    count = count + __check_row(y, x, captures, line, size)
    count = count + __check_column(y, x, captures, line, size)
    count = count + __check_diagonal1(y, x, captures, line, size)
    count = count + __check_diagonal2(y, x, captures, line, size)

    return count / 8


def __check_column(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in column.
    :param col: column to analyse
    :param goals: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    col_g = ''.join([str(grid[col + i * size]) for i in range(size)])
    start = max(0, row - 3)
    end = min(size, row + 4)
    col_g = col_g[start:end]
    for goal in goals:
        cnt = cnt + col_g.count(goal[0]) * goal[1]
    return cnt


def __check_row(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in row.
    :param row:  row to analyse
    :param goals: goal line
    :param grid: grid to analyse
    :return: Rule status (WIN | NO)
    """
    cnt = 0
    row_g = ''.join([str(grid[i + (row * size)]) for i in range(size)])
    start = max(0, col - 3)
    end = min(size, col + 4)
    row_g = row_g[start:end]
    for goal in goals:
        cnt = cnt + row_g.count(goal[0]) * goal[1]
    return cnt


def __check_diagonal1(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in a diagonal.
    :param row:  y pos
    :param col:  x pos
    :param goals: goal line
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
    start = max(0, min(col, row) - 3)
    end = min(len(diag1_g), min(col, row) + 4)
    diag1_g = diag1_g[start:end]
    for goal in goals:
        cnt = cnt + diag1_g.count(goal[0]) * goal[1]
    return cnt


def __check_diagonal2(row: int, col: int, goals, grid, size) -> int:
    """Check if the next move is winning by aligning five stones or more in a diagonal.
    :param row:  y pos
    :param col:  x pos
    :param goals: goal line
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
    len_diag2_g = len(diag2_g)
    start = max(0, min(col, len_diag2_g - row) - 3)
    end = min(len_diag2_g, min(len_diag2_g - col, row) + 4)
    diag2_g = diag2_g[start:end]
    for goal in goals:
        cnt = cnt + diag2_g.count(goal[0]) * goal[1]
    return cnt
