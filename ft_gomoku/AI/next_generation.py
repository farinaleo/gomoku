#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/1/24, 11:13 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import Grid, RuleStatus
from ft_gomoku.AI import heuristic as heuristic_f

mem_grid = {}


def next_generation(grid: Grid, rules, ai_value, first_call=False, debug=False):
    """Generate the next generation from the given grid by placing the player.
    :param grid: the grid to extend
    :param rules: the rules aplay to the game
    :param ai_value: the value used to identify the AI.
    :return: a list of ft_gomoku.grid representing the next generation
    """
    i = 0
    global mem_grid
    if first_call:
        mem_grid.clear()
    new_gen = []
    line = grid.line_grid
    size = grid.size
    line_size = len(line)
    bypass = 'middle' if line.count('0') > line_size - 2 else None
    player, opponent = (grid.player1, grid.player2) if ai_value == grid.player1 else (grid.player2, grid.player1)

    cluster = __cluster(line, size, line_size, player, opponent, bypass)
    for cell in cluster:
        if (line[cell[0] + cell[1] * size] == '0'
                and 0 <= cell[0] < size
                and 0 <= cell[1] < size):
            _next = grid.__copy__()
            if _next.add_rock(row=cell[1], col=cell[0], player=player, rules=rules) != RuleStatus.NO:
                _next.heuristic = heuristic_f(_next, player)
                if mem_grid.get(str(_next)) and mem_grid.get(str(_next)).heuristic >= _next.heuristic:
                    continue
                new_gen.append(_next)
                mem_grid[str(_next)] = _next
    if len(new_gen) == 0:
        cluster.clear()
        while len(new_gen) == 0 and i < line_size:
            for cell in cluster:
                if (line[cell[0] + cell[1] * size] == '0'
                        and 0 <= cell[0] < size
                        and 0 <= cell[1] < size):
                    _next = grid.__copy__()
                    if _next.add_rock(row=cell[1], col=cell[0], player=player, rules=rules) != RuleStatus.NO:
                        _next.heuristic = heuristic_f(_next, player)
                        if mem_grid.get(str(_next)) and mem_grid.get(str(_next)).heuristic >= _next.heuristic:
                            continue
                        new_gen.append(_next)
                        mem_grid[str(_next)] = _next
            if len(new_gen) == 0:
                cluster.clear()
                cluster.append((i % size, i // size))
                i = i + 1

    new_gen.sort(key=None, reverse=True if ai_value == grid.player1 else True)
    if first_call:
        new_gen = new_gen[:min(len(new_gen), 4)]
    else:
        new_gen = new_gen[:min(len(new_gen), 3)]
    if debug:
        _points = []
        for cell in new_gen:
            _points.append(cell.get_last_move()[-2:])
        return _points
    return new_gen


def __cluster(line, size, line_size, p1, p2, bypass):
    """ determining the search area and return a points cluster.
    :param line: the game as line.
    :param size: the grid size.
    :param line_size: the total line size len(line).
    :param p1: the player.
    :param p2: the opponent.
    :param bypass: allow the middle expansion if the grid contains one stone.
    :return: a points list.
    """
    cluster = []

    try:
        first_p1 = line.index(p1)
    except ValueError:
        first_p1 = 19 * 19
        pass
    try:
        first_p2 = line.index(p2)
    except ValueError:
        first_p2 = 19 * 19
        pass
    i = min(first_p1, first_p2)
    i = max(i, 0)

    try:
        last_p1 = line_size - line[::-1].index(p1)
    except ValueError:
        last_p1 = 0
        pass
    try:
        last_p2 = line_size - line[::-1].index(p2)
    except ValueError:
        last_p2 = 0
        pass
    end = max(last_p1, last_p2)
    end = min(end, line_size)

    expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'attack', 4)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'defend', 5)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'full_miam', 5)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'defend', 4)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'all', 3)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'attack', 3)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'attack', 2)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'attack', 1)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'defend', 2)
    if len(cluster) == 0:
        expend_cluster(line, i, end, size, p1, p2, cluster, bypass if bypass is not None else 'attack', 0)
    if len(cluster) == 0:
        mid = size // 2
        if line[mid + mid * size] == '0':
            cluster.append((mid, mid))
    return cluster


