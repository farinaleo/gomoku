import time
from random import randint
from typing import List, Tuple

import pygame
from ft_gomoku.engine.engine import Engine
from ft_gomoku.game.screen.particle import Particle, stars_effect
from ft_gomoku.engine.image_control import get_image
from ft_gomoku.engine.sound_control import play_sound
from ft_gomoku.data_structure.GameStruct import GameStruct


#TODO: change player value type

def anim_win(engine: Engine, game_engine: GameStruct, rocks_coord: dict):
	if game_engine.winner[2] == '5':
		five_win(engine, game_engine, rocks_coord)
	else:
		capture_win(engine, game_engine)


def five_win(engine: Engine, game_engine: GameStruct, rocks_coord: dict):
	winner = game_engine.winner[0]
	win_img = get_image('p1_win.png' if winner == '1' else 'p2_win.png', 1280 // 2, 720 // 2)
	groups_particles = pygame.sprite.Group()
	from ft_gomoku import draw_rocks
	for x in range(30):
		darken_screen(engine)
		for i in range(5):
			draw_rocks(engine.screen, game_engine, rocks_coord[game_engine.winner[1][i]], 35, game_engine.winner[0])
			pygame.display.update()
	play_sound('winning_sound.mp3')
	for i in range(5):
		draw_rocks(engine.screen, game_engine, rocks_coord[game_engine.winner[1][i]], 35, game_engine.winner[0], True)
		pygame.display.update()
		pygame.time.wait(100)
	pygame.time.wait(1000)
	play_sound('tada.mp3')
	while True:
		engine.screen.fill((8, 26, 43))
		stars_effect(20, engine.get_window_size()[0], engine.get_window_size()[1], groups_particles)
		groups_particles.update()
		groups_particles.draw(engine.screen)
		engine.screen.blit(win_img, (engine.get_window_size()[0] // 2 - win_img.get_width() // 2, engine.get_window_size()[1] // 2 - win_img.get_height() // 2))
		pygame.display.flip()
		engine.clock.tick(engine.settings.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return

def capture_win(engine: Engine, game_engine: GameStruct):
	winner = game_engine.winner[0]
	win_img = get_image('p1_captures_win.png' if winner == '1' else 'p2_captures_win.png', 1280 // 2, 720 // 2)
	groups_particles = pygame.sprite.Group()
	play_sound('tada.mp3')
	while True:
		engine.screen.fill((8, 26, 43))
		stars_effect(20, engine.get_window_size()[0], engine.get_window_size()[1], groups_particles)
		groups_particles.update()
		groups_particles.draw(engine.screen)
		engine.screen.blit(win_img, (engine.get_window_size()[0] // 2 - win_img.get_width() // 2, engine.get_window_size()[1] // 2 - win_img.get_height() // 2))
		pygame.display.flip()
		engine.clock.tick(engine.settings.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return


def darken_screen(engine: Engine):
	overlay = pygame.Surface((engine.screen.get_width(), engine.screen.get_height()))  # Create a new surface with screen dimensions
	overlay.set_alpha(15)
	overlay.fill((0, 0, 0))
	engine.screen.blit(overlay, (0, 0))
	pygame.display.flip()


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

	index = min(x, size - 1 - y)
	x -= index
	y += index
	if x < 0 or x > size - 1 or y < 0 or y > size:
		print("diag2 rwt", x, y)
		return None
	while x < size and 0 <= y:
		print("diag1", x, y)
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

	if x < 0 or x > size - 1 or y < 0 or y > size:
		return None
	while 0 <= x < size and 0 <= y < size:
		print("diag2", x, y)
		if game_engine.grid.line_grid[x + y * size] == rock:
			count += 1
			rocks.append((x, y))
		else:
			count = 0
			rocks = []
		if count == 5:
			print("diag2 rocks", rocks)
			return rocks
		x += 1
		y += 1
