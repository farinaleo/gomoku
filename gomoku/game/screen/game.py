import pygame
from gomoku.game.engine import Engine, load_music, get_image, set_titlescreen


def handle_events(engine, events_list) -> str | bool:
	for event in pygame.event.get():
		if event.type in [pygame.VIDEORESIZE]:
			if not engine.settings.get_fullscreen():
				engine.update_screen_size()
				return 'restart'
		if event.type in [pygame.KEYDOWN, pygame.QUIT]:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
				print('quit')
				engine.set_running(False)
				return 'quit'
	return True


def game_screen(engine: Engine):
	set_titlescreen('Gomoku - Game')
	while True:
		events_list = []
		running = True

		while running:
			engine.screen.fill((8, 26, 43))
			draw_board(engine)

			result = handle_events(engine, events_list)
			if result == 'quit':
				return
			pygame.display.update()


def draw_board(engine: Engine):
	"""Draw the game board"""
	image = get_image('grid_19x19.png', 2000, 2000)
	image_width = 800
	image_height = 800
	ratio_width = engine.get_window_size()[0] / 1920
	ratio_height = engine.get_window_size()[1] / 1080
	image = pygame.transform.scale(image, (image_width * ratio_width, image_height * ratio_height))
	image_rect = image.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] // 2))
	engine.screen.blit(image, image_rect)
