import pygame
import time

from ft_gomoku import Engine
from ft_gomoku.data_structure.GameStruct import GameStruct


def show_timer(engine: Engine, game_engine: GameStruct):
	"""Show the timer
	:param engine: the game engine
	:param game_engine: the game engine
	"""
	elapsed_time = int(time.time() - game_engine.get_time())
	player_1_time = round(game_engine.total_time_player_1[1], 2)
	player_2_time = round(game_engine.total_time_player_2[1], 2)
	player_1_avg = round(sum(game_engine.list_time_player_1) / len(game_engine.list_time_player_1), 2) if len(game_engine.list_time_player_1) > 0 else 0
	player_2_avg = round(sum(game_engine.list_time_player_2) / len(game_engine.list_time_player_2), 2) if len(game_engine.list_time_player_2) > 0 else 0

	# Create the text
	font = engine.font
	text_timer = font.render(f"Time : {elapsed_time} seconds", True, (255, 255, 255))
	text_rect = text_timer.get_rect(topleft=(10, 10))

	text_p1_timer = font.render(f"Player 1 reflection time : {player_1_time} seconds", True, (255, 255, 255))
	text_p1_rect = text_p1_timer.get_rect(topleft=(10, 40))

	text_p2_timer = font.render(f"Player 2 reflection time : {player_2_time} seconds", True, (255, 255, 255))
	text_p2_rect = text_p2_timer.get_rect(topleft=(10, 70))

	text_p1_avg = font.render(f"Player 1 average reflection time : {player_1_avg} seconds", True, (255, 255, 255))
	text_p1_avg_rect = text_p1_avg.get_rect(topleft=(10, 100))

	text_p2_avg = font.render(f"Player 2 average reflection time : {player_2_avg} seconds", True, (255, 255, 255))
	text_p2_avg_rect = text_p2_avg.get_rect(topleft=(10, 130))

	# Fill a rectangle with the background color to clean screen
	pygame.draw.rect(engine.screen, (8, 26, 43), text_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p1_avg_rect)
	pygame.draw.rect(engine.screen, (8, 26, 43), text_p2_avg_rect)

	engine.screen.blit(text_timer, (10, 10))
	engine.screen.blit(text_p1_timer, (10, 40))
	engine.screen.blit(text_p2_timer, (10, 70))
	engine.screen.blit(text_p1_avg, (10, 100))
	engine.screen.blit(text_p2_avg, (10, 130))