def expend_cluster(line, i, end, size, p1, p2, cluster, bypass, nb_friends=4):
    """ Expend the cluster with the next points to explore.
    :param line: the game as line.
    :param i: the starting point.
    :param end: the ending point.
    :param size: the grid size.
    :param p1: the player.
    :param p2: the opponent.
    :param cluster: the points cluster.
    :param bypass: allow the middle expansion if the grid contains one stone.
    :param nb_friends: the total friends number to have to admit a point.
    :return: a points list.
    """
    while i < end:
        x = i % size
        y = i // size
        if line[i] != '0':
            _up = y - 1
            _down = y + 1
            _left = x - 1
            _right = x + 1
            # up left
            if can_expend(line, i, x, y, _left, _up, size, p1, p2, bypass, nb_friends):
                if (_left, _up) not in cluster:
                    cluster.append((_left, _up))
            # up mid
            if can_expend(line, i, x, y, x, _up, size, p1, p2, bypass, nb_friends):
                if (x, _up) not in cluster:
                    cluster.append((x, _up))
            # up right
            if can_expend(line, i, x, y, _right, _up, size, p1, p2, bypass, nb_friends):
                if (_right, _up) not in cluster:
                    cluster.append((_right, _up))
            # mid left
            if can_expend(line, i, x, y, _left, y, size, p1, p2, bypass, nb_friends):
                if (_left, y) not in cluster:
                    cluster.append((_left, y))
            # mid right
            if can_expend(line, i, x, y, _right, y, size, p1, p2, bypass, nb_friends):
                if (_right, y) not in cluster:
                    cluster.append((_right, y))
            # down left
            if can_expend(line, i, x, y, _left, _down, size, p1, p2, bypass, nb_friends):
                if (_left, _down) not in cluster:
                    cluster.append((_left, _down))
            # down mid
            if can_expend(line, i, x, y, x, _down, size, p1, p2, bypass, nb_friends):
                if (x, _down) not in cluster:
                    cluster.append((x, _down))
            # down right
            if can_expend(line, i, x, y, _right, _down, size, p1, p2, bypass, nb_friends):
                if (_right, _down) not in cluster:
                    cluster.append((_right, _down))
        i = i + 1


def can_expend(line, i, x, y, x_exp, y_exp, size, player, opponent, bypass, nb_friends) -> bool:
    """Allow the expansion for the search.
    :param line: the game as line.
    :param i: the starting point index
    :param x: the starting x coordinate.
    :param y: the starting y coordinate.
    :param x_exp: the expansion x coordinate.
    :param y_exp: the expansion y coordinate.
    :param size: the grid size.
    :param player: the player value.
    :param opponent: the opponent value.
    :param bypass: allow the middle expansion if the grid contains one stone.
    :param nb_friends: the total friends number to have to admit a point.
    :return: True if the expansion is allowed, otherwise False.
    """
    if line[i] == player and bypass != 'defend':
        if 0 <= x_exp < size and 0 <= y_exp < size and line[x_exp + y_exp * size] == '0':
            if bypass == 'full_miam':
                if dir_capture(line, x_exp, y_exp, x - x_exp, y - y_exp, size, player, opponent):
                    return True
            if dir_friends(line, x_exp, y_exp, x - x_exp, y - y_exp, size, player, opponent, nb_friends):
                return True
            if dir_capture(line, x_exp, y_exp, x - x_exp, y - y_exp, size, opponent, player):
                return True
            if dir_protect(line, x_exp, y_exp, x - x_exp, y - y_exp, size, player, opponent):
                return True
            return False
    elif line[i] == opponent and (opponent == '2' or bypass != 'attack'):
        if 0 <= x_exp < size and 0 <= y_exp < size and line[x_exp + y_exp * size] == '0':
            if bypass == 'middle' and x == size // 2 and y == size // 2:
                return True
            if bypass == 'full_miam':
                if dir_capture(line, x_exp, y_exp, x - x_exp, y - y_exp, size, opponent, player):
                    return True
            if dir_friends(line, x_exp, y_exp, x - x_exp, y - y_exp, size, opponent, player, nb_friends):
                return True
            if dir_capture(line, x_exp, y_exp, x - x_exp, y - y_exp, size, player, opponent):
                return True
    return False


