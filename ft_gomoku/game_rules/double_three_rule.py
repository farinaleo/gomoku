#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku import RuleStatus, rule, capture

free2_3 = [('0022200', 1), ('0202200', 1), ('0022020', 1), ('002220', 1), ('022200', 1), ('020220', 1), ('022020', 1)]
free1_3 = [('0011100', 1), ('0101100', 1), ('0011010', 1), ('001110', 1), ('011100', 1), ('010110', 1), ('011010', 1)]


@rule()
def double_three_forbidden(row: int, col: int, player, grid) -> RuleStatus:
    """Check if the next move is making a double three or more
    :param row: y pos
    :param col: x pos
    :param player: who played the move
    :param grid: the grid
    :return: Rule status (WIN | OK | NO)
    """
    line = grid.line_grid
    size = grid.size
    opponent = grid.player2 if player == grid.player1 else grid.player1
    free_three = []
    free_three.extend(free1_3)
    free_three.extend(free2_3)

    cnt = __check_column(row, col, player, opponent, line, size, free_three)
    cnt = cnt + __check_row(row, col, player, opponent, line, size, free_three)
    cnt = cnt + __check_diagonal1(row, col, player, opponent, line, size, free_three)
    cnt = cnt + __check_diagonal2(row, col, player, opponent, line, size, free_three)

    if capture(row, col, player, grid) == RuleStatus.CAPTURE:
        return RuleStatus.OK
    if cnt >= 2:
        return RuleStatus.NO
    else:
        return RuleStatus.OK


def __check_column(y: int, x: int, player, opponent, line, size, cases) -> float:
    """Extract the column from the game board to analyse it.
    :param y:  row to analyse
    :param x: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    col_g = ''.join([str(line[x + i * size]) for i in range(size)])
    start = max(0, y - 5)
    end = min(size, y + 6)
    col_g = col_g[start:end]
    return freedom_rate(col_g, player, opponent, cases)


def __check_row(y: int, x: int, player, opponent, line, size, cases) -> float:
    """Extract the row from the game board to analyse it.
    :param y:  row to analyse
    :param x: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    row_g = ''.join([str(line[i + (y * size)]) for i in range(size)])
    start = max(0, x - 5)
    end = min(size, x + 6)
    row_g = row_g[start:end]
    return freedom_rate(row_g, player, opponent, cases)


def __check_diagonal1(y: int, x: int, player, opponent, line, size, cases) -> float:
    """Extract the first diagonal from the game board to analyse it.
    :param y:  row to analyse
    :param x: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    _x = x
    _y = y
    while 0 <= y < size and 0 <= x < size:
        y = y - 1
        x = x - 1
    y = y + 1
    x = x + 1
    diag1_g = ''.join([str(line[(x + i) + (y + i) * size]) for i in range(min(size - y, size - x))])
    start = max(0, min(_x, _y) - 5)
    end = min(len(diag1_g), min(_x, _y) + 6)
    diag1_g = diag1_g[start:end]
    return freedom_rate(diag1_g, player, opponent, cases)


def __check_diagonal2(y: int, x: int, player, opponent, line, size, cases) -> float:
    """Extract the second diagonal from the game board to analyse it.
    :param y:  row to analyse
    :param x: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    _x = x
    _y = y
    while 0 <= y < size and 0 <= x < size:
        y = y + 1
        x = x - 1
    y = y - 1
    x = x + 1

    diag2_g = ''.join([str(line[(x + i) + (y - i) * size]) for i in range(min(y + 1, size - x))])
    len_diag2_g = len(diag2_g)
    start = max(0, min(_x, size - _y) - 5)
    end = min(len_diag2_g, min(_x, size - _y) + 6)
    diag2_g = diag2_g[start:end]
    return freedom_rate(diag2_g, player, opponent, cases)


def freedom_rate(line, player, opponent, cases):
    """Evaluate the alignment freedom (for three alignment).
    :param line: the extracted line
    :param player: the player value
    :param opponent: the opponent value
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    cnt = 0
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
            cnt = cnt + case[1]
            break
    return cnt
