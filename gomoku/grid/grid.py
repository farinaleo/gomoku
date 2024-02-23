from dataclasses import dataclass


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

	def add_rock(self, row: int, col: int, player, rules) -> bool:
		"""Add a rock to the grid
		:param row: y coordinate
		:param col: x coordinate
		:param player: player who wants to add the rock
		:param rules: rules functions to apply. They must return True if the add
			is allowed otherwise False [rule(row, col, grid) -> bool]
		:return: True if rock was added else False
		"""
		if 0 <= row < self.__size and 0 <= col < self.__size and self.__grid[row][col] == 0:
			for rule in rules:
				if not rule(row, col, self.__grid):
					return False
			self.__grid[row][col] = player
			self.__line_grid[col + row * self.__size] = player
			return True
		return False
