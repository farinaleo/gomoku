import pygame
import time
from ft_gomoku.engine import Engine, get_image, set_titlescreen, play_sound, stop_sound, load_music
from ft_gomoku.game.screen.components import draw_board, place_rocks, draw_rocks, redraw_board
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

	states = 0
	while True:
		elapsed_time = int(time.time() - start_time)
		redraw_board(engine, game_engine, board)
		states = print_subtitle(elapsed_time, engine, font)
		for event in pygame.event.get():
			if event.type in [pygame.KEYDOWN, pygame.QUIT]:
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
					stop_sound()
					engine.change_screen('main_menu')
					return 'quit'
		if states >= 0:
			anim_random_rock(engine, game_engine, board)
			pygame.display.update()


def print_subtitle(time: int, engine: Engine, font: pygame.freetype.Font):
	"""Print the subtitle at the given time"""
	states = 0
	subtitles = [(0, 2, "Gomoku is a tradional japanese board game"),
	             (3, 7, "where two players try to be the first one to get five pieces in a row on the board"),
	             (8, 13, "One player uses all of the black pieces, and the other player uses all of the white pieces"),
	             (14, 16, "The player with the black pieces goes first"),
	             (17, 21, "They place a black piece on one of the intersections made by the squares on the board"),
	             (22, 25, "Then the player with the white pieces takes a turn"),
	             (26, 30, "Players continue taking turns and placing pieces on the board"),
	             (31, 37, "The goal of the game is to get five pieces in a row horizontally, vertically, or diagonally"),
	             (38, 41, "While blocking the other player getting five in a row first"),
	             (42, 46, "The first player to get five in a row wins the game")]

	for start, end, subtitle in subtitles:
		states += 1
		if start <= time <= end:
			text_surface, text_rect = font.render(subtitle, (255, 255, 255))
			text_rect.center = (engine.get_window_size()[0] // 2, engine.get_window_size()[1] - 50)
			# Define the rectangle
			rect_width = engine.get_window_size()[0]
			rect_height = 25
			rect_x = (engine.get_window_size()[0] - rect_width) // 2
			rect_y = text_rect.centery - rect_height // 2
			rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

			# Fill the rectangle
			engine.screen.fill((8, 26, 43), rect)
			engine.screen.blit(text_surface, text_rect)
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
	print(player)
	rock_img = game_engine.get_rocks_img(player, last)
	anim_place_rock(screen, game_engine, coords, radius, player, False)
	screen.blit(rock_img, (coords[0] - radius // 2, coords[1] - radius // 2))


def anim_random_rock(engine: Engine, game_engine: GameStruct, board: dict) -> int:
	"""Animate the random rock placement
	"""
	clock = pygame.time.Clock()
	x = 3
	pygame.display.update()
	while x < 6:
		x += 1
		draw(engine.screen, game_engine, board[(x, 5)], 50, str(x % 2))
	return 1






