import time
import pygame
from ft_gomoku.engine.engine import Engine
from ft_gomoku.engine.image_control import get_image
from ft_gomoku.engine.sound_control import play_sound
from ft_gomoku.game.screen.components.particle import stars_effect
from ft_gomoku.data_structure.GameStruct import GameStruct


def anim_win(engine: Engine, game_engine: GameStruct, rocks_coord: dict, loose: bool = False):
	"""Animate the win
	:param engine: the game engine
	:param game_engine: the game engine
	:param rocks_coord: the rocks coordinates
	:param loose: if the player loose
	"""
	# player_1_time = round(game_engine.total_time_player_1[1], 2)
	# player_2_time = round(game_engine.total_time_player_2[1], 2)
	# player_1_avg = round(sum(game_engine.list_time_player_1) / len(game_engine.list_time_player_1), 2) if len(
	# 	game_engine.list_time_player_1) > 0 else 0
	# player_2_avg = round(sum(game_engine.list_time_player_2) / len(game_engine.list_time_player_2), 2) if len(
	# 	game_engine.list_time_player_2) > 0 else 0
	# print(f' Winner : {game_engine.winner[0]}, average time {player_1_avg} for p1 and {player_2_avg} for p2')
	end_time = time.time()
	if game_engine.winner[2] == '5':
		five_win(engine, game_engine, rocks_coord, end_time, loose)
	else:
		capture_win(engine, game_engine, end_time, loose)


def five_win(engine: Engine, game_engine: GameStruct, rocks_coord: dict, end_time: float, loose: bool):
	"""Animate the win with five rocks
	:param engine: the game engine
	:param game_engine: the game engine
	:param rocks_coord: the rocks coordinates
	:param end_time: the end time
	:param loose: if the player loose
	"""
	from ft_gomoku import draw_rocks

	for x in range(30):
		darken_screen(engine)
		for i in range(5):
			draw_rocks(engine.screen, game_engine, rocks_coord[game_engine.winner[1][i]], engine.rocks_size, game_engine.winner[0])
			pygame.display.update()
	play_sound('winning_sound.mp3')
	for i in range(5):
		draw_rocks(engine.screen, game_engine, rocks_coord[game_engine.winner[1][i]], engine.rocks_size, game_engine.winner[0], True)
		pygame.display.update()
		pygame.time.wait(100)
	pygame.time.wait(1000)
	play_sound('failure.mp3' if loose else 'tada.mp3')
	end_screen(engine, game_engine, end_time)


def capture_win(engine: Engine, game_engine: GameStruct, end_time: float, loose: bool):
	"""Animate the win with the capture
	:param engine: the game engine
	:param game_engine: the game engine
	:param end_time: the end time
	:param loose: if the player loose
	"""
	dx = 0
	dy = 0
	rock_img = game_engine.rock_black_img if game_engine.winner[0] == '2' else game_engine.rock_white_img
	for x in range(30):
		darken_screen(engine)
	for i in range(10):
		engine.screen.blit(rock_img, (engine.window_size[0] // 2 + dx * 40 - (40*2.5), engine.window_size[1] // 2 + dy * 40))
		dx += 1
		if dx == 5:
			dx = 0
			dy += 1
		play_sound('pop.mp3')
		pygame.display.flip()
		engine.clock.tick(engine.settings.get_fps())
		pygame.time.wait(140)
	pygame.time.wait(1000)
	play_sound('failure.mp3' if loose else 'tada.mp3')
	end_screen(engine, game_engine, end_time)


def end_screen(engine: Engine, game_engine: GameStruct, end_time: float):
	"""Show the end screen
	:param engine: the game engine
	:param game_engine: the game engine
	:param end_time: the end time
	"""
	winner = game_engine.winner[0]
	win_img = get_image('p1_wins.png' if winner == '1' else 'p2_wins.png', 1280 // 2, 720 // 2)
	groups_particles = pygame.sprite.Group()
	while True:
		engine.screen.fill((8, 26, 43))
		stars_effect(20, engine.get_window_size()[0], engine.get_window_size()[1], groups_particles)
		groups_particles.update()
		groups_particles.draw(engine.screen)
		engine.screen.blit(win_img, (engine.get_window_size()[0] // 2 - win_img.get_width() // 2,
		                             engine.get_window_size()[1] // 2 - win_img.get_height() // 2))
		show_party_information(engine, game_engine, end_time)
		pygame.display.flip()
		engine.clock.tick(engine.settings.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				engine.change_screen('main_menu')
				return


def show_party_information(engine: Engine, game_engine: GameStruct, end_time: float):
	"""Show the party information
	:param engine: the game engine
	:param game_engine: the game engine
	:param end_time: the end time
	"""
	font = engine.font
	p1_total_rocks = game_engine.grid.get_captured_stones(game_engine.player_2[1])
	p2_total_rocks = game_engine.grid.get_captured_stones(game_engine.player_1[1])
	total_time = int(end_time - game_engine.get_time())
	for i in range(game_engine.grid.size * game_engine.grid.size):
		if game_engine.grid.line_grid[i] == '1':
			p1_total_rocks += 1
		elif game_engine.grid.line_grid[i] == '2':
			p2_total_rocks += 1
	total_turns = min(p1_total_rocks, p2_total_rocks)
	text_time = font.render(f'Total time: {total_time} seconds', True, (255, 255, 255))
	text_turn = font.render(f'Total turns: {total_turns}', True, (255, 255, 255))
	text_turn_rect = text_turn.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] - 140))
	text_time_rect = text_time.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] - 100))
	engine.screen.blit(text_turn, text_turn_rect)
	engine.screen.blit(text_time, text_time_rect)


def darken_screen(engine: Engine):
	"""Darken the screen
	:param engine: the game engine
	"""
	overlay = pygame.Surface((engine.screen.get_width(), engine.screen.get_height()))
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
		return None
	while x < size and 0 <= y:
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
