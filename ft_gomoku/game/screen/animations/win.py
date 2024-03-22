from random import randint
from typing import List, Tuple

import pygame
from ft_gomoku.data_structure.GameStruct import GameStruct


#TODO: change player value type

def anim_win(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, player: int):
	print(game_engine.grid.line_grid)


def get_winner_rocks(game_engine: GameStruct) -> list[tuple[int, int]] | None:
	"""Found all rocks that make the winner line
	:param game_engine: the game engine
	:return: a list with the rocks that make the winner line
	"""
	player = game_engine.player_turn[1]
	if (rocks := check_row(game_engine, player)) is not None:
		return rocks
	if (rocks := check_col(game_engine, player)) is not None:
		return rocks
	if (rocks := check_diag1(game_engine, player)) is not None:
		return rocks
	if (rocks := check_diag2(game_engine, player)) is not None:
		return rocks
	return None


def check_row(game_engine: GameStruct, player: str) -> list[tuple[int, int]] | None:
	"""Check if the player win with a row
	:param game_engine: the game engine
	:param player: the player
	:return: a list with the rocks that make the winner line
	"""
	count = 0
	rocks = []
	size = game_engine.grid.size
	rock, x, y = game_engine.grid.get_last_move(player)

	for i in range(size):
		if game_engine.grid.line_grid[i + y * size] == rock:
			count += 1
			rocks.append((i, y))
		else:
			count = 0
			rocks = []
		if count == 5:
			return rocks
	return None


def check_col(game_engine: GameStruct, player: str) -> list[tuple[int, int]] | None:
	"""Check if the player win with a column
	:param game_engine: the game engine
	:param player: the player
	:return: a list with the rocks that make the winner line
	"""
	count = 0
	rocks = []
	size = game_engine.grid.size
	rock, x, y = game_engine.grid.get_last_move(player)

	for i in range(size):
		if game_engine.grid.line_grid[x + i * size] == rock:
			count += 1
			rocks.append((x, i))
		else:
			count = 0
			rocks = []
		if count == 5:
			return rocks
	return None


def check_diag1(game_engine: GameStruct, player: str) -> list[tuple[int, int]] | None:
	"""Check if the player win with a diagonal
	:param game_engine: the game engine
	:param player: the player
	:return: a list with the rocks that make the winner line
	"""
	count = 0
	rocks = []
	size = game_engine.grid.size
	rock, x, y = game_engine.grid.get_last_move(player)

	index = min(x, y)
	x -= index
	y += index

	while x < size - 1 and y >= 0:
		if game_engine.grid.line_grid[x + y * size] == rock:
			count += 1
			rocks.append((x, y))
		else:
			count = 0
			rocks = []
		if count == 5:
			return rocks
		x += 1
		y -= 1
	return None


def check_diag2(game_engine: GameStruct, player: str) -> list[tuple[int, int]] | None:
	"""Check if the player win with a diagonal
	:param game_engine: the game engine
	:param player: the player
	:return: a list with the rocks that make the winner line
	"""
	count = 0
	rocks = []
	size = game_engine.grid.size
	rock, x, y = game_engine.grid.get_last_move(player)

	index = min(x, y)
	x -= index
	y -= index

	while x < size - 1 and y >= 0:
		if game_engine.grid.line_grid[x + y * size] == rock:
			count += 1
			rocks.append((x, y))
		else:
			count = 0
			rocks = []
		if count == 5:
			return rocks
		x += 1
		y += 1
