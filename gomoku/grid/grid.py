#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 5:27 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import copy
from dataclasses import dataclass
import gomoku.game_rules as gm_rules

@dataclass
class Grid:
	"""Class to represent the grid game"""

	def __init__(self, size: int):
		"""Initialize the class
		:param size: The size of the grid
		"""
		self.__size = size
		self.__grid = [[0 for _ in range(size)] for _ in range(size)]
		self.__line_grid = [element for line in self.__grid for element in line]
		self.__last_move = [None, None, None]

	def __str__(self):
		"""Return a string representation of the grid
		:return: A string representation of the grid
		"""
		return str(self.__grid)

	def get_size(self):
		"""Return the size of the grid
		:return: The size of the grid
		"""
		return self.__size

	def get_grid(self):
		"""Return the grid representation
		:return: The grid representation as [[]]
		"""
		return self.__grid

	def get_line(self):
		"""Return the line representation of the grid
		:return: The line representation of the grid
		"""
		return self.__line_grid

	def get_last_move(self):
		""" Return the last move played
		:return: [Player, x, y]
		"""
		return self.__last_move

	def add_rock(self, row: int, col: int, player, rules) -> gm_rules.RuleStatus:
		"""Add a rock to the grid
		:param row: y coordinate
		:param col: x coordinate
		:param player: player who wants to add the rock
		:param rules: rules functions to apply. They must return True if the add
			is allowed otherwise False [rule(row, col, player, grid) -> bool]
		:return: True if rock was added else False
		"""
		if 0 <= row < self.__size and 0 <= col < self.__size and self.__grid[row][col] == 0:
			grid_cp = copy.deepcopy(self.__grid)
			grid_cp[row][col] = player
			if rules is not None:
				for rule in rules:
					if rule is None:
						pass
					res = rule(row, col, player, grid_cp)
					if res == gm_rules.RuleStatus.WIN:
						return gm_rules.RuleStatus.WIN
					elif res == gm_rules.RuleStatus.NO:
						return gm_rules.RuleStatus.NO
			self.__grid[row][col] = player
			self.__line_grid[col + row * self.__size] = player
			self.__last_move = [player, col, row]
			return gm_rules.RuleStatus.OK
		return gm_rules.RuleStatus.NO
