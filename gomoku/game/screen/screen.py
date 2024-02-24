from random import choice, uniform, randint

import pygame
from gomoku.game.engine import Engine
from gomoku.data_structure import SettingsStruct
from gomoku.game.engine import load_music
from gomoku.game.screen.particle import stars_effect


def main_menu(engine: Engine):
	""" Main menu screen """
	pygame.display.set_caption('Gomoku - Title screen')
	engine.screen.fill((8, 26, 43))
	pygame.display.update()
	load_music('title_screen.mp3')

	screen_width, screen_height = engine.settings.get_window_size()
	image = pygame.image.load('gomoku/assets/img/logo-game.png')
	image_width = screen_width // 3
	aspect_ratio = image.get_width() / image.get_height()
	image_height = int(image_width / aspect_ratio)

	image = pygame.transform.scale(image, (image_width, image_height))
	logo_rect = image.get_rect()
	logo_rect.center = (screen_width // 2, image_height // 2)

	running = True
	group_particles = pygame.sprite.Group()
	while running:
		dt = engine.clock.tick(engine.settings.get_fps()) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		engine.screen.fill((8, 26, 43))
		engine.screen.blit(image, logo_rect)
		stars_effect(20, engine.settings.get_width(), engine.settings.get_height(), group_particles)
		group_particles.draw(engine.screen)
		group_particles.update(dt)
		pygame.display.update()
	engine.change_screen(None)
