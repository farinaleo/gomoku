#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 6:08 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

from .logger.logger import log
from .game_rules.rule_status import CAPTURE, RuleStatus
from .grid.grid import Grid
from .game_rules.rules_decorator import rule
from .game_rules.five_to_win_rule import five_to_win
from .game_rules.capture import capture
from .game_rules.ten_captures_to_win_rule import ten_capture_to_win
from .game_rules.double_three_rule import double_three_forbidden
# from .data_structure import SettingsStruct
# from .engine import Engine, get_image, set_titlescreen, stop_sound, play_sound
# from .game import draw_rocks
# from .game import main_menu
# from .game import game_screen
# from .game import tutorial_screen
from .AI.next_generation import next_generation
from .AI import run_ai
