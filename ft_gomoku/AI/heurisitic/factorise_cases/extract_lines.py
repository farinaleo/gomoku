#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/23/24, 12:49 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


def extract_column(row: int, col: int, grid, size) -> str:
    """Extract the column from the game bord to analyse it.
    :param row: The row to analyse.
    :param col: column to analyse
    :param grid: grid to analyse
    :param size: the game board size.
    :return: the extracted column.
    """
    col_g = ''.join([str(grid[col + i * size]) for i in range(size)])
    return col_g


def extract_row(row: int, col: int, grid, size) -> str:
    """Extract the row from the game bord to analyse it.
    :param row: The row to analyse.
    :param col: column to analyse
    :param grid: grid to analyse
    :param size: the game board size.
    :return: the extracted row.
    """
    row_g = ''.join([str(grid[i + (row * size)]) for i in range(size)])
    return row_g


def extract_diagonal1(row: int, col: int, grid, size) -> str:
    """Extract the first diagonal from the game bord to analyse it.
    :param row: The row to analyse.
    :param col: column to analyse
    :param grid: grid to analyse
    :param size: the game board size.
    :return: the extracted diagonal.
    """
    while 0 <= row < size and 0 <= col < size:
        row = row - 1
        col = col - 1
    row = row + 1
    col = col + 1
    diag1_g = ''.join([str(grid[(row + i) * size + col + i]) for i in range(min(size - row, size - col))])
    return diag1_g


def extract_diagonal2(row: int, col: int, grid, size) -> str:
    """Extract the second diagonal from the game bord to analyse it.
    :param row: The row to analyse.
    :param col: column to analyse
    :param grid: grid to analyse
    :param size: the game board size.
    :return: the extracted diagonal.
    """
    while 0 <= row < size and 0 <= col < size:
        row = row + 1
        col = col - 1
    row = row - 1
    col = col + 1

    diag2_g = ''.join([str(grid[(row - i) * size + col + i]) for i in range(min(row + 1, size - col))])
    return diag2_g
