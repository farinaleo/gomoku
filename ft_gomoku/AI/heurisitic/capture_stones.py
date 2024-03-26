#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/11/24, 2:08 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid


def capture_stones(line, grid, x, y, player, opponent, size, line_size) -> float:
    """ Find the rate of captured stones. 1 is equal to 10 stones captured.
    :param line: the game as list.
    :param grid: the node.
    :param x: last move played.
    :param y: last move played.
    :param player: player who played the move to evaluate.
    :param opponent: the opponent.
    :param size: the grid size.
    :param line_size: the total lien size.
    :return: the rate of captured.
    """
    captured_stones = grid.get_captured_stones(player)
    return captured_stones
