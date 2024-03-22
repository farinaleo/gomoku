import pygame
import time
from ft_gomoku.engine import Engine, set_titlescreen, stop_sound, load_music
from ft_gomoku.game.screen.components import draw_board, redraw_board
from ft_gomoku.game.screen.animations import anim_place_rock
import pygame.freetype
from ft_gomoku.data_structure.GameStruct import GameStruct


def tutorial_screen(engine: Engine):
	stop_sound()
	set_titlescreen('Gomoku - Tutorial')

	game_engine = GameStruct(10, "Nolan", "Leo")
	game_engine.init_img(50)

	font = pygame.freetype.SysFont('ft_gomoku/assets/fonts/Roboto-Bold.ttf', 24)

	# Start the tutorial
	load_music('tutorial_gomoku.mp3', 0)
	start_time = time.time()
	board = draw_board(engine, game_engine)
	redraw_board(engine, game_engine, board)

	states_anim = [False, False, False, False, False, False, False, False, False]
	states = 0
	while True:
		elapsed_time = int(time.time() - start_time)
		states = print_subtitle(elapsed_time, engine, font)
		for event in pygame.event.get():
			if event.type in [pygame.KEYDOWN, pygame.QUIT]:
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
					stop_sound()
					engine.change_screen('main_menu')
					return 'quit'
		if states <= 2 and states_anim[0] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			states_anim[0] = anim_random_rock(engine, game_engine, board)
			continue
		elif 3 <= states < 4 and states_anim[1] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			states_anim[1] = anim_black_and_white_rock(engine, game_engine, board)
			continue
		elif 4 <= states < 5 and states_anim[2] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			states_anim[2] = anim_black_rock(engine, game_engine, board)
			continue
		elif 5 <= states < 6 and states_anim[3] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			draw(engine.screen, game_engine, board[(5, 5)], 50, '2')
			states_anim[3] = True
			continue
		elif 6 <= states < 7 and states_anim[4] is False:
			print_subtitle(elapsed_time, engine, font)
			pygame.time.wait(2000)
			draw(engine.screen, game_engine, board[(6, 6)], 50, '1')
			continue
		elif 6 <= states < 7 and states_anim[4] is False:
			print_subtitle(elapsed_time, engine, font)
			pygame.time.wait(2000)
			draw(engine.screen, game_engine, board[(6, 6)], 50, '1')
			states_anim[4] = True
			continue
		elif 7 <= states < 8 and states_anim[5] is False:
			pygame.time.wait(1500)
			print_subtitle(elapsed_time, engine, font)
			draw(engine.screen, game_engine, board[(5, 6)], 50, '2')
			states_anim[5] = True
			continue
		elif 8 <= states < 9 and states_anim[6] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			pygame.time.wait(2800)
			anim_horizontally(engine, game_engine, board)
			pygame.time.wait(100)
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			anim_vertically(engine, game_engine, board)
			pygame.time.wait(100)
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			states_anim[6] = anim_diagonally(engine, game_engine, board)
			continue
		elif 9 <= states < 10 and states_anim[7] is False:
			pygame.time.wait(1000)
			print_subtitle(elapsed_time, engine, font)
			draw(engine.screen, game_engine, board[(8, 8)], 50, '1')
			states_anim[7] = True
			continue
		elif 10 <= states < 11 and states_anim[8] is False:
			redraw_board(engine, game_engine, board)
			print_subtitle(elapsed_time, engine, font)
			states_anim[8] = anim_random_rock(engine, game_engine, board)
			engine.change_screen('main_menu')
			pygame.time.wait(2000)
			return


def print_subtitle(time: int, engine: Engine, font: pygame.freetype.Font):
	"""Print the subtitle at the given time"""
	states = 0
	subtitles = {
		(0, 2): "Gomoku is a tradional japanese board game",#1
		(3, 7): "where two players try to be the first one to get five pieces in a row on the board",#2
		(8, 13): "One player uses all of the black pieces, and the other player uses all of the white pieces",#3
		(14, 16): "The player with the black pieces goes first",#4
		(17, 21): "They place a black piece on one of the intersections made by the squares on the board",#5
		(22, 25): "Then the player with the white pieces takes a turn",#6
		(26, 30): "Players continue taking turns and placing pieces on the board",#7
		(31, 37): "The goal of the game is to get five pieces in a row horizontally, vertically, or diagonally",#8
		(38, 41): "While blocking the other player getting five in a row first",#9
		(42, 46): "The first player to get five in a row wins the game"#10
	}

	for timecode, subtitle in subtitles.items():
		states += 1
		if timecode[0] <= time <= timecode[1]:
			text_surface, text_rect = font.render(subtitle, (255, 255, 255))
			text_rect.center = (engine.get_window_size()[0] // 2, engine.get_window_size()[1] - 50)
			rect_width = engine.get_window_size()[0]
			rect_height = 25
			rect_x = (engine.get_window_size()[0] - rect_width) // 2
			rect_y = text_rect.centery - rect_height // 2
			rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

			engine.screen.fill((8, 26, 43), rect)
			engine.screen.blit(text_surface, text_rect)
			pygame.display.update()
			return states
	return 0


def draw(screen: pygame.Surface, game_engine: GameStruct, coords: tuple, radius: int, player, last: bool = False): # TODO: change player: int to player: str
	"""Draw the rocks on the screen
	:param screen: the pygame screen
	:param game_engine: the game engine
	:param coords: the coordinates of the rocks
	:param radius: the radius of the rocks
	:param player: the player
	:param last: if the rock is the last one
	"""
	rock_img = game_engine.get_rocks_img(player, last)
	anim_place_rock(screen, game_engine, coords, radius, player, False)
	screen.blit(rock_img, (coords[0] - radius // 2, coords[1] - radius // 2))


def anim_random_rock(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the random rock placement
	"""
	x = 3
	y = 5
	pygame.display.update()
	while x < 6:
		x += 1
		draw(engine.screen, game_engine, board[(x, y)], 50, '1' if x % 2 else '2')
	while y < 7:
		y += 1
		x -= 1
		draw(engine.screen, game_engine, board[(x, y)], 50, '1' if x % 2 else '2')
	return True


def anim_black_and_white_rock(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the black rock placement
	"""
	y = 2
	pygame.display.update()
	while y < 6:
		y += 1
		draw(engine.screen, game_engine, board[(4, y)], 50, '2')
	y = 2
	pygame.time.wait(2000)
	while y < 6:
		y += 1
		draw(engine.screen, game_engine, board[(6, y)], 50, '1')
	return True


def anim_black_rock(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the black rock placement
	"""
	y = 2
	pygame.display.update()
	while y < 6:
		y += 1
		draw(engine.screen, game_engine, board[(5, y)], 50, '2')
	return True


def anim_horizontally(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the black rock placement horizontally"""
	x = 4
	pygame.display.update()
	while x < 8:
		x += 1
		draw(engine.screen, game_engine, board[(x, 5)], 50, '2')
	return True


def anim_vertically(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the black rock placement vertically"""
	y = 4
	pygame.display.update()
	while y < 8:
		y += 1
		draw(engine.screen, game_engine, board[(5, y)], 50, '2')
	return True


def anim_diagonally(engine: Engine, game_engine: GameStruct, board: dict) -> bool:
	"""Animate the black rock placement diagonally"""
	y = 4
	x = 4
	pygame.display.update()
	while x < 7:
		y += 1
		x += 1
		draw(engine.screen, game_engine, board[(x, y)], 50, '2')
	return True




