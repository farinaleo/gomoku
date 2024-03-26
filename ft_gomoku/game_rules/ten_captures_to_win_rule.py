#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from ft_gomoku import rule, RuleStatus


@rule()
def ten_capture_to_win(row: int, col: int, player, grid) -> RuleStatus:
	"""Check whether the given player captured ten stones
	:param row: y pos
	:param col: x pos
	:param player: who played the move
	:param grid: the grid
	:return: Rule status (WIN | OK)
	"""
	if grid.get_captured_stones(player) >= 10:
		return RuleStatus.WIN
	return RuleStatus.OK
