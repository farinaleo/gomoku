import pygame
from ft_gomoku import Engine
from ft_gomoku.data_structure.GameStruct import GameStruct


def show_capture(engine: Engine, game_engine: GameStruct):
	"""Show the capture
	:param engine: the game engine
	:param game_engine: the game engine
	"""
	font = engine.font

	player_1_capture = game_engine.grid.get_captured_stones(game_engine.player_1[1])
	player_2_capture = game_engine.grid.get_captured_stones(game_engine.player_2[1])

	text_p1_capture = font.render(f'Player 1: {player_1_capture} x ', True, (255, 255, 255))
	text_p2_capture = font.render(f'Player 2: {player_2_capture} x ', True, (255, 255, 255))

	img_p1 = game_engine.get_rocks_img(game_engine.player_2[1], False)
	img_p2 = game_engine.get_rocks_img(game_engine.player_1[1], False)

	text_p1_rect = text_p1_capture.get_rect(topleft=(10, engine.window_size[1] // 2))
	text_p2_rect = text_p1_capture.get_rect(topleft=(10, engine.window_size[1] // 2 + 50))

	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_rect)

	engine.screen.blit(text_p1_capture, (10, engine.window_size[1] // 2))
	engine.screen.blit(text_p2_capture, (10, engine.window_size[1] // 2 + 50))

	engine.screen.blit(img_p1, (130, engine.window_size[1] // 2 - 5))
	engine.screen.blit(img_p2, (130, engine.window_size[1] // 2 + 50 - 5))
