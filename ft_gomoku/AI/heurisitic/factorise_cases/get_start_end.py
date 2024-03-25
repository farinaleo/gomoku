#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 1:54 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from typing import Tuple


def get_start_end(line: str, line_type: str, x, y, size: int, dist: int = 0) -> Tuple[int, int]:
    """ Compute the start and end of the given line according to the given distance.
    :param line: the line to analyse.
    :param line_type: type of line to analyse, used to aplay the correct calculus.
    :param x: x coordinate.
    :param y: y coordinate.
    :param size: the game board size.
    :param dist: the distance for the point (x, y) to consider.
    :return: a tuple (start, end)
    """
    start = 0
    end = 0

    if line_type == 'row':
        start = max(0, y - dist - 1 if dist != 0 else 0)
        end = min(size, y + dist)
    elif line_type == 'col':
        start = max(0, x - dist - 1 if dist != 0 else 0)
        end = min(size, x + dist)
    elif line_type == 'diag1':
        start = max(0, min(x, y) - dist - 1 if dist != 0 else 0)
        end = min(len(line), min(x, y) - dist)
    elif line_type == 'diag2':
        start = max(0, min(x, size - y) - dist - 1 if dist != 0 else 0)
        end = min(len(line), min(x, size - y) + dist)
    return start, end
