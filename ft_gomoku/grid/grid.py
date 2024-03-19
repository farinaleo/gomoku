#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 2/25/24, 7:36 PM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import copy
import numpy as np
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
		self.winning = False
		self.size = size
		self.line_grid = ['0'] * (size * size)
		self.history = []
		self.player1 = player1
		self.player2 = player2
		self.captured_stones = {player1: 0, player2: 0}

	def __copy__(self):
		new_grid = Grid(self.size, self.player1, self.player2)
		new_grid.winning = self.winning
		new_grid.line_grid = self.line_grid[:]
		new_grid.history = self.history[:]
		new_grid.captured_stones = self.captured_stones.copy()
		return new_grid

	def __str__(self):
		"""Return a string representation of the grid
		:return: A string representation of the grid
		"""
		return str(self.line_grid)

	# def get_size(self):
	# 	"""Return the size of the grid
	# 	:return: The size of the grid
	# 	"""
	# 	return self.__size

	# def get_line(self):
	# 	"""Return the line representation of the grid
	# 	:return: The line representation of the grid
	# 	"""
	# 	return self.__line_grid

	def get_last_move(self, player=None, i=1):
		""" Return the last move played if the player is not specified,
		otherwise return the player last move.
		:param player: The player to search
		:param i: The index of the move (1 for the last, 2 for the last -1, ...)
		:return: [Player, x, y] | None if no move found
		"""
		cnt = 0
		if not self.history:
			return None
		if player is None:
			return self.history[-1]
		else:
			for move in reversed(self.history):
				if move[0] == player:
					cnt = cnt + 1
					if cnt == i:
						return move
		return None

	def __add_move(self, player, x, y):
		"""Add a move to the history.
		:param player: The player who did the move
		:param x: The coordinate of the move
		:param y: The coordinate of the move
		"""
		self.history.append((player, x, y))

	# def get_player1(self):
	# 	""" Return the player1
	# 	:return: The player1
	# 	"""
	# 	return self.__player1

	# def get_player2(self):
	# 	""" Return the player2
	# 	:return: The player 2
	# 	"""
	# 	return self.__player2

	def get_captured_stones(self, player):
		"""Get the number of captured stones
		:param player: The who captured the stones
		:return: The number of captured stones
		"""
		if player == self.player1 or player == self.player2:
			return self.captured_stones[player]
		else:			return None

	# def is_win(self):
	# 	""" Check if the game is over"""
	# 	return self.__winning

	def add_rock(self, row: int, col: int, player, rules) -> RuleStatus:
		"""Add a rock to the grid
		:param row: y coordinate
		:param col: x coordinate
		:param player: player who wants to add the rock
		:param rules: rules functions to apply. They must return True if the add
			is allowed otherwise False [rule(row, col, player, grid) -> bool]
		:return: True if rock was added else False
		"""
		if 0 <= row < self.size and 0 <= col < self.size and self.line_grid[col + row * self.size] == '0':
			grid_cp = self.__copy__()
			# grid_cp = self
			grid_cp.line_grid[col + row * grid_cp.size] = player
			grid_cp.__add_move(player, col, row)
			if rules is not None:
				for rule in rules:
					if rule is None:
						pass
					res = rule(row, col, player, grid_cp, self)
					if res == RuleStatus.WIN:
						self.winning = True
						return RuleStatus.WIN
					elif res == RuleStatus.NO:
						return RuleStatus.NO
			self.line_grid[col + row * self.size] = player
			self.__add_move(player, col, row)
			return RuleStatus.OK
		return RuleStatus.NO

	def remove_rock(self, col, row) -> RuleStatus:
		"""remove a rock from the grid
		:param col: x coordinate
		:param row: y coordinate
		:return: rule Status
		"""
		if 0 <= row < self.size and 0 <= col < self.size and self.line_grid[col + row * self.size] != '0':
			self.line_grid[col + row * self.size] = '0'
			return RuleStatus.OK
		return RuleStatus.NO

	def force_rock(self, col, row, player) -> RuleStatus:
		"""force a rock in the grid
		:param col: x coordinate
		:param row: y coordinate
		:param player: player who want to force the rock
		:return: rule status
		"""
		self.line_grid[col + row * self.size] = player
		self.__add_move(player, col, row)
		return RuleStatus.OK

	def cnt_capture(self, player, nb_stones: int):
		"""Add the captured stones to the count
		:param player: player who captured stones
		:param nb_stones: number of stones captured
		"""
		if player == self.player1 or player == self.player2:
			self.captured_stones[player] += nb_stones
		return 1