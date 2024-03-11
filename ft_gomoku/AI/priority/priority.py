#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/10/24, 1:19 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.


from ft_gomoku import Grid


def is_critical(grid: Grid, x: int, y: int, player) -> bool:
	"""
	Checks if the move is critical (probably winning).
	:param grid: the game.
	:param x: coordinate x.
	:param y: coordinate y.
	:param player: the player who placed the stone.
	:return: True if the move is critical, False otherwise.
	"""
	# is in a four alignment (or three)
	# has captured 8 opponent stones
