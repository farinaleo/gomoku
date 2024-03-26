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
    """

    :param line:
    :param line_type:
    :param x:
    :param y:
    :param size:
    :param dist:
    :return:
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
        end = min(len(line), min(size - y, x) + dist)
    return start, end