def dir_protect(line, x, y, x_dir, y_dir, size, player, opponent):
    """Check if the player is able to capture the opponent.
    :param line:
    :param x:
    :param y:
    :param x_dir:
    :param y_dir:
    :param size:
    :param player:
    :param opponent:
    :return:
    """
    if 0 <= x < size and 0 <= y < size:
        if 0 <= x + x_dir < size and 0 <= y + y_dir < size \
                and line[(x + x_dir) + (y + y_dir) * size] == player:
            if 0 <= x + x_dir * 2 < size and 0 <= y + y_dir * 2 < size \
                    and line[(x + x_dir * 2) + (y + y_dir * 2) * size] == player:
                if 0 <= x + x_dir * 3 < size and 0 <= y + y_dir * 3 < size \
                        and line[(x + x_dir * 3) + (y + y_dir * 3) * size] == opponent:
                    return True
    return False


def dir_friends(line, x, y, x_dir, y_dir, size, player, opponent, nb_friends):
    """
    Count the number of available friends around the point.
    :param line: the game as line.
    :param x: the starting x coordinate.
    :param y: the starting y coordinate.
    :param x_dir: the x direction.
    :param y_dir: the y direction.
    :param size: the game size.
    :param player: the player value.
    :param opponent: the opponent value.
    :param nb_friends: the total friends number to have to admit a point.
    :return:
    """
    i = 0
    cnt_friends = 0
    tmp_x = x
    tmp_y = y
    while i < 5 and 0 <= x < size and 0 <= y < size and line[x + y * size] != opponent and nb_friends > 0:
        if line[x + y * size] == player:
            cnt_friends = cnt_friends + 1
        x = x + x_dir
        y = y + y_dir
        i = i + 1
    i = 0
    x = tmp_x
    y = tmp_y
    while i < 5 and 0 <= x < size and 0 <= y < size and line[x + y * size] != opponent and nb_friends > 0:
        if line[x + y * size] == player:
            cnt_friends = cnt_friends + 1
        x = x - x_dir
        y = y - y_dir
        i = i + 1
    return cnt_friends >= nb_friends


def dir_capture(line, x, y, x_dir, y_dir, size, player, opponent):
    """ Check if the player is able to capture the opponent.
    :param line: the game as line.
    :param x: the starting x coordinate.
    :param y: the starting y coordinate.
    :param x_dir: the x direction.
    :param y_dir: the y direction.
    :param size: the game size.
    :param player: the player value.
    :param opponent: the opponent value.
    :param nb_friends: the total friends number to have to admit a point.
    :return:
    """
    if 0 <= x < size and 0 <= y < size:
        if 0 <= x + x_dir < size and 0 <= y + y_dir < size \
                and line[(x + x_dir) + (y + y_dir) * size] == opponent:
            if 0 <= x + x_dir * 2 < size and 0 <= y + y_dir * 2 < size \
                    and line[(x + x_dir * 2) + (y + y_dir * 2) * size] == opponent:
                if 0 <= x + x_dir * 3 < size and 0 <= y + y_dir * 3 < size \
                        and line[(x + x_dir * 3) + (y + y_dir * 3) * size] == player:
                    return True
    return False
