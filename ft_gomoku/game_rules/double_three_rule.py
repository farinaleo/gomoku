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
    # if player == '1':
    free_three.extend(free1_3)
    # else:
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


def __check_column(row: int, col: int, player, opponent, line, size, cases) -> float:
    """Extract the column from the game board to analyse it.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    col_g = ''.join([str(line[col + i * size]) for i in range(size)])
    start = max(0, col - 5)
    end = min(size, col + 6)
    col_g = col_g[start:end]

    return freedom_rate(col_g, player, opponent, cases)


def __check_row(row: int, col: int, player, opponent, line, size, cases) -> float:
    """Extract the row from the game board to analyse it.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    row_g = ''.join([str(line[i + (row * size)]) for i in range(size)])
    start = max(0, row - 5)
    end = min(size, row + 6)
    row_g = row_g[start:end]

    return freedom_rate(row_g, player, opponent, cases)


def __check_diagonal1(row: int, col: int, player, opponent, line, size, cases) -> float:
    """Extract the first diagonal from the game board to analyse it.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    while 0 <= row < size and 0 <= col < size:
        row = row - 1
        col = col - 1
    row = row + 1
    col = col + 1
    diag1_g = ''.join([str(line[(col + i) + (row + i) * size]) for i in range(min(size - row, size - col))])
    start = max(0, min(col, row) - 5)
    end = min(len(diag1_g), min(col, row) - 6)
    diag1_g = diag1_g[start:end]
    return freedom_rate(diag1_g, player, opponent, cases)


def __check_diagonal2(row: int, col: int, player, opponent, line, size, cases) -> float:
    """Extract the second diagonal from the game board to analyse it.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :param cases: all possible alignments cases.
    :return: possibilities sum.
    """
    while 0 <= row < size and 0 <= col < size:
        row = row + 1
        col = col - 1
    row = row - 1
    col = col + 1

    diag2_g = ''.join([str(line[(col + i) + (row - i) * size]) for i in range(min(row + 1, size - col))])
    len_diag2_g = len(diag2_g)
    start = max(0, min(col, len_diag2_g - row) - 5)
    end = min(len_diag2_g, min(len_diag2_g - col, row) + 6)
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
