#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:54 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku.AI.heurisitic.factorise_cases import get_start_end


def expend_to_victory(lines: [], x: int, y: int, player, opponent, size: int) -> float:
    """Evaluate the possibility to win in alignment case.
    :param lines: the extracted lines.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :return: the evaluated value.
    """
    cnt = 0
    for line in lines:
        start, end = get_start_end(line[0], line[1], y, x, size, 5)
        _line = line[0][start:end]
        cnt = cnt + can_win(line, player, opponent)
    return cnt / 4


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