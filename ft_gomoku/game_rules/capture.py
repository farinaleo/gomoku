#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import RuleStatus, CAPTURE, rule

point = []


@rule()
def capture(row: int, col: int, player, grid):
    """Check if the move can capture two enemy stones
    :param row: y pos
    :param col: x pos
    :param player: who played the move
    :param grid: the grid
    :return: Rule status (CAPTURE | NO)
    """
    status = RuleStatus.OK
    size = grid.get_size()
    grid_tab = grid.get_grid()
    p1, p2 = grid.get_player1(), grid.get_player2()
    goal = str(p1+p2+p2+p1) if player == p1 else str(p2+p1+p1+p2)

    up = __check_up(row, col, goal, grid_tab, size)
    down = __check_down(row, col, goal, grid_tab, size)
    left = __check_left(row, col, goal, grid_tab, size)
    right = __check_right(row, col, goal, grid_tab, size)

    if up == CAPTURE.CAPTURE or down == CAPTURE.CAPTURE or left == CAPTURE.CAPTURE or right == CAPTURE.CAPTURE:
        status = RuleStatus.CAPTURE
    elif up != CAPTURE.NO_UP:
        if left != CAPTURE.NO_LEFT:
            if __check_up_left(row, col, goal, grid_tab, size) == CAPTURE.CAPTURE:
                status = RuleStatus.CAPTURE
        if right != CAPTURE.NO_RIGHT:
            if __check_up_right(row, col, goal, grid_tab, size) == CAPTURE.CAPTURE:
                status = RuleStatus.CAPTURE
    if down != CAPTURE.NO_DOWN:
        if left != CAPTURE.NO_LEFT:
            if __check_down_left(row, col, goal, grid_tab, size) == CAPTURE.CAPTURE:
                status = RuleStatus.CAPTURE
        if right != CAPTURE.NO_RIGHT:
            if __check_down_right(row, col, goal, grid_tab, size) == CAPTURE.CAPTURE:
                status = RuleStatus.CAPTURE

    if status == RuleStatus.OK:
        return status
    return status, point


def __check_up(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture upwards
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y -= 1
        inc += 1

    if line == goal:
        point.append((col, row - 1))
        point.append((col, row - 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_down(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture downwards
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y += 1
        inc += 1

    if line == goal:
        point.append((col, row + 1))
        point.append((col, row + 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_left(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture leftwards
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        x -= 1
        inc += 1

    if line == goal:
        point.append((col - 1, row))
        point.append((col - 2, row))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_right(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture rightwards
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        x += 1
        inc += 1

    if line == goal:
        point.append((col + 1, row))
        point.append((col + 2, row))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_up_left(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture upwards left
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y -= 1
        x -= 1
        inc += 1

    if line == goal:
        point.append((col - 1, row - 1))
        point.append((col - 2, row - 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_up_right(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture upwards right
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row

    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y -= 1
        x += 1
        inc += 1

    if line == goal:
        point.append((col + 1, row - 1))
        point.append((col + 2, row - 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_down_left(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture downwards left
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y += 1
        x -= 1
        inc += 1

    if line == goal:
        point.append((col - 1, row + 1))
        point.append((col - 2, row + 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO


def __check_down_right(row: int, col: int, goal, grid, size) -> CAPTURE:
    """Check if the player can capture downwards right
    :param row: y pos
    :param col: x pos
    :param goal: goal string to reach
    :param grid: the grid
    :param size: size of a line
    :return: Rule status
    """
    global point
    inc = 0
    line = ''
    x, y = col, row
    
    while 0 <= x < size and 0 <= y < size and inc < 4:
        line += str(grid[y][x])
        y += 1
        x += 1
        inc += 1
    if line == goal:
        point.append((col + 1, row + 1))
        point.append((col + 2, row + 2))
        return CAPTURE.CAPTURE
    elif inc != 4:
        return CAPTURE.NO_UP
    return CAPTURE.NO
