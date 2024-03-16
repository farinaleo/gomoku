#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/13/24, 3:17 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


def expend_to_victory(line, grid, x, y, player, opponent, size, line_size) -> float:
    """Evaluate the possibility to win in alignment case.
    :param line: the game as list.
    :param grid: the node.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :param line_size: the total line size.
    :return: the evaluated value.
    """
    count = __check_row(y, x, player, opponent, line, size)
    count = count + __check_column(y, x, player, opponent, line, size)
    count = count + __check_diagonal1(y, x, player, opponent, line, size)
    count = count + __check_diagonal2(y, x, player, opponent, line, size)
    return count / 4


def __check_column(row: int, col: int, player, opponent, line, size) -> float:
    """Check if the next move has the space to expend the alignment to the victory.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :return: 0 for no winning, 1 for winning, 0.5 if no friends for alignment
    """
    col_g = ''.join([str(line[col + i * size]) for i in range(size)])
    start = max(0, row - 4)
    end = min(size, row + 5)
    col_g = col_g[start:end]

    return can_win(col_g, player, opponent)


def __check_row(row: int, col: int, player, opponent, line, size) -> float:
    """Check if the next move has the space to expend the alignment to the victory.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :return: 0 for no winning, 1 for winning, 0.5 if no friends for alignment
    """
    row_g = ''.join([str(line[i + (row * size)]) for i in range(size)])
    start = max(0, col - 4)
    end = min(size, col + 5)
    row_g = row_g[start:end]

    return can_win(row_g, player, opponent)


def __check_diagonal1(row: int, col: int, player, opponent, line, size) -> float:
    """Check if the next move has the space to expend the alignment to the victory.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :return: 0 for no winning, 1 for winning, 0.5 if no friends for alignment
    """
    while 0 <= row < size and 0 <= col < size:
        row = row - 1
        col = col - 1
    row = row + 1
    col = col + 1
    diag1_g = ''.join([str(line[(row + i) * size + col + i]) for i in range(min(size - row, size - col))])
    start = max(0, min(col, row) - 4)
    end = min(len(diag1_g), min(col, row) + 5)
    diag1_g = diag1_g[start:end]

    return can_win(diag1_g, player, opponent)


def __check_diagonal2(row: int, col: int, player, opponent, line, size) -> float:
    """Check if the next move has the space to expend the alignment to the victory.
    :param row:  row to analyse
    :param col: column to analyse
    :param player: player value
    :param opponent: opponent value
    :param line: line to analyse
    :param size: size of the board
    :return: 0 for no winning, 1 for winning, 0.5 if no friends for alignment
    """
    while 0 <= row < size and 0 <= col < size:
        row = row + 1
        col = col - 1
    row = row - 1
    col = col + 1

    diag2_g = ''.join([str(line[(row - i) * size + col + i]) for i in range(min(row + 1, size - col))])
    len_diag2_g = len(diag2_g)
    start = max(0, min(col, len_diag2_g - row) - 4)
    end = min(len_diag2_g, min(len_diag2_g - col, row) + 5)
    diag2_g = diag2_g[start:end]

    return can_win(diag2_g, player, opponent)


def can_win(line, player, opponent):
    """Evaluate the possibility of winning
    :param line: the extracted line
    :param player: the player value
    :param opponent: the opponent value
    :return: 0 for no winning, 1 for winning, 0.5 if no friends for alignment
    """
    if line.count(player) < 2:
        return 0.5
    friends = 0
    for c in line:
        if c == player:
            friends = friends + 1
            if friends >= 2:
                break
        if c == opponent:
            friends = 0
    if friends < 2:
        return 0.5
    start = 0
    end = 5
    len_diag2_g = len(line)
    while 0 <= start < len_diag2_g and 0 <= end < len_diag2_g:
        if line[start:end].count(player) >= 2:
            if line[start:end].count(opponent) == 0:
                return 1
        start = start + 1
        end = end + 1
    return 0
