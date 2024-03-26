#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from enum import Enum


class RuleStatus(Enum):
	NO = -1
	OK = 0
	WIN = 1
	CAPTURE = 2


class CAPTURE(Enum):
	NO = -1
	OK = 0
	WIN = 1
	CAPTURE = 2
	NO_UP = -2
	NO_DOWN = -3
	NO_LEFT = -4
	NO_RIGHT = -5
