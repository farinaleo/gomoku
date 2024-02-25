#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 6:34 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from gomoku import RuleStatus


def rule():
    def decorator(func):
        def wrapper(row: int, col: int, player, grid, game):
            result = func(row, col, player, grid)
            if type(result) == tuple and result[0] == RuleStatus.CAPTURE:
                game.remove_rock(result[1][0][0], result[1][0][1])
                game.remove_rock(result[1][1][0], result[1][1][1])
                return RuleStatus.OK
            elif type(result) == RuleStatus and result == RuleStatus.WIN:
                game.force_rock(col, row, player)
            elif type(result) == RuleStatus and result == RuleStatus.NO:
                game.remove_rock(col, row)
            return result

        return wrapper

    return decorator
