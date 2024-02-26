#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 7:36 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import copy
from dataclasses import dataclass
from ft_gomoku import RuleStatus


@dataclass
class Grid:
	"""Class to represent the grid game"""

	def __init__(self, size: int, player1, player2):
		"""Initialize the class
		:param size: The size of the grid
		"""
		if size is None or player1 is None or player2 is None or player1 == player2:
			raise ValueError("Grid initialisation failed due to bad parameters")
		self.__size = size
		self.__grid = [[0 for _ in range(size)] for _ in range(size)]
		self.__line_grid = [element for line in self.__grid for element in line]
		self.__last_move = [None, None, None]
		self.__player1 = player1
		self.__player2 = player2
		self.__captured_stones = {player1: 0, player2: 0}

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

	def get_player1(self):
		""" Return the player1
		:return: The player1
		"""
		return self.__player1

	def get_player2(self):
		""" Return the player2
		:return: The player 2
		"""
		return self.__player2

	def get_captured_stones(self, player):
		"""Get the number of captured stones
		:param player: The who captured the stones
		:return: The number of captured stones
		"""
		if player == self.__player1 or player == self.__player2:
			return self.__captured_stones[player]
		else:
			return None

	def add_rock(self, row: int, col: int, player, rules) -> RuleStatus:
		"""Add a rock to the grid
		:param row: y coordinate
		:param col: x coordinate
		:param player: player who wants to add the rock
		:param rules: rules functions to apply. They must return True if the add
			is allowed otherwise False [rule(row, col, player, grid) -> bool]
		:return: True if rock was added else False
		"""
		if 0 <= row < self.__size and 0 <= col < self.__size and self.__grid[row][col] == 0:
			grid_cp = copy.deepcopy(self)
			grid_cp.force_rock(col, row, player)
			if rules is not None:
				for rule in rules:
					if rule is None:
						pass
					res = rule(row, col, player, grid_cp, self)
					if res == RuleStatus.WIN:
						return RuleStatus.WIN
					elif res == RuleStatus.NO:
						return RuleStatus.NO
			self.force_rock(col, row, player)
			return RuleStatus.OK
		return RuleStatus.NO

	def remove_rock(self, col, row) -> RuleStatus:
		"""remove a rock from the grid
		:param col: x coordinate
		:param row: y coordinate
		:return: rule Status
		"""
		if 0 <= row < self.__size and 0 <= col < self.__size and self.__grid[row][col] != 0:
			self.__grid[row][col] = 0
			self.__line_grid[col + row * self.__size] = 0
			return RuleStatus.OK
		return RuleStatus.NO

	def force_rock(self, col, row, player) -> RuleStatus:
		"""force a rock in the grid
		:param col: x coordinate
		:param row: y coordinate
		:param player: player who want to force the rock
		:return: rule status
		"""
		self.__grid[row][col] = player
		self.__line_grid[col + row * self.__size] = player
		self.__last_move = [player, col, row]
		return RuleStatus.OK

	def cnt_capture(self, player, nb_stones: int):
		"""Add the captured stones to the count
		:param player: player who captured stones
		:param nb_stones: number of stones captured
		"""
		if player == self.__player1 or player == self.__player2:
			self.__captured_stones[player] += nb_stones